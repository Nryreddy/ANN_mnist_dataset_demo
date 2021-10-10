from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="ANN_mnist_dataset_demo",
    version="0.0.1",
    author="Nryreddy",
    description="A small package for ANN implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nryreddy/ANN_mnist_dataset_demo",
    project_urls={
        "Bug Tracker": "https://github.com/Nryreddy/ANN_mnist_dataset_demo/issues",
    },
    
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]

)