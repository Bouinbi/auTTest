"""
Lab setup 

"""
from setuptools import setup

setup(
    name="auTTest",
    version="1.0.0",
    description="Automated Pentest",
    packages=['auTTest'],
    
    install_requires=[
        "click",
        "questionary",
        "argparse"
    		],
    
    entry_points={
        'console_scripts': ['auTTest=auTTest.__main__:main']
                },

)

