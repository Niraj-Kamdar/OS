# Boomslang OS
A simple UNIX like single core multitasking operating system simulator. Since the OS is built on Python, it has been given name of a snake species called boomslang.

## Installation
```console
pip install git+https://github.com/Niraj-Kamdar/OS.git#egg=boomslang_os
```
## Usage
The below command will start the kernel which will start a scheduler and a shell which can be used to perform basic operations like `cd`, `pwd`, etc.
```console
python -m boomslang_os.kernel
```
You can also run custom scripts like `echo_server` or `fib` which is given in the examples.

> Note: It isn't design to be used as an actual OS but rather help students understands concept of an OS by making it. 
