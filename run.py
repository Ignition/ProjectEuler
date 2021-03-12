#!/usr/bin/env python3
import argparse

import os
from contextlib import contextmanager

script_loc = os.path.dirname(__file__)

@contextmanager
def working_directory(directory):
    owd = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(owd)

def cpp(args):
    os.system("conan install . -if build -s build_type=Release -s cppstd=20 --build missing")
    os.system("conan build . -bf build -pf .")
    if args.problem == 'all':
        for file in os.listdir("./bin"):
            os.system(f"echo -n '{file}: '; ./bin/{file}")
    else:
        os.system(f"./bin/{args.problem}")

def main():
    all_languages = ['cpp', 'rust', 'java']

    parser = argparse.ArgumentParser()
    parser.add_argument('--benchmark', action='store_true')
    parser.add_argument('language', default='cpp', nargs='?', choices=all_languages + ['all'])
    parser.add_argument('problem', default='all', nargs='?')
    args = parser.parse_args()

    languages = all_languages if args.language == 'all' else [args.language]
    switcher = {'cpp':cpp}

    for language in languages:
        with working_directory(os.path.join(script_loc,language)):
            switcher[language](args)

if __name__ == "__main__":
    main()
