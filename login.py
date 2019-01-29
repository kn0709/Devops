#!/usr/bin/env python
import paramiko
import os.path
import json
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip_file = open('ip.txt', 'r')
for host in ip_file:
        ssh.connect(hostname=host, username='pdcadmin', password='JkeioNy6Ghwe$W@')
        stdin, stdout, stderr = ssh.exec_command("free -om | gawk  '/Mem:/{print $3}'")
        while not stdout.channel.exit_status_ready() :#and hostname.channel.exit_status_ready()
                if stdout.channel.recv_ready():
                        mem_util=stdout.channel.recv(1024).rstrip()
        stdin, stdout, stderr = ssh.exec_command("free -m | gawk  '/cache:/{print $3}'")
        while not stdout.channel.exit_status_ready() :
                if stdout.channel.recv_ready():
                        cache_util=stdout.channel.recv(1024).rstrip()
        stdin, stdout, stderr = ssh.exec_command("sar -u | gawk  '/Average:/{print $8}'")
        while not stdout.channel.exit_status_ready() :#and hostname.channel.exit_status_ready()
                if stdout.channel.recv_ready():
                        cpu_idle=float(stdout.channel.recv(1024).rstrip())
        stdin, stdout, stderr = ssh.exec_command('hostname')
        while not stdout.channel.exit_status_ready():
                if stdout.channel.recv_ready():
                        hostname=stdout.channel.recv(1024).rstrip()
        entry="{\"CPU_IDLE\":\"%s\",\"CPU_UTILISED\":\"%.2f\",\"MEM_UTILISED\":\"%s\",\"CACHE_UTILISED\":\"%s\"}" %(cpu_idle,(100.00-cpu_idle),mem_util,cache_util)
        entry=json.dumps(entry)
        print entry
        open('%s.json' %hostname, 'a')
        ssh.close()
#this is a test for git
