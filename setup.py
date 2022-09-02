from setuptools import setup
from typing import List

#Declerinng variables for setup functios
PROJECT_NAME="housig predictor"
VERSION="0.0.1"
AUTHOR="Anna Sargsyan"
DESCRIPTION="This is my first Machine Learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    #Description:This functio is goinng to return list of requirement
    # metion in requiremets.txt file
    #Return this fuction is going to return a list which
    #  contain name of liberaries metio in req.txt file



    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=["housing"],
    install_requires=get_requirements_list()

)

