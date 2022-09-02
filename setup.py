from setuptools import setup,find_packages
from typing import List

#Declerinng variables for setup functios
PROJECT_NAME="housing predictor"
VERSION="0.0.3"
AUTHOR="Anna Sargsyan"
DESCRIPTION="This is my first Machine Learning project"

REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    #Description:This functio is goinng to return list of requirement
    # metion in requiremets.txt file
    #Return this fuction is going to return a list which
    #  contain name of liberaries metio in req.txt file



    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()

)

