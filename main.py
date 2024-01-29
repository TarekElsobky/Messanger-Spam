from fbchat import Client
import fbchat
from termcolor import colored
from getpass import getpass

print(colored(f"This code created by \"{colored('Tarek Elsobky', 'magenta')}\""))
user = input(colored("Enter user name >> ", "yellow"))
password = getpass(colored("Enter password >> ", "yellow"))
client = Client(user, password)
name = input(colored("What is friend name >> ", "yellow"))
message = input(colored("What is the message >> ", "yellow"))
num = int(input(colored("how many messages you want to send >> ", "yellow")))
users = client.searchForUsers(name)
user = users[0]
for i in range(num):
    try:
        client.send(fbchat.models.Message(message), user.uid)
    except Exception:
        continue
print(colored("Done", "green"))
