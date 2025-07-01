# VideoProcessingFramework  
Original repository - https://github.com/NVIDIA/VideoProcessingFramework  

## Problem  
VideoProcessingFramework is compiled with latest version of torch and doesn't work with previous versions.  
For this to be possible it's necessary to bound or set properly the version of torch in setup.py and pyproject.toml files with setup_torch_version.py  