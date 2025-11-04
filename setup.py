from setuptools import setup, find_packages

setup(
    name="tool-cli",
    version="0.1.0",
    description="CLI egoísta apenas para facilitar minha vida",
    author="Iris",
    py_modules=[],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "src": ["custom-files/*.zsh"],
    },
    entry_points={
        "console_scripts": [
            "lino-ci=src.cli:main",
        ],
    },
    python_requires=">=3.10",
    install_requires=[],
)
