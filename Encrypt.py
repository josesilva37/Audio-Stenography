import wave
import sys
from multiprocessing import Process, Queue

#Ler o ficheiro de audio .wav, se nao receber o ficheiro como argumento entao da print de algumas instruçoes
while True:
	try:
		musica = wave.open(sys.argv[1], mode = 'rb')
		break
	except FileNotFoundError:
		print("Parameteres missing")
		print("-? for help")
		sys.exit()
		break
		
		
# Ler os frames e converter para byte array
frame_bytes = bytearray(list(musica.readframes(musica.getnframes())))
#Mensagem secreta
mensagem = input("Intruduza uma mensagem para encriptar ")

def convert(mensagem,frame_bytes):
	#Acrescenta data para preencher o resto dos bytes
	mensagem = mensagem + int((len(frame_bytes)-(len(mensagem)*8*8))/8) *'#'
	#Converter o texto para uma array de bit
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in mensagem])))
	#Substituir o LSB de cada byte do audio por um bit do bit array
	q.put(bits)
q = Queue()
p = Process(target=convert,args=(mensagem,frame_bytes))
p.start()
bits =q.get()
p.join()

for i, bit in enumerate(bits):
	frame_bytes[i] = (frame_bytes[i] & 254) | bit
#A função bytes, assim como a funçção bytearray, converte objetos para objetos em bytes, que nao podem ser modificados
frame_modified = bytes(frame_bytes)
#Escrever os bits e criar o audio final.
with wave.open(sys.argv[2], 'wb') as fd:
	fd.setparams(musica.getparams())
	fd.writeframes(frame_modified)
musica.close()
