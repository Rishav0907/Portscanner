import socket
import subprocess
import sys
subprocess.call('clear',shell=True)
print("\n-----------------------------------------------------")
print("\n-               Hey I am Coderco                    -")
print("\n------------Welcome to my port scanner---------------")
print("\n-----------------------------------------------------")
print("Enter the host name:")
host_name=input(">")
ip=socket.gethostbyname(host_name)
print("Enter the protocol number:")
print("1) TCP")
print("2) UDP")
protocol=int(input(">"))

if(protocol==1):
    try:
        for i in range(1,5000):
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            check=soc.connect_ex((ip,i))
            if check==0:
                print("Host",host_name,"with port",i,"is open")
    except socket.gaierror:
        print("Host name cannot be resolved.")
        print("Try again")
        sys.exit()
    except KeyboardInterrupt:
        print("pressed Ctrl+c")
        sys.exit()

elif(protocol==2):
        try:
            for i in range(1,5000):
                soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                check=soc.connect_ex((ip,i))
                if check==0:
                    print("Host",host_name,"with port",i,"is open")
        except socket.gaierror:
            print("Host name cannot be resolved.")
            print("Try again")
            sys.exit()
        except KeyboardInterrupt:
            print("pressed Ctrl+c")
            sys.exit()

