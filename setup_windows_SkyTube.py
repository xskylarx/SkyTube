__author__ = 'soporte'
# Let's start with some default (for me) imports...
import sys
import os
import PyQt4
from cx_Freeze import setup, Executable


# Process the includes, excludes and packages first
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\DHCP\\']

includes = ["inicio","PyQt4.QtCore","PyQt4.QtGui","os","sys","PyQt4",'requests','pafy']
excludes = []
packages = []
path = []
include_files = ['imagenes']

skytube = Executable(
    # what to build
    script = "skytube.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "skytube.exe",
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = False,
    appendScriptToLibrary = False,
    icon = 'imagenes/logo.ico',
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "0.1",
    description = "SkyTube Descarga Videos de Youtube",
    author = "skylar",
    name = "SkyTube",

    options = {"build_exe": {"includes": includes,
                 "excludes": excludes,
                 "packages": packages,
                 "path": path,
                 "include_files": include_files,

                 }
           },

    executables = [skytube]
    )