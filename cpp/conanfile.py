from conans import ConanFile, CMake, tools


class ProjectEulerConan(ConanFile):
    name = "project_euler"
    version = "0.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of ProjectEuler here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    generators = "cmake"
    export_sources="src/*"
    build_requires="cmake/3.19.6"

    def configure(self):
        self.options["cmake"].with_openssl = True

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
        cmake.install()
