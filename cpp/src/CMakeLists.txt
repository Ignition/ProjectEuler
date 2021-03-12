cmake_minimum_required(VERSION 3.19.6)
project(project_euler)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(1 1.hpp 1.cpp)
install(TARGETS 1)
