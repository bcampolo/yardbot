# Import submodules to make them accessible when the package is imported
from .yardbot import *

# Define package-level variables
PACKAGE_NAME = "yardbot"
VERSION = "0.1"


# Define a function that can be accessed directly from the package namespace
def yardbot():
    print("Run Yard Bot")


# Perform any necessary initialization tasks
print(f"{PACKAGE_NAME} version {VERSION} initialized")
