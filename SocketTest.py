import socket
print(socket.gethostname())
print(socket.gethostbyname("www.nexusonline.com"))

hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname_ex(hostname)
    print("Ipv4 adddress is "+str(ip_address[2][0]))
except:
    print('err')


try:
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    print("Ipv6 adddress is "+str(ip_address))
except:
    print('err')




