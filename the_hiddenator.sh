#!/bin/bash
#Funcao de ajuda ao utilizador, que indica o respetivo funcionamento do script
helpFunction()
{
	echo ""
	echo "To encrypt"
	echo "Usage: $0 -e path_to_file_to_encrypt new_file"
	echo ""
	echo "To decode"
	echo "Usage : $0 -d file_to_decode"
	echo ""
	echo "To get help"
	echo "Usage : -?"
}
#Recebe os argumentos do utilizador e verifica que caso corresponde
case "$1" in 
	-e)
	if [ -z $4 ] && [ -n "$2" ] && [ -n "$3" ]
	then 
		python3 Encrypt.py "$2" "$3"
	else
		helpFunction
	fi
	;;
	-d)
	if [ -z $3 ] && [ -n "$2" ]
	then
		python3 Decode.py "$2"
	else
		helpFunction
	fi
	;;
	-?)
	helpFunction
	exit 0
	;;
	*)
	helpFunction
	exit 1
	;;
esac
