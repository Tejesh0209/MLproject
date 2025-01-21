from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from the file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]  # Fix the issue by stripping newlines
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Tejesh Boppana',
    author_email='tejesh.boppana@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
