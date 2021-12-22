import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='my3d',
    version='0.0.0',
    packages=['my3d'],
    license='MIT',
    author='Zach Bateman',
    description='Three Dimensional Visualization and UI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zachbateman/my3d.git',
    download_url='https://github.com/zachbateman/my3d/archive/v_0.0.0.tar.gz',
    keywords=['VISUALIZATION', 'THREE', 'DIMENSION'],
    install_requires=[],
    include_package_data=True,
    classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   ]
)
