from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns the list of requirements
    from the requirements.txt file.
    """
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirements_lst

# Do NOT call print(get_requirements()) here in production setup.py

# Setup configuration
setup(
    name="Networksecurity",  # Typo fixed in name
    version="0.0.1",
    author="Ankit Kumar",
    author_email="ank838281@gmail.com",
    packages=find_packages(include=["networksecurity", "networksecurity.*"]),
    install_requires=get_requirements()
)