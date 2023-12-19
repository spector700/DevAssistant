#!/usr/bin/env python

from setuptools import setup

setup(
    name="DevAssistant",
    version="0.1.0",
    entry_points={
        "console_scripts": [
            "DevAssistant = dev_assistant:main",
        ],
    },
)
