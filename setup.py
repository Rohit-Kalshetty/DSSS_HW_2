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
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    url='https://github.com/your-username/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
