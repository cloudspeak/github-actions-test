from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="github_actions_test",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudspeak/github-actions-test",
    packages=find_packages(exclude=("example")),
    python_requires=">=3.7",
    install_requires=["pulumi>=1.8.1", "pulumi-aws>=1.0.0",],
    test_requires=["pulumi>=1.8.1", "pulumi-aws>=1.0.0",],
    test_suite="test",
)
