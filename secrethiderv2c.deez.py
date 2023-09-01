import time
# import encryption shit
from cryptography.fernet import Fernet
# key generation
key = Fernet.generate_key()
 
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)

#input for old vs new secrets, and then some file read stuff to read secrets and password
oldsecret=input('do you want to view an old secret?y/n ')
#absurdly spaghettified delete confirm system
if oldsecret=='y':
    delsecret=input('would you like to delete the old secret(s)?y/n ')
    if delsecret=='y':
        delconfirm=input('are you sure?y/n ')
        if delconfirm=='y':
            dfile = open("secrets.txt", "w")
            dfile.close()
            print('deleted')
        else:
            print('cancelling')
        #opens file as a variable and strips to check password entered against the saved password
    else:
        try:
            guess = input('what is the previously said password? ')
                # opening the encrypted file
            with open('passwords.txt', 'rb') as enc_pw:
                encrypted = enc_pw.read()
 
            # decrypting the file
            decrypted = fernet.decrypt(encrypted)
             Signature did not match digest.
            with open('passwords.txt', 'wb') as dec_file:
                    dec_file.write(decrypted)

            with open("passwords.txt") as f:
                    filecontents=f.read()
                    filecontents=filecontents.strip()
            if guess == filecontents:
                print('correct, the secret(s) is ')
                with open('secrets.txt', 'rb') as enc_pw:
                    encrypted = enc_pw.read()
 
                    # decrypting the file
                decrypted = fernet.decrypt(encrypted)
            
                with open('secrets.txt', 'wb') as dec_file:
                    dec_file.write(decrypted)
                sfile = open("secrets.txt" , "r")
                print(sfile.read())
                sfile.close()

            else:
                print('you do not get to see the secrets')
        except FileNotFoundError:
            print('no password saved')

        #secret saving shit for new people
else:
    try:
        #writing secret to file
        secret=input('what secret do you want to protect? ' + '\n')
        secret= '\n' + secret
        sfile = open("secrets.txt", "a" )
        sfile.write(secret)
        sfile.close()
        #encrypting secret
        with open('secrets.txt', 'rb') as file:
            original = file.read()
        print('opened success')
        encryptedsecret = fernet.encrypt(original)
        with open('secrets.txt', 'wb') as encrypted_file:
            encrypted_file.write(encryptedsecret)
        print('encrypt success')
         #setting password
        print('alright, now set a password')
        print('what do you want your password to be?\(will overwrite previous passwords\)')
        password=input()
        pfile = open("passwords.txt", "w" )
        pfile.write(password)
        pfile.close()
        #password encryption
        with open('passwords.txt', 'rb') as file:
            originalpw = file.read()
        print('opened success')
        encryptedpw = fernet.encrypt(originalpw)
        with open('passwords.txt', 'wb') as encrypted_file:
            encrypted_file.write(encryptedpw)
        print('encrypt success')
        print('password set! now rerun the program to view secrets!')
    except:
        print('something went wrong')
