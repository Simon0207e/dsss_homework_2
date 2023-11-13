from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1.0',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'setuptools==68.2.2',
        'wheel==0.41.3',
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz.module:main_function',
        ],
    },
    author='Ximeng Zhang',
    author_email='zximeng0203@gmail.com',
    description=' math quiz',
    long_description='',
    url='https://github.com/Simon0207e/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    use_scm_version=True,
)
