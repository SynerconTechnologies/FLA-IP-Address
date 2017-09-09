import sys
import os

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["PyQt5.QtWidgets","PyQt5.QtCore","PyQt5.QtGui"],
                         "include_files": ["synerconlogo.ico"]}


target = Executable(
    script="EnterFLAip.py",
    base="Win32GUI",
    icon="synerconlogo.ico"
    )

setup(  name = "FLA IP Address Setting Utility",
        version = "1.0",
        description = "A small utility to set the IP address for the RP1210 functionality of the FLA",
        options = {"build_exe": build_exe_options},
        executables = [target])
