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

path = input("Enter the location of the Zip file you want to extract: \n")
directory = input("Enter the location of where you want the contents of the Zip file to be extracted to: \n")

try:
   zip_ref = zipfile.ZipFile(path, 'r') #path is the location of the file

   zip_ref.extractall(directory)

   zip_ref.close()
    
except FileNotFoundError:
    print("Error the file specified was not found :(")

except Exception:
    print("Ooops something went wrong")

else:
    print("Extracting Zip file was Successful !!!")

finally:
    print("End of Script")            
