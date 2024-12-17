from setuptools import setup

setup(
    name='alpha_cluster_oxygen',
    version='0.1.0',
    description='A package to compute the hotspot structure of a tetrahedral alpha-clustered oxygen',
    url='https://github.com/shuds13/pyexample',
    author='Marek Matas',
    author_email='marek.matas@fjfi.cvut.cz',
    license='open source',
    packages=['alpha_cluster_oxygen'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)