import wave
import sys
from multiprocessing import Process, Queue
#Recebe o ficheiro de musica por argumento, e caso nao receba da print de informaçoes
while True:
	try:
		song = wave.open(sys.argv[1], mode='rb')
		break
	except FileNotFoundError:
		print("Parameteres missing")
		print("-? for help")
		sys.exit()
		break
# Converter o audio para Byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

def convert(frame_bytes,q):
	#Extrair o LSB de cada byte
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	# Converter o Bytearray para string
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	#Elimina os caracteres extras
	decoded = string.split("###")[0]
	q.put(decoded)
q = Queue()
p = Process(target=convert,args=(frame_bytes,q))
p.start()
p.join()
# Print o codigo extraido
print("Sucessfully decoded: "+q.get())
song.close()
