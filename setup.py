#!/usr/bin/env python3

from distutils.core import setup, Extension
import platform
import os

target_os = platform.system()
root = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(root, "src")
sources = []
for root, dirs, files in os.walk(src):
    for file in files:
        if file.endswith(".c"):
            sources.append(os.path.join(root, file))
includes = ["/usr/local/include",
            "/usr/local/include/freerdp2",
            "/usr/local/include/winpr2",
            "/usr/include/freerdp2",
            "/usr/include/winpr2",
            "/opt/homebrew/opt/freerdp/include/freerdp2",
            "/opt/homebrew/opt/freerdp/include/winpr2"]
libs = ["/usr/local/lib", "/usr/lib", "/usr/lib64/"]
modulel = Extension("pyrdping", sources=sources,
                    define_macros=[("TARGET_OS_WATCH", target_os),
                                   ("TARGET_OS_IPHONE", '0'), ],
                    libraries=['freerdp2'],
                    include_dirs=includes,
                    library_dirs=libs, )

setup(
    name="pyrdping",
    author="JumpServer",
    author_email="code@jumpserver.org",
    version="0.0.2",
    ext_modules=[modulel]
)
