from pwn import *

conn = remote('c1.lagncrash.com', 9006)
with open('Miscellaneous/Plumber/output.txt', 'a') as f:
    while True:
        output = str(conn.recvline())[2:-2]
        
        break
