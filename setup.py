import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Xpaper",
    version="0.0.0",
    author="Ekene Izukanne",
    author_email="ekeneizukanne@gmail.com",
    description="Cross platform library for managing desktop wallpaper",
    license = "MIT",
    keyword = "wallpaper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spatocode/Xpaper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)