from setuptools import setup, find_packages

setup(
    name="tool-cli",
    version="0.1.0",
    description="CLI para executar comandos Docker",
    author="Iris",
    py_modules=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cliris=src.cli:main",
        ],
    },
    python_requires=">=3.10",
    install_requires=[],
)

