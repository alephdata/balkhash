from setuptools import setup, find_packages


setup(
    name='balkhash',
    version='0.1.0',
    description="Cloud storage library to store raw and structured data from "
                "different datasets in a data lake",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='storage',
    author='Journalism Development Network',
    author_email='data@occrp.org',
    url='http://github.com/alephdata/balkhash',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'google-cloud-storage>=1.10.0',
        'normality>=0.6.1'
    ],
    tests_require=[
    ],
    entry_points={}
)