import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pre-commit-hooks-xiaoyuechen", 
    version="0.0.1",
    author="Xiaoyue Chen",
    author_email="xiaoyue_chen@outlook.com",
    description="A collection of pre-commit hooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaoyuechen/pre-commit-hooks.git",
    packages=setuptools.find_packages(),
    install_requires = ["cpplint", "cmakelang"],
    classifiers=[
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)