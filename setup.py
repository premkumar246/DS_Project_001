from setuptools import find_packages,setup
from typing import List


HYPENEDOT = '-e.'
def get_requirements(file_path:str)->List[str]:

    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPENEDOT in requirements:
            requirements.remove(HYPENEDOT)
    
    return requirements

    


setup(
    name = 'DS_Project_001',
    version = '0.0.1',
    author = 'Prem Kumar',
    author_email = 'sanamalapremkumar@gmail.com',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')

)