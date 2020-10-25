# Copyright 2020 Xiaoyue Chen
#
# This file is part of "Useful Pre-commit Hooks" at
#
#     https://github.com/xiaoyuechen/useful-pre-commit-hooks.git
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    classifiers=[
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
