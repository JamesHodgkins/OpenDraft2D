cmake_minimum_required(VERSION 3.14)

# Set the project name
project(OpenDraft)




# ========================================================
# Add sources
# Collect the Python files
# Collect Python files
file(GLOB PYTHON_SOURCES "${CMAKE_SOURCE_DIR}/python/*.*")

# Create a custom target to hold these files in the Visual Studio solution
add_custom_target(PythonFiles SOURCES ${PYTHON_SOURCES})

# Optional: Organize the files in a source group for easy navigation in Visual Studio
source_group("Python Files" FILES ${PYTHON_SOURCES})


# ========================================================



# Set the path to the Python virtual environment
set(VENV_PATH "${CMAKE_BINARY_DIR}/venv")

# Manually set the Python executable
set(Python3_EXECUTABLE "C:/Users/jlh33/AppData/Local/Programs/Python/Python310/python.exe")

# Find Python development libraries
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Check if Python executable was found
if(NOT EXISTS ${Python3_EXECUTABLE})
    message(FATAL_ERROR "Python interpreter not found: ${Python3_EXECUTABLE}")
endif()

# Create the virtual environment
execute_process(
    COMMAND ${Python3_EXECUTABLE} -m venv "${VENV_PATH}"
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    RESULT_VARIABLE result
)
if(result)
    message(FATAL_ERROR "Failed to create virtual environment. Exit code: ${result}")
else()
    message(STATUS "Virtual environment created at: ${VENV_PATH}")
endif()

# Optionally install dependencies from requirements.txt
if(EXISTS "${CMAKE_SOURCE_DIR}/requirements.txt")
    set(PIP_EXECUTABLE "${VENV_PATH}/Scripts/pip")  # Use "bin/pip" on Linux/Mac

    execute_process(
        COMMAND ${PIP_EXECUTABLE} install -r ${CMAKE_SOURCE_DIR}/requirements.txt
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
        RESULT_VARIABLE pip_result
    )
    if(pip_result)
        message(FATAL_ERROR "Failed to install dependencies. Exit code: ${pip_result}")
    else()
        message(STATUS "Dependencies installed from requirements.txt")
    endif()
endif()

# Set the Python executable to use
set(PYTHON_EXECUTABLE "${Python3_EXECUTABLE}")

# Specify the path to PySide6 installation
set(PYSIDE6_INCLUDE_DIR "${VENV_PATH}/Lib/site-packages/PySide6")
set(PYSIDE6_LIB_DIR "${VENV_PATH}/Lib/site-packages/PySide6")

# Include PySide6 headers
include_directories(${PYSIDE6_INCLUDE_DIR})

# Create a list of libraries to link against (if needed)
set(PYSIDE6_LIBRARIES
    ${PYSIDE6_LIB_DIR}/PySide6.dll   # Adjust for your specific setup
    ${PYSIDE6_LIB_DIR}/shiboken6.dll  # Include shiboken if necessary
)

# Add your Python source files here (e.g., main.py)
set(APP_PY "${CMAKE_SOURCE_DIR}/python/app.py")

# Debugging output for paths
message(STATUS "VENV_PATH: ${VENV_PATH}")
message(STATUS "PYTHON_EXECUTABLE: ${PYTHON_EXECUTABLE}")
message(STATUS "App Path: ${APP_PY}")

# PyInstaller target to create a standalone .exe
set(PYINSTALLER_EXECUTABLE "${VENV_PATH}/Scripts/pyinstaller")  # Use "bin/pyinstaller" on Linux/Mac

add_custom_target(package_exe ALL
    COMMAND ${PYINSTALLER_EXECUTABLE} --onefile --name OpenDraft --distpath ${CMAKE_BINARY_DIR}/bin ${APP_PY}
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    COMMENT "Packaging application into a standalone executable in the 'bin' directory"
    DEPENDS ${VENV_PATH}  # Ensure venv is created first
)

# Optionally, if you want to run the executable after packaging, you could create a separate target.
add_custom_target(run_exe
    COMMAND ${CMAKE_BINARY_DIR}/bin/OpenDraft.exe
    DEPENDS package_exe
)
