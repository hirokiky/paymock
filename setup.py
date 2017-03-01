from setuptools import setup


setup(
    name='paymock',
    version='0.1.0',
    url='https://github.com/hirokiky/paymock/',
    author='Hiroki KIYOHARA',
    description='Mock library for payjp',
    long_description=open('README.rst').read(),
    py_modules=['paymock'],
    install_requires=[
        "payjp==0.0.3",
        "responses==0.5.1",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development'
    ],
)
