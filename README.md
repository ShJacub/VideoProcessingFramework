# VideoProcessingFramework  
Original repository - https://github.com/NVIDIA/VideoProcessingFramework  

## Problem  
VideoProcessingFramework is compiled with latest version of torch and doesn't work with previous versions.  
For this to be possible it's necessary to bound or set properly the version of torch in setup.py and  
pyproject.toml files  

## Install  
-----
- Installation is made inside nvidia/cuda:12.4.1-devel-ubuntu22.04 docker container 
  - Ubuntu22.04  
  - cuda12.4.1
  - python3.10.12

#### torch==2.5.1
1. Replace  
  1.1. install_requires=["torch"] with install_requires=["torch<=2.5.1"] in src/PytorchNvCodec/setup.py  
  1.2. "torch" with "torch<=2.5.1" in src/PytorchNvCodec/pyproject.toml  
2. Make installation described in original repo  

#### torch==2.4.1  
1. Replace  
  1.1. install_requires=["torch"] with install_requires=["torch<=2.4.1"] in src/PytorchNvCodec/setup.py  
  1.2. "torch" with "torch<=2.4.1" in src/PytorchNvCodec/pyproject.toml  
2. Set CMAKE_POLICY_VERSION_MINIMUM=3.5  
  export CMAKE_POLICY_VERSION_MINIMUM=3.5  
3. Make installation described in original repo  

#### torch==2.3.1  
1. Replace  
  1.1. install_requires=["torch"] with install_requires=["torch<=2.3.1"] in src/PytorchNvCodec/setup.py  
  1.2. "torch" with "torch<=2.3.1" in src/PytorchNvCodec/pyproject.toml  
2. Set CMAKE_POLICY_VERSION_MINIMUM=3.5  
  export CMAKE_POLICY_VERSION_MINIMUM=3.5  
3. Make installation described in original repo  


- Installation is made inside nvidia/cuda:11.8.0-devel-ubuntu20.04 docker container 
  - Ubuntu20.04  
  - cuda11.8.0
  - python3.8.10

#### torch==2.2.2  
1. Replace  
  1.1. install_requires=["torch"] with install_requires=["torch<=2.2.2"] in src/PytorchNvCodec/setup.py  
  1.2. "torch" with "torch<=2.2.2" in src/PytorchNvCodec/pyproject.toml  
3. Make installation described in original repo  