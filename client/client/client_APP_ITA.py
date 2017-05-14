#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from socket import *      # Importo dei moduli necessari 

ctrl_cmd = ['Avanti', 'Indietro', 'Sinistra', 'Destra', 'Stop', 'CPU_temp', 'HOME', 'Distanza', 'x+', 'x-', 'y+', 'y-', 'xy_HOME']

top = Tk()   # Creo la finestra di top
top.title('Applicazione gestione #SuperCar')

HOST = '192.168.1.254'    # Server(Raspberry Pi) indirizzo IP
PORT = 21567
BUFSIZ = 1024             # dimensione buffer 
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Creiamo il socket
tcpCliSock.connect(ADDR)                    # Connessione al server

# =============================================================================
# The function is to send the command forward to the server, so as to make the 
# car move forward.
# =============================================================================
 
def funzione_avanti(event):
	print 'avanti'
	tcpCliSock.send('Avanti')

def funzione_indietro(event):
	print 'indietro'
	tcpCliSock.send('Indietro')

def funzione_sinistra(event):
	print 'sinistra'
	tcpCliSock.send('Sinistra')

def funzione_destra(event):
	print 'destra'
	tcpCliSock.send('Destra')

def funzione_stop(event):
	print 'stop'
	tcpCliSock.send('Stop')

def funzione_home(event):
	print 'home'
	tcpCliSock.send('Home')

def incrementa_x(event):
	print 'x+'
	tcpCliSock.send('x+')

def decrementa_x(event):
	print 'x-'
	tcpCliSock.send('x-')

def incrementa_y(event):
	print 'y+'
	tcpCliSock.send('y+')

def decrementa_y(event):
	print 'y-'
	tcpCliSock.send('y-')

def xy_home(event):
	print 'xy_home'
	tcpCliSock.send('xy_home')

# =============================================================================
# Exit the GUI program and close the network connection between the client 
# and server.
# =============================================================================
def funzione_quit(event):
	top.quit()
	tcpCliSock.send('stop')
	tcpCliSock.close()

# =============================================================================
# Create buttons
# =============================================================================
Btn0 = Button(top, width=5, text='Avanti',bg="green")
Btn1 = Button(top, width=5, text='Indietro',bg="green")
Btn2 = Button(top, width=5, text='Sinistra',bg="green")
Btn3 = Button(top, width=5, text='Destra',bg="green")
Btn4 = Button(top, width=5, text='Fine',bg="green")
Btn5 = Button(top, width=5, height=2, text='Home',bg="green")

# =============================================================================
# Buttons layout
# =============================================================================
Btn0.grid(row=0,column=1)
Btn1.grid(row=2,column=1)
Btn2.grid(row=1,column=0)
Btn3.grid(row=1,column=2)
Btn4.grid(row=3,column=2)
Btn5.grid(row=1,column=1)

# =============================================================================
# Bind the buttons with the corresponding callback function.
# =============================================================================
Btn0.bind('<ButtonPress-1>', funzione_avanti)  # When button0 is pressed down, call the function forward_fun().
Btn1.bind('<ButtonPress-1>', funzione_indietro)
Btn2.bind('<ButtonPress-1>', funzione_sinistra)
Btn3.bind('<ButtonPress-1>', funzione_destra)
Btn0.bind('<ButtonRelease-1>', funzione_stop)   # When button0 is released, call the function stop_fun().
Btn1.bind('<ButtonRelease-1>', funzione_stop)
Btn2.bind('<ButtonRelease-1>', funzione_stop)
Btn3.bind('<ButtonRelease-1>', funzione_stop)
Btn4.bind('<ButtonRelease-1>', funzione_quit)
Btn5.bind('<ButtonRelease-1>', funzione_home)

# =============================================================================
# Create buttons
# =============================================================================
Btn07 = Button(top, width=5, text='X+', bg='red')
Btn08 = Button(top, width=5, text='X-', bg='red')
Btn09 = Button(top, width=5, text='Y-', bg='red')
Btn10 = Button(top, width=5, text='Y+', bg='red')
Btn11 = Button(top, width=5, height=2, text='HOME', bg='red')

# =============================================================================
# Buttons layout
# =============================================================================
Btn07.grid(row=1,column=5)
Btn08.grid(row=1,column=3)
Btn09.grid(row=2,column=4)
Btn10.grid(row=0,column=4)
Btn11.grid(row=1,column=4)

# =============================================================================
# Bind button events
# =============================================================================
Btn07.bind('<ButtonPress-1>', incrementa_x)
Btn08.bind('<ButtonPress-1>', decrementa_x)
Btn09.bind('<ButtonPress-1>', decrementa_y)
Btn10.bind('<ButtonPress-1>', incrementa_y)
Btn11.bind('<ButtonPress-1>', xy_home)
#Btn07.bind('<ButtonRelease-1>', home_fun)
#Btn08.bind('<ButtonRelease-1>', home_fun)
#Btn09.bind('<ButtonRelease-1>', home_fun)
#Btn10.bind('<ButtonRelease-1>', home_fun)
#Btn11.bind('<ButtonRelease-1>', home_fun)

# =============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# control the car remotely with the keyboard.
# =============================================================================
top.bind('<KeyPress-a>', funzione_sinistra)   # Press down key 'A' on the keyboard and the car will turn left.
top.bind('<KeyPress-d>', funzione_destra) 
top.bind('<KeyPress-s>', funzione_indietro)
top.bind('<KeyPress-w>', funzione_avanti)
top.bind('<KeyPress-h>', funzione_home)
top.bind('<KeyRelease-a>', funzione_home) # Release key 'A' and the car will turn back.
top.bind('<KeyRelease-d>', funzione_home)
top.bind('<KeyRelease-s>', funzione_stop)
top.bind('<KeyRelease-w>', funzione_stop)


#top.bind('<KeyPress-c>'),xy_home)

spd = 50

def changeSpeed(ev=None):
	tmp = 'speed'
	global spd
	spd = speed.get()
	data = tmp + str(spd)  # Change the integers into strings and combine them with the string 'speed'. 
	print 'sendData = %s' % data
	tcpCliSock.send(data)  # Send the speed data to the server(Raspberry Pi)

label = Label(top, text='Speed:', fg='red')  # Create a label
label.grid(row=6, column=0)                  # Label layout

speed = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=changeSpeed)  # Create a scale
speed.set(50)
speed.grid(row=6, column=1)

def main():
	top.mainloop()

if __name__ == '__main__':
	main()
