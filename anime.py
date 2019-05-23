import os
import time
import random
import quote 

#jeda waktu dalam satuan detik
jedaWaktu = 30

#jeda waktu dalam satuan detik
def jeda():
	time.sleep(jedaWaktu)


#untuk membersikan terminal/console
def clear():
	os.system('clear')


#menampilkan quote
def tampilkan():

	#menentukan jumlah index
	max = (len(quote.quote) - 1)

	#menentukan random index
	randomIndex = random.randint(0,max)


	clear()
	print(quote.quote[randomIndex][0])
	jeda()
	clear()


while True:

	tampilkan()



