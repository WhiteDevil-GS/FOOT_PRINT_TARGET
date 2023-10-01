RED="\e[31m"
ORANGE="\e[33m"
BLUE="\e[94m"
GREEN="\e[92m"
STOP="\e[0m"
RED="$(printf '\033[31m')"  GREEN="$(printf '\033[32m')"  ORANGE="$(printf '\033[33m')"  BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  CYAN="$(printf '\033[36m')"  WHITE="$(printf '\033[37m')" BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"  GREENBG="$(printf '\033[42m')"  ORANGEBG="$(printf '\033[43m')"  BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"  CYANBG="$(printf '\033[46m')"  WHITEBG="$(printf '\033[47m')" BLACKBG="$(printf '\033[40m')"
RESETBG="$(printf '\e[0m\n')"
printf "${GREEN}"
printf "=================================\n"
printf "${ORANGE}"
figlet -w 200 -f standard "WHITE          DEVIL"
printf "${BLUE}"
figlet -w 200 -f  big ".                 ..    GS    ..              ."
printf "${GREEN}"
printf "=================================\n"
printf "${STOP}"
echo "  "

echo "${RED}[${WHITE}01${RED}]${ORANGE}- Foot Printing Target"
echo "${RED}[${WHITE}02${RED}]${ORANGE}- Discover IPS IN RANGE "
read ch
sleep 0.5
echo "${RED}[${WHITE}+${RED}]${ORANGE}-- Loading The INFO....."
clear
printf "${GREEN}"
printf "=================================\n"
printf "${ORANGE}"
figlet -w 200 -f standard "WHITE          DEVIL"
printf "${BLUE}"
figlet -w 200 -f  big ".                 ..    GS    ..              ."
printf "${GREEN}"
printf "=================================\n"
printf "${STOP}"

if [ $ch = 1 ]; then
    echo "${RED}[${WHITE}*${RED}]${ORANGE}- IP OF TARGET"
    read ip
    sudo nmap $ip -sC -sV -O

elif [ $ch = 2 ]; then
    sudo netdiscover

elif [ $ch = 99 ]; then
    echo "Thank You!!" 
else
    echo "inavlid choice!!!!!"
    sleep 1
fi
