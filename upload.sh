
source ./secret/cs16.sh
# source ./secret/Dsci.sh


wxcloud login -a $ID -k $PW
wxcloud run:deploy
# wxcloud env:list
wxcloud logout