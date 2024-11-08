from setuptools import setup, find_packages

setup(
    name="FractalImageGenerator",
    version="0.1",
    description="Fractal Image Generator",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers, Education',
    ],
    author="radifmin",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/radifmin/FractalImageGenerator",
    python_requires='>=3.9',
)