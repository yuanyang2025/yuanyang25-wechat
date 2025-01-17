
source ./secret/cs16.sh
source ./env.sh

wxcloud login -a $ID -k $PW
wxcloud run:deploy
# wxcloud env:list
wxcloud logout