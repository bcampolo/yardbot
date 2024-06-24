#!/bin/bash

echo "Uninstalling Yard Bot from build system..."
pip uninstall yardbot

echo "Building Yard Bot..."
python3 setup.py sdist bdist_wheel

