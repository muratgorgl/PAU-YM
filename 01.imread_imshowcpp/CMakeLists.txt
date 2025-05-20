cmake_minimum_required(VERSION 3.10)
project(IlkDers)

# Find OpenCV package
find_package(OpenCV REQUIRED)

# Include directories from OpenCV
include_directories(${OpenCV_INCLUDE_DIRS})

# create an executable
add_executable(IlkDers main.cpp)

# Link OpenCV libraries
target_link_libraries(IlkDers ${OpenCV_LIBS})