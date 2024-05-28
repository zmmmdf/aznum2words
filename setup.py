from setuptools import setup, find_packages

setup(
    name='aznum2words',
    version='0.1',
    packages=find_packages(),
    author='Ziya Mammadov',
    author_email='ziyamm08@gmail.com',
    description='Python library for converting numbers to Azerbaijani words',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ziyam/aznum2words',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[],
)
