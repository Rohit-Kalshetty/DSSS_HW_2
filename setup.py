from setuptools import setup, find_packages
setup(
    name='Python_sample',
    version='0.1',
    packages=find_packages(),
    py_modules=['math_quiz'],
    install_requires=[ ],
    entry_points={
        'console_scripts': [],
    },
    author='Rohit Kalshetty',
    author_email='rohit.kalshetty@fau.de',
    description='Data Science Survival Skills',
    url='https://github.com/Rohit-Kalshetty/DSSS_HW_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',],
)
