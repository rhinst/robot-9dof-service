from setuptools import setup
import platform


setup(
  name='robot-orientation-service',
  version='0.1',
  description='Robot Orientation service',
  url='https://github.com/rhinst/robot-orientation-service',
  author='Rob Hinst',
  author_email='rob@hinst.net',
  license='MIT',
  packages=['api'],
  data_files=[
    ('config', ['config/default.yaml']),
    ('config/dev', ['config/dev/env.yaml.dist']),
  ],
  install_requires = [
    'redis==3.5.3',
    'himl==0.7.0',
    'RPi.GPIO==0.7.0' if platform.platform().lower().find("armv7l") > -1 else 'Mock.GPIO==0.1.7',
    'smbus2==0.4.0'
  ],
  test_suite='tests',
  tests_require=['pytest==6.2.1'],
  entry_points={
    'console_scripts': ['orientation=orientation.__main__']
  }
)