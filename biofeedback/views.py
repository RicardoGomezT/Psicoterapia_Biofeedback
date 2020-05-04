from django.shortcuts import render
import os
from django.http import JsonResponse
import _thread as thread
#from subprocess import run


#from .models import Question



def index(request):

    thread.start_new_thread(plotters, ())
    print("yes")

    context = {'1': 1}
    return render(request, 'bio/index.html', context)


def plotters():
    cmd = 'python3 Desktop/proyecto/D_Biofeedback/biofeedback/luz4.py'
    os.system(cmd)



def index_2(request):
    thread.start_new_thread(plotters, ())
    context = {'1': 1}
    return render(request, 'bio/index_2.html', context)   

#import serial
#ser = serial.Serial('/dev/ttyUSB0', 9600)
filne = "save.txt"
#ser = open(filne, 'r')

temp_ant = 0
def get_seriales(request):
    global temp_ant 
    try:
        ser = open(filne, 'r')
        temp = ser.readline()        
        try:            
            datas = temp.split(";")
            #print(datas)
        except ValueError as Ve:
            print(1)
            temp = 'none'
        
        ser.close()
        #os.remove(filne)
                    
    except AttributeError as Ae:
        print(2)
        temp = 'none'

    except TypeError as Te:
        print(3)
        temp = 'none'

    except Exception as e:
        print(4)
        temp = 'none'

    change = True 
    if (temp == 'none'):
        datas = temp_ant
        change = False
    
    if (temp_ant != datas):
        temp_ant = datas

    data = {
                'serial': temp,
                'serial_1': datas[0],
                'serial_2': datas[1],
                'serial_3': datas[2],
                'change': change
            }

    return JsonResponse(data)
