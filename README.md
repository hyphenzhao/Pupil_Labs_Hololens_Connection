# Pupil-Labs and Hololens Connection
## 0. Pre-requirements
  + [Pupil-labs source code](https://github.com/pupil-labs/pupil/tree/master) - please make sure it could run on you device, i.e. please install all the dependencies.
  + [Script from this repo](https://github.com/hyphenzhao/Pupil_Labs_Hololens_Connection/archive/master.zip) - put it under ./pupil_src/shared_modules.
  + [Python 3](https://www.python.org/downloads/)
## 1. How to run it?
  0. Make sure you have all dependencies installed
  1. Use python to run script under pupil_src:
  ```command line
  $ python3 main.py service
  ```
  2. Use python to run script under pupil_src/shared_module:
  ```command line
  $ python3 hololens_server.py
  ```
  3. Get the IP address of your host computer, copy it into your Hololens Apps. Make sure Hololens and your host computer are in the same network.
  4. Now you could start your tracking functions in the Hololens App
  + Notice that if you are using Windows system, you probably have to specify the network interface by changing the *TCP_IP* parameter in the *hololens_server.py* 


