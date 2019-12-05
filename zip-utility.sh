#!/bin/bash
clear
figlet ZIP-UTILITY
echo "Version 1.0"
echo "Press Enter to continue or Press CTRL-C to exit"
read al
echo 'Installing Requirements....'
echo .
echo .
apt install python3
apt install python3-pip
echo Requirements Installed....
echo Press Enter To Continue...
read upd
clear
figlet ZIP-UTILITY
echo "Version 1.0"
echo -e "\e[4;31m This tool should not be used for any malicious purposes. Use this tool at your own risk. \e[0m"
echo "Press 1 To  Read Zip file "
echo "Press 2 To  Extract Zip file "
echo "Press 3 To  Brute Force Password protected Zip file"
echo "Press 4 To  EXIT "
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
#rm *.xxx >/dev/null 2>&1
python3 zip-read.py
#rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
python3 zip-extract.py
exit 0
elif [ $ch -eq 3 ];then
clear
python3 zip-crack.py
exit 0
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;31m"
figlet ZIP-UTILITY
exit 0
fi
done
