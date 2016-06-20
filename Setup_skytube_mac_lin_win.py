__author__ = 'jsandoval'
# Let's start with some default (for me) imports...
import sys
from cx_Freeze import setup, Executable


build_exe_options = {
"include_msvcr": True   #skip error msvcr100.dll missing
}
# Process the includes, excludes and packages first
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\DHCP\\']

includes = ["inicio","os","sys",'pafy',"PyQt5.QtCore","PyQt5.QtGui", "PyQt5.QtWidgets","PyQt5.QtNetwork","PyQt5.QtWebKit","PyQt5.QtPrintSupport", "atexit",
            "PyQt5.Qt","PyQt5.QtXmlPatterns"]
excludes = []
packages = []
path = []
include_files = ['imagenes']
include_msvcr = ['networkChanger.exe.manifest']

if sys.platform == 'win32':
    base = 'Win32GUI'
if sys.platform == 'linux' or sys.platform == 'linux2':
    base = None

skytube = Executable(
    # what to build
    script = "skytube.py",
    initScript = None,
    base = base,
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    icon = 'imagenes/logo.ico',
    #shortcutName="DHCP",
    #shortcutDir="ProgramMenuFolder"
    )

setup(

    version = "4.0",
    description = "SkyTube Descarga Videos de Youtube",
    author = "skylar",
    name = "SkyTube",

    options = {"build_exe": {"includes": includes,
                 "excludes": excludes,
                 "packages": packages,
                 "path": path,
                 "include_files": include_files,
                 "include_msvcr": include_msvcr,

                 }
           },

    executables = [skytube]
    )
