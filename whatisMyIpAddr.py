import socket   
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
print("Your PC Name :" + hostname)   
print("Your Computer IP Address:" + IPAddr)   