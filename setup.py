from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gh-autofollow",  # Replace with your package name
    version="0.1.0",  # Initial version
    author="Nnamdi Michael Okpala",  # Your name
    author_email="okpalan@protonmail.com",  # Your email
    description="A Python package to auto-follow and auto-unfollow GitHub users based on their activity",
    long_description=long_description,
    long_description_content_type="text/markdown",  # If you're using a Markdown README
    url="https://github.com/okpalan/autogithubfollow",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find all packages
    install_requires=[
        "requests",  # Add any dependencies your package needs
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Set your Python version requirement
    entry_points={
        'console_scripts': [
            'autogithubfollow=gh_autofollow.cli:main',  # Adjusted entry point
        ],
    },
)
