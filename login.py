#!/usr/bin/env python
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#transport = ssh.get_transport()
ssh.connect(hostname='10.8.6.144', username='pdcadmin', password='JkeioNy6Ghwe$W@')
print "login OK!!"
stdin, stdout, stderr = ssh.exec_command("ls -a")
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        #rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        #if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),
#command = "ls -a"
#ssh.exec_command(command)
#print stdout
ssh.close()
