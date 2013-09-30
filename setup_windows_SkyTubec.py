__author__ = 'soporte'
# Let's start with some default (for me) imports...
import sys
from cx_Freeze import setup, Executable


# Process the includes, excludes and packages first
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\DHCP\\']

includes = ['os','pafy','sys']
excludes = []
packages = []
path = []
include_files = []

skytube = Executable(
    # what to build
    script = "skytubec.py",
    initScript = None,
    base = 'Console',
    targetName = "skytubec.exe",
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    #icon = '',
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
