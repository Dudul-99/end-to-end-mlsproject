from setuptools import find_packages, setup
from typing import List

hyphen_dot='-e .'

def get_requirements(path: str)->List[str]:
    '''
    Fonction reading the packages in the requirements.txt file wich are necessary for the project
    '''
    requirements= []
    with open(path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphen_dot in requirements:
            requirements.remove(hyphen_dot)
    return requirements


setup(
name="end_to_end_project",
version="0.0.1",
author="Abdul BOURA",
author_email="abdul.bouraa@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),
)