from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any empty lines and comments starting with '#'.
    """
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='MLProject',
    version='0.1.0',
    author='Siddhesh513',
    author_email='siddheshsutar86@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
