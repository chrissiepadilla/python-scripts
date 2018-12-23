# passwordcrack

passwordcrack.py

This script: 
- codes a password crack by taking each password that we have and comparing it to the hash that we get.
- imports md5 library
- set up a counter to know how many passwords we are going through
- raw input for the MD5 password we are looking for
- raw input for directory location of our password file (which is a dictionary attack list of passwords you have saved in the file)
- do some error checking opening file
- create our loop to take action with each password in file
- increment our counter
- next compare the file md5 to the md5 that came in
- if match is found, print match and break out of loop
- if match is not found, print error Not found.

Thanks -- @chrissiepadilla