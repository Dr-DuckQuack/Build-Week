import socket, requests

#port scanner

target="192.168.50.101"
portrange= input("Enter the port range to scan (es 5-1000): ")

lowport= int(portrange.split('-')[0])
highport= int(portrange.split('-')[1])
print('scanning host', target, 'from port', lowport, 'to port', highport)

for port in range(lowport, highport):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status= s.connect_ex((target, port))
    if (status==0):
        print('*** Port',port,'- OPEN ***')
    else:
        print('Port',port,'- CLOSED')
        s.close()
        

#http method

target="http://192.168.50.101/"
   
try:
    connection= requests.options(target)
    print("I metodi HTTP abilitati sono: ", connection.headers.get("Allow"))

except Exception as e:
    print(f"errore riscontrato: {e}")
    
    
    
    