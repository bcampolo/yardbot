from setuptools import find_packages, setup

setup(
    name="yardbot",
    version="1.0",
    author="Bruno Campolo",
    author_email="bjcampolo@gmail.com",
    description="Yard Bot",
    packages=["yardbot"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "yardbot = yardbot.yardbot:main",
        ],
    },
)
