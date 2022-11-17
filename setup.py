from setuptools import setup, find_packages

setup(
    name='address_extractor',
    author='Sahar Zal, Moein Salimi, Hossein Parto',
    version='1.12',
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        "pip>=21.3.1",
        "wheel==0.36.2",
        "testresources==2.0.1",
        "setuptools==54.1.1",
    ],
    packages=find_packages(),
    package_data={
        'address_extractor': [
                'src/*',
                'assets/*',
        ],
    }
    
)