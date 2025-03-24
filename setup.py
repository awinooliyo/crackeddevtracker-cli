from setuptools import setup, find_packages

setup(
    name="cracktracker",
    version="1.0.0",
    description="Terminal-based productivity tracker for cracked devs",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "rich",
        "cryptography",
        "openai",
        "textual",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "crack=cracktracker.main:app",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
