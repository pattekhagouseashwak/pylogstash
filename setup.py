from setuptools import setup, find_packages

setup(
    name='pylogstash',
    version='0.7',
    description='A Python library to transfer logs using python-logtash where user need to provide logstash ip and port',
    author='Ashwak',
    packages=find_packages(),
    install_requires=['logstash'],
    python_requires=">=3",
)