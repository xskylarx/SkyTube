__author__ = 'soporte'
# Let's start with some default (for me) imports...
import sys
import os
import PyQt4
from cx_Freeze import setup, Executable


# Process the includes, excludes and packages first
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\DHCP\\']

includes = []
excludes = []
packages = []
path = []
include_files = []

if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'linux' or sys.platform == 'linux2':
    base = None

skytube = Executable(
    # what to build
    script = "skytubec.py",
    initScript = None,
    base = 'Console',
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    icon = 'imagenes/logo.ico',
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "0.1",
    description = "SkyTube Descarga Videos de Youtube",
    author = "skylar",
    name = "SkyTubec",

    options = {"build_exe": {"includes": includes,
                 "excludes": excludes,
                 "packages": packages,
                 "path": path,
                 "include_files": include_files,

                 }
           },

    executables = [skytube]
    )
