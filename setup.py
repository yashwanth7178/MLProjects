from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''''
    this function will return the list of requirements
    '''
    get_requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLProjects',
    version='0.0.1',
    author='yashwanth7178',
    author_email='17b61a0208@nmre.edu.in',
    packages=find_packages(),
    install_reuires=get_requirements('requirements.txt')
)