from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_name: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    requirements = []
    with open(file=file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name="ML_Project",
    version="0.0.1",
    author="Shreyansh",
    author_email="paneyshreyansh46@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
