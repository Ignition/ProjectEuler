#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--benchmark', action='store_true')
    parser.add_argument('language', nargs='?', default='cpp', choices=['cpp', 'rust', 'java', 'all'])
    parser.add_argument('problem', default='all', nargs='?')
    args = parser.parse_args()
    print(vars(args))

if __name__ == "__main__":
    main()
