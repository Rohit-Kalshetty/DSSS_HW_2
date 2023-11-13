# Setup Git on your Windows Computer cuz Mac is Meh:

# For Windows:

# 1. Download Git:

# 	a. Visit the official Git website: https://git-scm.com/downloads
# 	b. The website will detect your operating system. Click on the Windows download link.

# 2. Run the Installer:

# 	a.Once the download is complete, run the installer
# 	b. You'll go through several installation steps. You can generally choose the default settings, but you might want to make sure that "Git Bash" is selected to install, as it provides a Unix-like command-line environment on Windows.

# 3. Adjust System PATH (if prompted):

# 	a. During the installation, there might be an option to "Adjusting your PATH environment" or "Use Git from the Windows Command Prompt." Choose this option to add Git to your PATH so that you can use Git from the command line.

# 4. Finish Installation:

# 	a. Complete the installation by following the on-screen instructions.

# 5. Verify Installation:

# 	a. Open a new command prompt window and type git --version. If Git has been installed successfully, it will display the installed version.

import os
import platform
import sys

import pkg_resources
from setuptools import find_packages, setup


def read_version(fname="whisper/version.py"):
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"))
    return locals()["__version__"]


requirements = []
if sys.platform.startswith("linux") and platform.machine() == "x86_64":
    requirements.append("triton>=2.0.0,<3")

setup(
    name="openai-whisper",
    py_modules=["whisper"],
    version="1.0",
    description="Robust Speech Recognition via Large-Scale Weak Supervision",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.8",
    author="OpenAI",
    url="https://github.com/openai/whisper",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements
    + [
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": ["whisper=whisper.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest", "scipy", "black", "flake8", "isort"]},
)
