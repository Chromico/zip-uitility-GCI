logo = """
 ______ _ ____       _   _ _____ ___ _     ___ _____ _   __
|__  /_ _|  _ \     | | | |_   _|_ _| |   |_ _|_   _\ \ / /
  / / | || |_) |____| | | | | |  | || |    | |  | |  \ V / 
 / /_ | ||  __/_____| |_| | | |  | || |___ | |  | |   | |  
/____|___|_|         \___/  |_| |___|_____|___| |_|   |_|  
"""

print(logo)
print("Version 1.0 \n")
print("This tool should not be used for any malicious purposes. Use this tool at your own risk.")


import zipfile


#Input info needed for cracking the ZIP file

zi = input("Enter Zip file location: \n")
password_list = input("Enter location of password list (.txt format) : \n")
x = input("Enter the location you want the zip file contents to be: \n")

import zipfile


count = 1

#open list as read bytes(rb)
with open(password_list,'rb') as text:
    for entry in text.readlines():  #read the contents
        password = entry.strip() #Seperate the lines
        try:      #this part runs in a loop until the contents of the text file have been used up
            with zipfile.ZipFile(zi,'r') as zf:
                zf.extractall(x, pwd=password) 

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~ %s\n ~%s\n ******************************''' 
                    % (password.decode('utf8'), data))  #specify that the data is utf8
                print("Size in Bytes:", data_size)    
                break

        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1 #keeps counting the number of tries until the password is cracked
   

        else:
            print("End of script")    
pass
      












