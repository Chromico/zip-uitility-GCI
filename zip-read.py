
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

path = input("Enter the location of the Zip file you want to read: \n")


try:
   zf = zipfile.ZipFile(path, 'r') #path is the location of the file

   data = zf.namelist()[0]

   data_size = zf.getinfo(data).file_size

   print("Contents:",data)  #prints contents of the zip file
   print("Size in Bytes:", data_size) #prints the data size in bytes

   zf.close()
    
except FileNotFoundError:
    print("Error the file specified was not found :(")

except Exception:
    print("Ooops something went wrong")

else:
    print("Reading Zip file was Successful !!!")

finally:
    print("End of Script")            
