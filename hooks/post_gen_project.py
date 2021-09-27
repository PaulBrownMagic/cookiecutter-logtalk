#!/usr/bin/env python3
"""Run after generating the project"""
import os
from pathlib import Path
import shutil
import subprocess as sp
import sys

USE_GIT = "{{ cookiecutter.git }}" == "y"
COPY_SETTINGS = "{{ cookiecutter.settings }}" == "y"

LOGTALKUSER = ""
LOGTALKHOME = ""
if "LOGTALKUSER" in os.environ:
    LOGTALKUSER = os.environ["LOGTALKUSER"]
if "LOGTALKHOME" in os.environ:
    LOGTALKHOME = os.environ["LOGTALKHOME"]


def git_init() -> None:
    """Init Git"""
    if not USE_GIT:
        return
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", '"Logtalk Project Init"'],
    ]
    for command in commands:
        result = sp.run(command, check=False)
        if result.returncode != 0:
            print("Failed to initialize git")
            sys.exit(1)


def copy_settings() -> None:
    """Copy Settings"""
    if not COPY_SETTINGS:
        return
    logtalk_dir = LOGTALKUSER if LOGTALKUSER else LOGTALKHOME
    if not logtalk_dir:
        print("Couldn't find LOGTALKUSER or LOGTALKHOME for settings")
        return  # We don't exit here, so project still created
    settings = Path(LOGTALKUSER).joinpath("settings-sample.lgt")
    if not settings.exists():
        print("Couldn't find settings-sample.lgt")
        return  # We don't exit here, so project still created
    # Do the copy
    shutil.copyfile(settings, "settings.lgt")


if __name__ == "__main__":
    copy_settings()
    git_init()
