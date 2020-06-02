
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print("ARG --->", arg)

# Print out the OS platform you're using:
print("PLATFORM --->", sys.platform)

# Print out the version of Python you're using:
print("VERSION --->", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("PROCESS ID --->", os.getpid())

# Print the current working directory (cwd):
print("CURRENT DIR --->", os.getcwd())

# Print out your machine's login name
print("MACHINE LOGIN NAME --->", os.getlogin())
