import hashlib
from colorama import Fore,Style
def kindHash():
      word = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Write : ")
      word1 = len(word)
      list = [("md5",32),("sha1",40),("sha256",64),("sha512",128)]
      for name,lon in list:
            if word1 == lon:
                  print("\n"+Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+name+"\n")    
def crackHashSalt() : 
      word = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Write : ")
      list = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Enter path of list : ")
      salt = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Enter Salt : ")
      salt1 = salt.encode()
      word1 = len(word)
      with open(list,"r") as file:
             for list1 in file:
                   en = list1.encode()
                   list2 = [(salt1+en,"left"),(en+salt1,"right"),(salt1+en+salt1,"middle")]
                   for func,name3 in list2 : 
                        if word1==32 :
                              ls = hashlib.md5(func).hexdigest()
                              name = "md5"
                        elif word1 == 40:
                              ls = hashlib.sha1(func).hexdigest()
                              name = "sha1"
                        elif word1 == 64:
                              ls = hashlib.sha256(func).hexdigest()
                              name = "sha256"
                        elif word1 == 128:
                              ls = hashlib.sha512(func).hexdigest()
                              name = "sha512"
                        else:
                              print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Invalid Input")    
                        if ls == word:
                              print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+list1+ " "+ name+" "+name3) 
def hashingSalt():
       word = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Write : ")
       salt = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Enter salt : ")
       salt1 = salt.encode()
       saif = word.encode()
       list2 = [(salt1+saif,"left"),(saif+salt1,"right"),(salt1+saif+salt1,"middle")]
       for salt3,name1 in list2 : 
            omar = [(hashlib.md5(salt3),"md5"),(hashlib.sha1(salt3),"sha1"),(hashlib.sha256(salt3),"sha256"),(hashlib.sha512(salt3),"sha512")]
            print("\n"+Fore.RED+"[+] "+Style.BRIGHT+Style.RESET_ALL+name1+" salt"+"\n")
            for func,name in omar:
                  ahmad = func.hexdigest()
                  print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+name+" "+Fore.BLUE+ahmad+Style.BRIGHT+Style.RESET_ALL+" "+Fore.RED+name1+Style.BRIGHT+Style.RESET_ALL)       
                     
def crackHash():
       word = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Write : ")
       list = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Enter path of list : ")
       word1 = len(word)
       with open(list,"r") as file:
             for list1 in file:
                   en = list1.encode()
                   if word1==32 :
                         ls = hashlib.md5(en).hexdigest()
                         name = "md5"
                   elif word1 == 40:
                         ls = hashlib.sha1(en).hexdigest()
                         name = "sha1"
                   elif word1 == 64:
                         ls = hashlib.sha256(en).hexdigest()
                         name = "sha256"
                   elif word1 == 128:
                         ls = hashlib.sha512(en).hexdigest()
                         name = "sha512"
                   else:
                         print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Invalid Input")    
                   if ls == word:
                         print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+list1+ " "+ name)
def hashing():
       word = input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+"Write : ")
       saif = word.encode()
       omar = [(hashlib.md5(saif),"md5"),(hashlib.sha1(saif),"sha1"),(hashlib.sha256(saif),"sha256"),(hashlib.sha512(saif),"sha512")]
       for func,name in omar:
              ahmad = func.hexdigest()
              print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+name+" "+Fore.BLUE+ahmad+Style.BRIGHT+Style.RESET_ALL)

def hash():
    print(Fore.BLUE+"1) "+Style.BRIGHT+Style.RESET_ALL + "Hash");print(Fore.BLUE+"2) "+Style.BRIGHT+Style.RESET_ALL + "Crack Hash");print(Fore.BLUE+"3) "+Style.BRIGHT+Style.RESET_ALL + "Hash With Salt");print(Fore.BLUE+"4) "+Style.BRIGHT+Style.RESET_ALL + "Crack Hash With Salt");print(Fore.BLUE+"5) "+Style.BRIGHT+Style.RESET_ALL + "Find kind of hash")
    choose = int(input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Enter number : "))
    match choose : 
           case 1 : hashing()
           case 2 : crackHash()
           case 3 : hashingSalt()
           case 4 : crackHashSalt()
           case 5 : kindHash()
           case  _: print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Invalid Input")

print(Fore.BLUE+"1) "+Style.BRIGHT+Style.RESET_ALL + "Hash");print(Fore.BLUE+"2) "+Style.BRIGHT+Style.RESET_ALL + "Exit")
choose = int(input(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Enter number : "))
while True:
        match choose:
                case 1 : hash() 
                case 2 : exit()
                case _: print(Fore.BLUE+"[+] "+Style.BRIGHT+Style.RESET_ALL+ "Invalid Input")