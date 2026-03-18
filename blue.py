import hashlib
import time 
from colorama import Fore,Style
def crackingsalt():
    word = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter hash : ")
    salt = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter salt : ")
    hash123 = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Do you know your hash yes/no: ")
    if hash123 == "yes":
            word1 = int(input( Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
            wordlist  = input (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter path wordlist : ")
            start = time.time()
            counter = 0
            with open (wordlist , "r") as file : 
                for list in file :
                    counter = counter+1
                    word321 = list.strip()
                    byteword = (salt+word321).encode()  
                    byteword1 = (word321+salt).encode() 
                    byteword2 = (salt+word321+salt).encode()
                    if word1 == 1 : 
                        byte321 = hashlib.md5(byteword).hexdigest()
                        byte32 =  hashlib.md5(byteword1).hexdigest()
                        byte3 = hashlib.md5(byteword2).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter," :",word321) 
                        if byte321 == word or byte32 == word or byte3 == word:   
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 2:
                        byte321 = hashlib.sha256(byteword).hexdigest()
                        byte32 =  hashlib.sha256(byteword1).hexdigest()
                        byte3 = hashlib.sha256(byteword2).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter," :",word321) 
                        if byte321 == word or byte32 == word or byte3 == word:   
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 3:
                        byte321 = hashlib.sha512(byteword).hexdigest()
                        byte32 =  hashlib.sha512(byteword1).hexdigest()
                        byte3 = hashlib.sha512(byteword2).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter," :",word321) 
                        if byte321 == word or byte32 == word or byte3 == word:   
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 4:
                        byte321 = hashlib.sha1(byteword).hexdigest()
                        byte32 =  hashlib.sha1(byteword1).hexdigest()
                        byte3 = hashlib.sha1(byteword2).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter," :",word321) 
                        if byte321 == word or byte32 == word or byte3 == word:   
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    else : 
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Invalid input")
                end = time.time()
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+f" Time: {end - start:.6f} seconds")
    elif hash123 == "no" : 
            length = len(word)
            if length == 32 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This md5 hash")
            elif length == 40 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha1 hash")
            elif length == 64 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha256")
            elif length == 128 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha512")

def salt():
    word = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter word : ")
    salt = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter salt : ")
    choose1 = int(input(Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
    if choose1 == 1 :
            a = (salt+word+Fore.BLUE+Style.BRIGHT+"salt + word"+Style.RESET_ALL).encode()
            saif1 = hashlib.md5(a).hexdigest()
            b = (word+salt).encode()
            saif12 = hashlib.md5(b).hexdigest()
            c = (salt+word+salt).encode()
            saif123 = hashlib.md5(c).hexdigest()
            print(saif1+Fore.BLUE+Style.BRIGHT+" salt + word"+Style.RESET_ALL);print(saif12+Fore.BLUE+Style.BRIGHT+" word + salt "+Style.RESET_ALL);print(saif123+Fore.BLUE+Style.BRIGHT+" salt + word + salt"+Style.RESET_ALL)
    elif choose1 == 2 :
            a = (salt+word).encode()
            saif1 = hashlib.sha256(a).hexdigest()
            b = (word+salt).encode()
            saif12 = hashlib.sha256(b).hexdigest()
            c = (salt+word+salt).encode()
            saif123 = hashlib.sha256(c).hexdigest()
            print(saif1+Fore.BLUE+Style.BRIGHT+" salt + word"+Style.RESET_ALL);print(saif12+Fore.BLUE+Style.BRIGHT+" word + salt"+Style.RESET_ALL);print(saif123+Fore.BLUE+Style.BRIGHT+" salt + word + salt"+Style.RESET_ALL)
    elif choose1 == 3 :
            a = (salt+word).encode()
            saif1 = hashlib.sha512(a).hexdigest()
            b = (word+salt).encode()
            saif12 = hashlib.sha512(b).hexdigest()
            c = (salt+word+salt).encode()
            saif123 = hashlib.sha512(c).hexdigest()
            print(saif1+Fore.BLUE+Style.BRIGHT+" salt + word"+Style.RESET_ALL);print(saif12+Fore.BLUE+Style.BRIGHT+" word + salt"+Style.RESET_ALL);print(saif123+Fore.BLUE+Style.BRIGHT+" salt + word + salt"+Style.RESET_ALL)
    elif choose1 == 4 :
            a = (salt+word).encode()
            saif1 = hashlib.sha1(a).hexdigest()
            b = (word+salt).encode()
            saif12 = hashlib.sha1(b).hexdigest()
            c = (salt+word+salt).encode()
            saif123 = hashlib.sha1(c).hexdigest()
            print(saif1+Fore.BLUE+Style.BRIGHT+" salt + word"+Style.RESET_ALL);print(saif12+Fore.BLUE+Style.BRIGHT+" word + salt"+Style.RESET_ALL);print(saif123+Fore.BLUE+Style.BRIGHT+" salt + word + salt"+Style.RESET_ALL)
    else : 
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Invalid input")
def hashing():
    word = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter word : ")
    choose1 = int(input(Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
    if choose1 == 1 :
            b = word.encode()
            saif123 = hashlib.md5(b).hexdigest()
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+saif123)
    elif choose1 == 2 :
            b = word.encode()
            saif123 = hashlib.sha256(b).hexdigest()
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+saif123)
    elif choose1 == 3 :
            b = word.encode()
            saif123 = hashlib.sha512(b).hexdigest()
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+saif123) 
    elif choose1 == 4 :
            b = word.encode()
            saif123 = hashlib.sha1(b).hexdigest()
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+saif123)  
    else : 
            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Invalid input")
def craking():
    word = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter hash : ")
    hash123 = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Do you know your hash yes/no: ")
    counter = 0
    if hash123 == "yes":
            word1 = int(input( Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
            wordlist  = input (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter path wordlist : ")
            start = time.time()
            with open (wordlist , "r") as file : 
                for list in file :
                    counter = counter + 1
                    word321 = list.strip()
                    byteword = word321.encode()  
                    if word1 == 1 : 
                        byte321 = hashlib.md5(byteword).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter,": "+word321)
                        if byte321 == word :    
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 2:
                        byte321 = hashlib.sha256(byteword).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter,": "+word321)
                        if byte321 == word :    
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 3:
                        byte321 = hashlib.sha512(byteword).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter,": "+word321)
                        if byte321 == word :    
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    elif word1 == 4:
                        byte321 = hashlib.sha1(byteword).hexdigest()
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Trying",counter,": "+word321)
                        if byte321 == word :    
                            print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This is hash : "+word321)
                            break
                    else : 
                        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Invalid input")
                        break
                end = time.time()
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+f" Time: {end - start:.6f} seconds")
    elif hash123 == "no" : 
            length = len(word)
            if length == 32 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This md5 hash")
            elif length == 40 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha1 hash")
            elif length == 64 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha256")
            elif length == 128 : 
                print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" This sha512")
            else : 
                 print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"invalid input")

def hash():
    print(Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" Hashing")
    print(Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" craking hashing")
    print(Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" hashing with salt")
    print(Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" cracking hashing with salt")
    choose  = int(input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter number : "))
    if choose == 1 : 
        hashing()
    elif choose == 2 : 
        craking()
    elif choose == 3 :
        salt()
    elif choose == 4 : 
        crackingsalt()
    else :
        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"invalid input")
def hashfile():
    word = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter path file : ")
    choose = int(input( Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
    if choose == 1 : 
         h  = hashlib.md5()
         x = "md5"
    elif choose == 2 : 
         h = hashlib.sha256()
         x = "sha256"
    elif choose == 3 : 
         h = hashlib.sha512()
         x = "sha512"
    elif choose == 4 : 
         h = hashlib.sha1()
         x = "sha1"
    with open (word, "rb")as file:
        while chunk := file.read(4096):
                h.update(chunk)
        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"this is hash", h.hexdigest())
    choose1 = input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" do you want save hash : ").lower()
    if choose1 == "yes" : 
        with open ("hash.txt","a")as file:
              file.write(word + " : "+h.hexdigest()+" this hash : "+x+" \n" )
        print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" hash save")
    else:
         print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" OK : ")

def integrity():
    word = input (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter hash"+Fore.BLUE+Style.BRIGHT+" 1"+Style.RESET_ALL+" : ")
    word1 = input (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter hash"+Fore.BLUE+Style.BRIGHT+" 2"+Style.RESET_ALL+" : ")
    choose = int(input( Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" md5 \n"+Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" sha256\n"+Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" sha512\n"+Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+" sha1\n"+Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+"choose : "))
    if word == word1 : 
         print (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Matching Hashes")
    else : 
         print (Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Mismatched Hashes")
while True:
    print(Fore.BLUE+Style.BRIGHT+"1)"+Style.RESET_ALL+" hash : md5,sha1,sha256,sha512")
    print(Fore.BLUE+Style.BRIGHT+"2)"+Style.RESET_ALL+" hashing file")
    print(Fore.BLUE+Style.BRIGHT+"3)"+Style.RESET_ALL+" File Integrity Checker")
    print(Fore.BLUE+Style.BRIGHT+"4)"+Style.RESET_ALL+ " Exit")
    choose = int(input(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Enter number : "))
    match choose :
        case 1 : hash()
        case 2 : hashfile()
        case 3 : integrity()
        case 4 : break
        case _:print(Fore.BLUE+Style.BRIGHT+"[+]"+Style.RESET_ALL+" Invalid input")