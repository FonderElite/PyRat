 #!/bin/bash
 export PS1="\e[0;31m[\u@\h \W]\$ \e[m "
 if [ "$EUID" -ne 0 ] then 
 export PS1="\e[0;31m[\u@\h \W]\$ \e[m" 
  echo 'You Need Root Privellages to execute this bash command'
  exit
else
 sudo apt-get update
 sudo apt install python3
 sudo apt install 
fi
 
 
 
