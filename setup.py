from setuptools import setup, find_packages

setup(
    name="discord.py-self",
    version="2.0.1.1",
    author="Epic",
    description="A patched version of discord.py-self with custom fixes",
    long_description="A selfbot-safe version of discord.py including a fix for the build number issue.",
    long_description_content_type="text/markdown",
    url="https://github.com/NOTEPICY/discord.py-self",
    packages=find_packages(include=["discord*", "discord_protos*"]),
    include_package_data=True,
    install_requires=[
        "aiohttp",
        "requests",
        "websockets",
        "protobuf>=4.25.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)