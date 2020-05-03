from setuptools import setup
setup(
  name = 'pybleno',
  packages = ['pybleno', 'pybleno/hci_socket',  'pybleno/hci_socket/BluetoothHCI'], # this must be the same as the name above
  version = '0.11.1',
  description = 'A direct port of the Bleno bluetooth LE peripheral role library to Python2/3',
  author = 'Adam Langley, Thomas Mirlacher, John Blance',
  author_email = '',
  url = 'https://github.com/jblance/pybleno', 
  download_url = 'https://github.com/jblance/pybleno', 
  keywords = ['Bluetooth', 'Bluetooth Smart', 'BLE', 'Bluetooth Low Energy'], # arbitrary keywords
  install_requires = [
      'numpy',
      'pycryptodome'
  ],
  classifiers=[
      'Programming Language :: Python :: 2.7'
  ]
)
