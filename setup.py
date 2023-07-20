from setuptools import setup, find_packages

setup(
    name="upscaler",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv>=1.0",
    ],
    entry_points={
        "console_scripts": [
            # If your project has command-line scripts, add their entry points here, e.g.
            # "my_script=my_package.my_module:main",
        ],
    },
    python_requires=">=3.6",
    author="Ceren Sare Kilicarslan",
    author_email="cerensare.06@gmail.com",
    description="Increase the resolution of your images, with a simple-to-use function in the OpenCV library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)