import paramiko
import time

commands = ['_cmdline-mode on\n', 'Y\n', 'Jinhua1920unauthorized\n\n', 'dis cur | inc ip address\n', 'dis cur | inc vlan\n']

max_buffer = 65535
devices = {
   'monitoramento': {
      'ip': '192.168.23.56',
      'username': 'admin@system',
      'password': '12345678'
      #'port': '8181'
      }
   }

def get_connection(host, username, password):#, port):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(hostname=host,username=username, password=password, look_for_keys=False, allow_agent=False) #port=port, 
   return ssh

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


for device in devices.keys(): 
    connection = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'])#, port=devices[device]['port'])
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
   #new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)
    
    for id, command in enumerate(commands):
        #print(f"Executing command {command}")
        new_connection.send(command)
        time.sleep(2)
        output = new_connection.recv(max_buffer)
        if id == 3:
            print(output.split()[8], output.split()[9])
        if id == 4:
            print(output)
           

new_connection.close()
