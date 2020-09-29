<<<<<<< HEAD:SIMEP.py
'''
Sistema de Medições de Processo
v0.1 - Initial Commit: Marcelo Souza / Robson Soares - 29/09/2020
---
'''
=======
>>>>>>> parent of 7c06504... Stable version:SIMEP280920.py
import _tkinter
from tkinter import *
from tkinter import Tk, Label
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import date
from datetime import datetime
from time import sleep
import sys
import mysql.connector
from PIL import ImageTk, Image
#from time import strftime, gmtime

#==================CRIA VARIAVEIS GLOBAIS=======================================
var_forno_atual=501

#================== FAZ A CONEXAO COM O BD ====================================
con = mysql.connector.connect(host='localhost',user='admin',password='geral',database='tablet8')
cursor = con.cursor()

'''
cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
valores_lidos_banho_data = cursor.fetchall()

datetablet = date.today()
datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

datebanco = valores_lidos_banho_data[0]
datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

if (datetablet_convertido == datebanco_convertido ):
    print('igual')
else:
    print('diferente')
'''


#==================CRIA RELATORIO CATODO=======================================
def relatorio_catodo():
    rel_catodo= Toplevel(login)
    rel_catodo.title("RELATORIO DE MEDIÇÕES CATODO")
    rel_catodo.attributes('-fullscreen' , 'true')

    cabecario = Label(rel_catodo, text="S I M E P   -   R E L A T O R I O   D E   M E D I Ç Õ E S   C A T O D O" ,font="century 20",  fg="#000099").place(x = 300, y=10 , width=950, height= 53)

     #==================CRIA LABE DATA DE HOJE RELATORIO CATODO=======================================
    cabecario_data = Label(rel_catodo, text=date.today() ,font="century 20",  fg="#000099").place(x = 280
                                                                                                  , y=50 , width=950, height= 53)
    #================== SELECIONA IMAGEM LOGO CBA RELATORIO CATODO  ====================================
    logo_cba_catodo = ImageTk.PhotoImage(file="C:\\Images Python\\Logocba.png")
    img = Label(rel_catodo, image=logo_cba_catodo)
    img.image = logo_cba_catodo
    img.place(x=10, y=10)
    
    #==================CRIA VARIAVEIS PARA LOOP RELATORIO CATODO=======================================
        
    inicio=501
    fim=518
    #==================CRIA LABEL CABECARIO RELATORIO CATODO=======================================
    label_c1_1a18 = Label(rel_catodo, text='CUBA  TEMP   BANHO    METAL  LOMBO'  ,font="century 10", bg="BLUE", fg="WHITE").place(x=10, y=110, width=285)
    label_c2__19a36 = Label(rel_catodo, text='CUBA     TEMP     BANHO    METAL  LOMBO' ,font="century 10", bg="BLUE", fg="WHITE").place(x=335, y=110, width=298)
    label_c3__1a18 = Label(rel_catodo, text='CUBA    TEMP    BANHO    METAL  LOMBO',font="century 10", bg="BLUE", fg="WHITE").place(x=675, y=110, width=290)
    label_c4__19a36 = Label(rel_catodo, text= 'CUBA    TEMP    BANHO    METAL  LOMBO',font="century 10", bg="BLUE", fg="WHITE").place(x=1005, y=110, width=288)

    #==================CRIA VARIAVEL INICIAL DE Y E INCREMENTO DE ESPACAMENTO ENTRE LINHAS=======================================
    espy_ini=140
    espy=32
    x=100
    
    #==================CRIA LOOP RELATORIO CATODO=====================================================================
    while(inicio<=fim):
        
        cuba_impar_1a18 = Label(rel_catodo, text=inicio ,font="century 12", bg="WHITE", fg="black").place(x=10, y=espy_ini, width=60)
        cuba_impar_19a36 = Label(rel_catodo, text=inicio+18 ,font="century 12", bg="WHITE", fg="black").place(x=335, y=espy_ini, width=60)
        cuba_par_1a18 = Label(rel_catodo, text=inicio+100 ,font="century 12", bg="WHITE", fg="black").place(x=675, y=espy_ini, width=60)
        cuba_par_19a36 = Label(rel_catodo, text=inicio+118 ,font="century 12", bg="WHITE", fg="black").place(x=1005, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE BANHO=====================================================================
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()
        print (valores_lidos_banho)#
        
        conte_linhas_nivelbanho = len(valores_lidos_banho)
        print (conte_linhas_nivelbanho)#
     
        
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
         
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))
        
        if (conte_linhas_data  < 1 ):
            ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=55, y=espy_ini, width=60)
            
        else:

            datebanco = valores_lidos_banho_data[0]  
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))                 
            if (conte_linhas_nivelbanho < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=55, y=espy_ini, width=60)

            else:
                ultima_banho = Label(rel_catodo, text= valores_lidos_banho[0], font="century 12", bg="WHITE", fg="black").place(x=55, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE TEMPERATURA=====================================================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()
        
        conte_linhas_temperatura = len(valores_lidos_temperatura)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=115, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))
        

            if (conte_linhas_temperatura < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=115, y=espy_ini, width=60)
            else:
                ultima_temperatura = Label(rel_catodo, text= valores_lidos_temperatura[0], font="century 12", bg="WHITE", fg="black").place(x=115, y=espy_ini, width=60)
        

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE METAL=====================================================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()
        
        conte_linhas_metal = len(valores_lidos_metal)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=175, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))
        
        

            if (conte_linhas_metal < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=175, y=espy_ini, width=60)
            else:
                ultima_metal = Label(rel_catodo, text= valores_lidos_metal[0], font="century 12", bg="WHITE", fg="black").place(x=175, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE LOMBO=====================================================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()
        
        conte_linhas_lombo = len(valores_lidos_lombo)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=235, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))        

            if (conte_linhas_lombo < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=235, y=espy_ini, width=60)
            else:
                ultima_lombo = Label(rel_catodo, text= valores_lidos_lombo[0], font="century 12", bg="WHITE", fg="black").place(x=235, y=espy_ini, width=60)

         #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE BANHO=====================================================================
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()
        
        conte_linhas_nivelbanho = len(valores_lidos_banho)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=395, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_nivelbanho < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=395, y=espy_ini, width=60)
            else:
                ultima_banho = Label(rel_catodo, text= valores_lidos_banho[0], font="century 12", bg="WHITE", fg="black").place(x=395, y=espy_ini, width=60)
  

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE TEMPERATURA=====================================================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()
        
        conte_linhas_temperatura = len(valores_lidos_temperatura)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=455, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_temperatura < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=455, y=espy_ini, width=60)
            else:
                ultima_temperatura = Label(rel_catodo, text= valores_lidos_temperatura[0], font="century 12", bg="WHITE", fg="black").place(x=455, y=espy_ini, width=60)
        

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE METAL=====================================================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()

        conte_linhas_metal = len(valores_lidos_metal)
        
        conte_linhas_metal = len(valores_lidos_metal)
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=515, y=espy_ini, width=60)
        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_metal < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=515, y=espy_ini, width=60)
            else:
                ultima_metal = Label(rel_catodo, text= valores_lidos_metal[0], font="century 12", bg="WHITE", fg="black").place(x=515, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE LOMBO=====================================================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()
        
        conte_linhas_lombo = len(valores_lidos_lombo)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+18) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=575, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_lombo < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=575, y=espy_ini, width=60)
            else:
                ultima_lombo = Label(rel_catodo, text= valores_lidos_lombo[0], font="century 12", bg="WHITE", fg="black").place(x=575, y=espy_ini, width=60)

         #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE BANHO=====================================================================
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()
        
        conte_linhas_nivelbanho = len(valores_lidos_banho)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=735, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_nivelbanho < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=735, y=espy_ini, width=60)
            else:
                ultima_banho = Label(rel_catodo, text= valores_lidos_banho[0], font="century 12", bg="WHITE", fg="black").place(x=735, y=espy_ini, width=60)
  

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE TEMPERATURA=====================================================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()
        
        conte_linhas_temperatura = len(valores_lidos_temperatura)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=795, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_temperatura < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=795, y=espy_ini, width=60)
            else:
                ultima_temperatura = Label(rel_catodo, text= valores_lidos_temperatura[0], font="century 12", bg="WHITE", fg="black").place(x=795, y=espy_ini, width=60)
        

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE METAL=====================================================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()
        
        conte_linhas_metal = len(valores_lidos_metal)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=855, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_metal < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=855, y=espy_ini, width=60)
            else:
                ultima_metal = Label(rel_catodo, text= valores_lidos_metal[0], font="century 12", bg="WHITE", fg="black").place(x=855, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE LOMBO=====================================================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()
        
        conte_linhas_lombo = len(valores_lidos_lombo)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+100) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=905, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_lombo < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=905, y=espy_ini, width=60)
            else:
                ultima_lombo = Label(rel_catodo, text= valores_lidos_lombo[0], font="century 12", bg="WHITE", fg="black").place(x=905, y=espy_ini, width=60)

         #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE BANHO=====================================================================
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()
        
        conte_linhas_nivelbanho = len(valores_lidos_banho)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1065, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_nivelbanho < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_banho = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1065, y=espy_ini, width=60)
            else:
                ultima_banho = Label(rel_catodo, text= valores_lidos_banho[0], font="century 12", bg="WHITE", fg="black").place(x=1065, y=espy_ini, width=60)
  

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE TEMPERATURA=====================================================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()
        
        conte_linhas_temperatura = len(valores_lidos_temperatura)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1125, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_temperatura < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_temperatura = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1125, y=espy_ini, width=60)
            else:
                ultima_temperatura = Label(rel_catodo, text= valores_lidos_temperatura[0], font="century 12", bg="WHITE", fg="black").place(x=1125, y=espy_ini, width=60)
        

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE METAL=====================================================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()
        
        conte_linhas_metal = len(valores_lidos_metal)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1185, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_metal < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_metal = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1185, y=espy_ini, width=60)
            else:
                ultima_metal = Label(rel_catodo, text= valores_lidos_metal[0], font="century 12", bg="WHITE", fg="black").place(x=1185, y=espy_ini, width=60)

        #==================RETORNA DO BANCO DE DADOS A ULTIMA MEDICAO DE LOMBO=====================================================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()
        
        conte_linhas_lombo = len(valores_lidos_lombo)

        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(inicio+118) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_data = len( valores_lidos_banho_data)
    
        datetablet = date.today()
        datetablet_convertido = (str(datetablet.year)+'-'+str(datetablet.month)+'-'+str(datetablet.day))

        if (conte_linhas_data  < 1 ):
            ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1235, y=espy_ini, width=60)

        else:
            
            datebanco = valores_lidos_banho_data[0]
            datebanco_convertido = (str(datebanco[0].year)+'-'+str(datebanco[0].month)+'-'+str(datebanco[0].day))

            if (conte_linhas_lombo < 1 or datebanco_convertido != datetablet_convertido): 
                ultima_lombo = Label(rel_catodo, text='***' ,font="century 12", bg="WHITE", fg="black").place(x=1235, y=espy_ini, width=60)
            else:
                ultima_lombo = Label(rel_catodo, text= valores_lidos_lombo[0], font="century 12", bg="WHITE", fg="black").place(x=1235, y=espy_ini, width=60)            
        
        inicio = inicio + 1
        espy_ini = espy_ini + espy

    def fechar_relatorio():
        rel_catodo.destroy()    
  
    bt_sair = Button(rel_catodo, text="S  A  I  R", width=15, height=4, font="Arial 25", background="#CDC9C9", command=fechar_relatorio).place(x=10, y=716, width=1290, height=45)
               
    

#CRIA JANELA MENSAGEBOX

def mensagem():
    mensagem = Toplevel(login)
    mensagem.title("SIMEP - MEDICOES DE CATODO")
    mensagem.attributes('-fullscreen' , 'true')
    #================== SELECIONA IMAGEM FUNDO CATODO ====================================
    #fundo_mensagem = ImageTk.PhotoImage(file="C:\\Images Python\\cuba_invalida.png")
    #img = Label(mensagem, image=fundo_mensagem)
    #img.image = fundo_mensagem
    #img.place(x=0, y=0)
      
    def fechar_mensagem():
        mensagem.destroy()
    #================== CRIA BOTAO FECHAR MENSAGEM E ATRIBUI IMAGEM DA LINHA ================   
    btn_mensagem = PhotoImage(file = "C:\Images Python\cuba_invalida.png")
    photoimage_mensagem = btn_mensagem
    msg = Button(mensagem, text = 'S A I R', image = photoimage_mensagem, compound = LEFT, command=fechar_mensagem)
    msg.image = photoimage_mensagem
    msg.place(x=0, y=0, width=1366, height=768)

       
 #CRIA JANELA PF

def PF():
    PF = Toplevel(login)
    PF.title("SIMEP - MEDICOES DO POINT FEEDER")
    PF.attributes('-fullscreen' , 'true')
    #================== SELECIONA IMAGEM FUNDO MENU ====================================
    fundo_PF = ImageTk.PhotoImage(file="C:\\Images Python\\Menu.png")
    img = Label(PF, image=fundo_PF)
    img.image = fundo_PF
    img.place(x=0, y=0)
    

#CRIA JANELA CATODO
def catodo():
    catodo = Toplevel(login)
    catodo.title("SIMEP - MEDICOES DE CATODO")
    catodo.attributes('-fullscreen' , 'true')
    #================== SELECIONA IMAGEM LOGO CBA CATODO ====================================
    logo_cba_catodo = ImageTk.PhotoImage(file="C:\\Images Python\\Logocba.png")
    img = Label(catodo, image=logo_cba_catodo)
    img.image = logo_cba_catodo
    img.place(x=50, y=10)

    
    def fechar_catodo():
        catodo.destroy()
    #================== ENVIAR  DADOS  NA TABELA CATODO  NO MYSQL====================================
    def enviar_catodo():
        data=datetime.now()
        cursor.execute("""INSERT INTO tablet8.catodo (Data, Forno, Banho, Temperatura, Metal, Lombo, Usuario) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(data,var_forno_atual, entry_banho.get(), entry_temperatura.get(), entry_metal.get(), ComboLombo.get(), user))
        con.commit()

        
        #cursor.execute("""INSERT INTO tablet8.catodo (Data, Forno, Banho, Temperatura, Metal, Lombo) VALUES (%s,%s,%s,%s,%s,%s)""",(0,0,0,0,0,0)
        #con.commit()
    #================== LIMPA ENTRY CATODO APOS ENVIO DADOS====================================    
        entry_banho.delete(0, END)
        entry_temperatura.delete(0, END)
        entry_metal.delete(0, END)
        ComboLombo.current(0)
        entry_banho.focus()
 
    #================== CRIA BOTAO SAIR CATODO E CHAMA def fechar_catodo ====================================
    bt_sair = Button(catodo, text="S  A  I  R", width=15, height=4, font="Arial 25", background="#CDC9C9", command=fechar_catodo).place(x=50, y=700, width=1300, height=53)
    
    #===============================CRIA ENTRY TELA CATODO ====================================   
    entry_cuba  = Entry(catodo, font="century 40" , bg="WHITE", bd=5, fg="#363636",)
    entry_cuba.place(x=50, y=185, width=250, height=55)
    entry_cuba.focus()
    entry_banho = Entry(catodo, font="century 36" , bg="WHITE", bd=5, fg="#363636",)
    entry_banho.place(x=600, y=245, width=120, height=55)
    entry_metal = Entry(catodo, font="century 36" , bg="WHITE", bd=5, fg="#363636",)
    entry_metal.place(x=600, y=345, width=120, height=55)
    entry_temperatura = Entry(catodo, font="century 36" , bg="WHITE", bd=5, fg="#363636",)
    entry_temperatura.place(x=600, y=445, width=120, height=55)
    
    #============================== CRIAÇÃO LISTA DE COMBINAÇÃO ===============================
    fonte_combo = ("century 30")
    ComboLombo = ttk.Combobox(catodo, values=["","AA","A","AN","NA","N","NR","RN","R","RR"], state = "readonly", font=fonte_combo)
    ComboLombo.option_add('*TCombobox*Listbox.font', fonte_combo) 
    ComboLombo.place(x=600, y=545, width=100, height=55)
    ComboLombo.current(0)
    ComboLombo.get()

    #===============================CRIA LABEL TELA CATODO ====================================
    cuba_selecionada = Label(catodo, text="C U B A                         S E L E C I O N A D A" ,font="century 20", bg="BLUE", fg="WHITE").place(x = 600, y=130 , width=680, height= 53)
    cuba_selecionada = Label(catodo, text="S I M E P   -   C O L E T A   D E   M E D I Ç Õ E S   C A T O D O" ,font="century 20",  fg="#000099").place(x = 300, y=10 , width=900, height= 53)
                                                                                                                                                     

    selecao_cuba = Label(catodo, text="DIGITE CUBA" ,font="century 20", bg="BLUE", fg="WHITE").place(x = 50, y=130 , width=250, height= 53)
    
    label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)

    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL BANHO ====================================
    cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_banho = cursor.fetchall()

    conte_linhas_nivelbanho = len(valores_lidos_banho)

    if (conte_linhas_nivelbanho < 1): 
        ultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
    else:
        ultima_banho = Label(catodo, text= valores_lidos_banho[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
        
    if (conte_linhas_nivelbanho < 2): 
        penultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)
    else:
        penultima_banho = Label(catodo, text=valores_lidos_banho[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)

    if (conte_linhas_nivelbanho < 3): 
        antepenultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)
    else:        
        antepenultima_banho = Label(catodo, text=valores_lidos_banho[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)

    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL METAL ====================================
    cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_metal = cursor.fetchall()

    conte_linhas_nivelmetal = len(valores_lidos_metal)

    if (conte_linhas_nivelmetal < 1): 
        ultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
    else:
        ultima_metal = Label(catodo, text= valores_lidos_metal[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
        
    if (conte_linhas_nivelmetal  < 2): 
        penultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)
    else:
        penultima_metal = Label(catodo, text=valores_lidos_metal[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)

    if (conte_linhas_nivelmetal  < 3): 
        antepenultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)
    else:        
        antepenultima_metal = Label(catodo, text=valores_lidos_metal[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)




    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL TEMPERATURA ====================================
    cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_temperatura = cursor.fetchall()

    conte_linhas_temp = len(valores_lidos_temperatura)

    if (conte_linhas_temp < 1): 
        ultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
    else:
        ultima_temperatura = Label(catodo, text= valores_lidos_temperatura[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
        
    if (conte_linhas_temp < 2): 
        penultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)
    else:
        penultima_temperatura = Label(catodo, text=valores_lidos_temperatura[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)

    if (conte_linhas_temp < 3): 
        antepenultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)
    else:        
        antepenultima_temperatura = Label(catodo, text=valores_lidos_temperatura[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)

    
    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS LOMBO ====================================
    cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_lombo = cursor.fetchall()

    conte_linhas_lombo = len(valores_lidos_lombo)

    if (conte_linhas_lombo < 1): 
        ultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
    else:
        ultima_lombo = Label(catodo, text= valores_lidos_lombo[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
        
    if (conte_linhas_lombo< 2): 
        penultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)
    else:
        penultima_lombo = Label(catodo, text=valores_lidos_lombo[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)

    if (conte_linhas_lombo< 3): 
        antepenultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)
    else:        
        antepenultima_lombo = Label(catodo, text=valores_lidos_lombo[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)


    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL BANHO ====================================
    cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_banho_data = cursor.fetchall()

    conte_linhas_banho_data = len(valores_lidos_banho_data)

    if (conte_linhas_banho_data < 1): 
        ultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
    else:
        ultima_data_banho = Label(catodo, text= valores_lidos_banho_data[0], font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
        
    if (conte_linhas_banho_data< 2): 
        penultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)
    else:
        penultima_data_banho = Label(catodo, text=valores_lidos_banho_data[1] ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)

    if (conte_linhas_banho_data< 3): 
        antepenultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)
    else:        
        antepenultima_data_banho = Label(catodo, text=valores_lidos_banho_data[2] ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)



    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL METAL ====================================
    cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_metal_data = cursor.fetchall()

    conte_linhas_metal_data = len(valores_lidos_metal_data)

    if (conte_linhas_metal_data < 1): 
        ultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
    else:
        ultima_data_metal = Label(catodo, text= valores_lidos_metal_data[0], font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
        
    if (conte_linhas_metal_data< 2): 
        penultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)
    else:
        penultima_data_metal = Label(catodo, text=valores_lidos_metal_data[1] ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)

    if (conte_linhas_metal_data< 3): 
        antepenultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
    else:        
        antepenultima_data_metal = Label(catodo, text=valores_lidos_metal_data[2] ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
    

    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA TEMPERATURA ====================================
    cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_temperatura_data = cursor.fetchall()

    conte_linhas_temperatura_data = len(valores_lidos_temperatura_data)

    if (conte_linhas_temperatura_data < 1): 
        ultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
    else:
        ultima_data_temperatura = Label(catodo, text= valores_lidos_temperatura_data[0], font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
        
    if (conte_linhas_temperatura_data< 2): 
        penultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)
    else:
        penultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[1] ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)

    if (conte_linhas_temperatura_data< 3): 
        antepenultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
    else:        
        antepenultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[2] ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
    

    #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA LOMBO ====================================
    cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
    valores_lidos_lombo_data = cursor.fetchall()

    conte_linhas_lombo_data = len(valores_lidos_lombo_data)

    if (conte_linhas_lombo_data < 1): 
        ultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
    else:
        ultima_data_lombo = Label(catodo, text= valores_lidos_lombo_data[0], font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
        
    if (conte_linhas_lombo_data< 2): 
        penultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)
    else:
        penultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[1] ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)

    if (conte_linhas_lombo_data< 3): 
        antepenultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
    else:        
        antepenultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[2] ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
    
    #===============================CRIA LABEL UNIDADE MEDIDA BANHO ====================================
    unidade_banho_ultima = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=830, y=245 , width=50, height= 53)
    unidade_banho_penultima = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=1030, y=245 , width=50, height= 53)
    unidade_banho_antepenultima_banho = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=1230, y=245 , width=50, height= 53)

    #===============================CRIA LABEL UNIDADE MEDIDA NIVEL METAL ====================================
    unidade_metal_ultima = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=830, y=345 , width=50, height= 53)
    unidade_metal_penultima = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=1030, y=345 , width=50, height= 53)
    unidade_metal_antepenultima_banho = Label(catodo, text="cm" ,font="century 20", bg="WHITE", fg="black").place(x=1230, y=345 , width=50, height= 53)

    #===============================CRIA LABEL UNIDADE MEDIDA TEMPERATURA ====================================
    unidade_temperatura_ultima = Label(catodo, text="ºC" ,font="century 20", bg="WHITE", fg="black").place(x=830, y=445 , width=50, height= 53)
    unidade_temperatura_penultima = Label(catodo, text="ºC" ,font="century 20", bg="WHITE", fg="black").place(x=1030, y=445 , width=50, height= 53)
    unidade_temperatura_antepenultima_banho = Label(catodo, text="ºC" ,font="century 20", bg="WHITE", fg="black").place(x=1230, y=445 , width=50, height= 53)

    #===============================CRIA LABEL IDENTIFICAÇÃO DAS MEDIÇÕES ====================================
    label_nivel_banho = Label(catodo, text="Nivel de Banho" ,font="Arial 16", fg="black").place(x=430, y=245 , width=150, height= 50)
    label_nivel_metal = Label(catodo, text="Nivel de Metal" ,font="Arial 16", fg="black").place(x=430, y=345 , width=150, height= 50)
    label_temperatura = Label(catodo, text="Temperatura" ,font="Arial 16", fg="black").place(x=430, y=445 , width=150, height= 50)
    label_lombo = Label(catodo, text="Lombo" ,font="Arial 16", fg="black").place(x=430, y=545 , width=150, height= 50)

     #===============================CRIA LABEL UNIDADE MEDIDA LOMBO ====================================
    #unidade_lombo_ultima = Label(catodo, text="ºAA" ,font="century 20", bg="WHITE", fg="black").place(x=830, y=545 , width=50, height= 53)
    #unidade_lombo_penultima = Label(catodo, text="A" ,font="century 20", bg="WHITE", fg="black").place(x=1030, y=545 , width=50, height= 53)
    #unidade_lombo_antepenultima_banho = Label(catodo, text="ºAR" ,font="century 20", bg="WHITE", fg="black").place(x=1230, y=545 , width=50, height= 53)

     #================== CRIA BOTAO ENVIAR DADOS CATODO ====================================
    bt_enviar_dados_catodo = Button(catodo, text="E  N  V  I  A  R", width=15, height=4, font="Arial 25", background="#CDC9C9", command = enviar_catodo).place(x=740, y=185, width=400, height=57)
    
   
    #===============================CRIA def SELECIONAR CUBA============================    
    def bt_selecionar():
        if (entry_cuba.get()==""):
            sleep(0.001) 
        else:
            global var_forno_atual
            def altera_cuba(var_forno_atual):
                return entry_cuba.get()
            
            var_forno_atual=altera_cuba(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
            entry_cuba.delete(0, END)

            #===============================ATUALIZA LABEL ULTIMOS VALORES BANHO ============================ 
            cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_banho = cursor.fetchall()

            conte_linhas_nivelbanho = len(valores_lidos_banho)

            if (conte_linhas_nivelbanho < 1): 
                ultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
            else:
                ultima_banho = Label(catodo, text= valores_lidos_banho[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
                
            if (conte_linhas_nivelbanho < 2): 
                penultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)
            else:
                penultima_banho = Label(catodo, text=valores_lidos_banho[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)

            if (conte_linhas_nivelbanho < 3): 
                antepenultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)
            else:        
                antepenultima_banho = Label(catodo, text=valores_lidos_banho[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)

            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL METAL ====================================
            cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_metal = cursor.fetchall()

            conte_linhas_nivelmetal = len(valores_lidos_metal)

            if (conte_linhas_nivelmetal < 1): 
                ultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
            else:
                ultima_metal = Label(catodo, text= valores_lidos_metal[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
                
            if (conte_linhas_nivelmetal  < 2): 
                penultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)
            else:
                penultima_metal = Label(catodo, text=valores_lidos_metal[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)

            if (conte_linhas_nivelmetal  < 3): 
                antepenultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)
            else:        
                antepenultima_metal = Label(catodo, text=valores_lidos_metal[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)




            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL TEMPERATURA ====================================
            cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_temperatura = cursor.fetchall()

            conte_linhas_temp = len(valores_lidos_temperatura)

            if (conte_linhas_temp < 1): 
                ultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
            else:
                ultima_temperatura = Label(catodo, text= valores_lidos_temperatura[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
                
            if (conte_linhas_temp < 2): 
                penultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)
            else:
                penultima_temperatura = Label(catodo, text=valores_lidos_temperatura[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)

            if (conte_linhas_temp < 3): 
                antepenultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)
            else:        
                antepenultima_temperatura = Label(catodo, text=valores_lidos_temperatura[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)

            
            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS LOMBO ====================================
            cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_lombo = cursor.fetchall()

            conte_linhas_lombo = len(valores_lidos_lombo)

            if (conte_linhas_lombo < 1): 
                ultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
            else:
                ultima_lombo = Label(catodo, text= valores_lidos_lombo[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
                
            if (conte_linhas_lombo< 2): 
                penultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)
            else:
                penultima_lombo = Label(catodo, text=valores_lidos_lombo[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)

            if (conte_linhas_lombo< 3): 
                antepenultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)
            else:        
                antepenultima_lombo = Label(catodo, text=valores_lidos_lombo[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)


            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL BANHO ====================================
            cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_banho_data = cursor.fetchall()

            conte_linhas_banho_data = len(valores_lidos_banho_data)

            if (conte_linhas_banho_data < 1): 
                ultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
            else:
                ultima_data_banho = Label(catodo, text= valores_lidos_banho_data[0], font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
                
            if (conte_linhas_banho_data< 2): 
                penultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)
            else:
                penultima_data_banho = Label(catodo, text=valores_lidos_banho_data[1] ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)

            if (conte_linhas_banho_data< 3): 
                antepenultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)
            else:        
                antepenultima_data_banho = Label(catodo, text=valores_lidos_banho_data[2] ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)



            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL METAL ====================================
            cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_metal_data = cursor.fetchall()

            conte_linhas_metal_data = len(valores_lidos_metal_data)

            if (conte_linhas_metal_data < 1): 
                ultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
            else:
                ultima_data_metal = Label(catodo, text= valores_lidos_metal_data[0], font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
                
            if (conte_linhas_metal_data< 2): 
                penultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)
            else:
                penultima_data_metal = Label(catodo, text=valores_lidos_metal_data[1] ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)

            if (conte_linhas_metal_data< 3): 
                antepenultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
            else:        
                antepenultima_data_metal = Label(catodo, text=valores_lidos_metal_data[2] ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
            

            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA TEMPERATURA ====================================
            cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_temperatura_data = cursor.fetchall()

            conte_linhas_temperatura_data = len(valores_lidos_temperatura_data)

            if (conte_linhas_temperatura_data < 1): 
                ultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
            else:
                ultima_data_temperatura = Label(catodo, text= valores_lidos_temperatura_data[0], font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
                
            if (conte_linhas_temperatura_data< 2): 
                penultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)
            else:
                penultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[1] ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)

            if (conte_linhas_temperatura_data< 3): 
                antepenultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
            else:        
                antepenultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[2] ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
            

            #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA LOMBO ====================================
            cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
            valores_lidos_lombo_data = cursor.fetchall()

            conte_linhas_lombo_data = len(valores_lidos_lombo_data)

            if (conte_linhas_lombo_data < 1): 
                ultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
            else:
                ultima_data_lombo = Label(catodo, text= valores_lidos_lombo_data[0], font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
                
            if (conte_linhas_lombo_data< 2): 
                penultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)
            else:
                penultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[1] ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)

            if (conte_linhas_lombo_data< 3): 
                antepenultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
            else:        
                antepenultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[2] ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
            
    #===============================CRIA def SELECIONAR PROX CUBA============================ 
    def bt_prox():
        global var_forno_atual        
        def muda_prox_forno(var_forno_atual):
            return (int(var_forno_atual) + 1)            
        #===============================INTERTRAVAMENTO CUBAS SALA 2============================ 
        if (int(var_forno_atual)>=301) and (int(var_forno_atual)<380) or (int(var_forno_atual)>=401) and (int(var_forno_atual)<480):                    
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 3============================ 
        elif (int(var_forno_atual)>=501) and (int(var_forno_atual)<579) or (int(var_forno_atual)>=601) and (int(var_forno_atual)<679):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 4============================
        elif (int(var_forno_atual)>=701) and (int(var_forno_atual)<780) or (int(var_forno_atual)>=801) and (int(var_forno_atual)<880):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 5============================
        elif (int(var_forno_atual)>=901) and (int(var_forno_atual)<972) or (int(var_forno_atual)>=1001) and (int(var_forno_atual)<1072):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>=1101) and (int(var_forno_atual)<1172) or (int(var_forno_atual)>=1201) and (int(var_forno_atual)<1272):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 6============================
        elif (int(var_forno_atual)>=1301) and (int(var_forno_atual)<1341) or (int(var_forno_atual)>=1401) and (int(var_forno_atual)<1441):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>=1501) and (int(var_forno_atual)<1541) or (int(var_forno_atual)>=1601) and (int(var_forno_atual)<1641):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 7============================
        elif (int(var_forno_atual)>=1701) and (int(var_forno_atual)<1749) or (int(var_forno_atual)>=1801) and (int(var_forno_atual)<1849):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>=1901) and (int(var_forno_atual)<1949) or (int(var_forno_atual)>=2001) and (int(var_forno_atual)<2049):
            var_forno_atual=muda_prox_forno(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        else:
             mensagem()
             
        #===============================ATUALIZA LABEL ULTIMOS VALORES BANHO ============================ 
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()

        conte_linhas_nivelbanho = len(valores_lidos_banho)

        if (conte_linhas_nivelbanho < 1): 
            ultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
        else:
            ultima_banho = Label(catodo, text= valores_lidos_banho[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
            
        if (conte_linhas_nivelbanho < 2): 
            penultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)
        else:
            penultima_banho = Label(catodo, text=valores_lidos_banho[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)

        if (conte_linhas_nivelbanho < 3): 
            antepenultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)
        else:        
            antepenultima_banho = Label(catodo, text=valores_lidos_banho[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL METAL ====================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()

        conte_linhas_nivelmetal = len(valores_lidos_metal)

        if (conte_linhas_nivelmetal < 1): 
            ultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
        else:
            ultima_metal = Label(catodo, text= valores_lidos_metal[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
            
        if (conte_linhas_nivelmetal  < 2): 
            penultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)
        else:
            penultima_metal = Label(catodo, text=valores_lidos_metal[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)

        if (conte_linhas_nivelmetal  < 3): 
            antepenultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)
        else:        
            antepenultima_metal = Label(catodo, text=valores_lidos_metal[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)




        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL TEMPERATURA ====================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()

        conte_linhas_temp = len(valores_lidos_temperatura)

        if (conte_linhas_temp < 1): 
            ultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
        else:
            ultima_temperatura = Label(catodo, text= valores_lidos_temperatura[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
            
        if (conte_linhas_temp < 2): 
            penultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)
        else:
            penultima_temperatura = Label(catodo, text=valores_lidos_temperatura[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)

        if (conte_linhas_temp < 3): 
            antepenultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)
        else:        
            antepenultima_temperatura = Label(catodo, text=valores_lidos_temperatura[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)

        
        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS LOMBO ====================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()

        conte_linhas_lombo = len(valores_lidos_lombo)

        if (conte_linhas_lombo < 1): 
            ultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
        else:
            ultima_lombo = Label(catodo, text= valores_lidos_lombo[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
            
        if (conte_linhas_lombo< 2): 
            penultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)
        else:
            penultima_lombo = Label(catodo, text=valores_lidos_lombo[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)

        if (conte_linhas_lombo< 3): 
            antepenultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)
        else:        
            antepenultima_lombo = Label(catodo, text=valores_lidos_lombo[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)


        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL BANHO ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_banho_data = len(valores_lidos_banho_data)

        if (conte_linhas_banho_data < 1): 
            ultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
        else:
            ultima_data_banho = Label(catodo, text= valores_lidos_banho_data[0], font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
            
        if (conte_linhas_banho_data< 2): 
            penultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)
        else:
            penultima_data_banho = Label(catodo, text=valores_lidos_banho_data[1] ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)

        if (conte_linhas_banho_data< 3): 
            antepenultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)
        else:        
            antepenultima_data_banho = Label(catodo, text=valores_lidos_banho_data[2] ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)



        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL METAL ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_metal_data = cursor.fetchall()

        conte_linhas_metal_data = len(valores_lidos_metal_data)

        if (conte_linhas_metal_data < 1): 
            ultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
        else:
            ultima_data_metal = Label(catodo, text= valores_lidos_metal_data[0], font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
            
        if (conte_linhas_metal_data< 2): 
            penultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)
        else:
            penultima_data_metal = Label(catodo, text=valores_lidos_metal_data[1] ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)

        if (conte_linhas_metal_data< 3): 
            antepenultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
        else:        
            antepenultima_data_metal = Label(catodo, text=valores_lidos_metal_data[2] ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
        

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA TEMPERATURA ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_temperatura_data = cursor.fetchall()

        conte_linhas_temperatura_data = len(valores_lidos_temperatura_data)

        if (conte_linhas_temperatura_data < 1): 
            ultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
        else:
            ultima_data_temperatura = Label(catodo, text= valores_lidos_temperatura_data[0], font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
            
        if (conte_linhas_temperatura_data< 2): 
            penultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)
        else:
            penultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[1] ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)

        if (conte_linhas_temperatura_data< 3): 
            antepenultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
        else:        
            antepenultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[2] ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
        

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA LOMBO ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_lombo_data = cursor.fetchall()

        conte_linhas_lombo_data = len(valores_lidos_lombo_data)

        if (conte_linhas_lombo_data < 1): 
            ultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
        else:
            ultima_data_lombo = Label(catodo, text= valores_lidos_lombo_data[0], font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
            
        if (conte_linhas_lombo_data< 2): 
            penultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)
        else:
            penultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[1] ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)

        if (conte_linhas_lombo_data< 3): 
            antepenultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
        else:        
            antepenultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[2] ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
        
            
        
    def bt_ant():
        global var_forno_atual
        def muda_forno_ant(var_forno_atual):
            return (int(var_forno_atual) - 1)
        #===============================INTERTRAVAMENTO CUBAS SALA 2============================ 
        if (int(var_forno_atual)>301) and (int(var_forno_atual)<=380) or (int(var_forno_atual)>401) and (int(var_forno_atual)<=480):                    
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)

        #===============================INTERTRAVAMENTO CUBAS SALA 3============================ 
        elif (int(var_forno_atual)>501) and (int(var_forno_atual)<=579) or (int(var_forno_atual)>601) and (int(var_forno_atual)<=679):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 4============================
        elif (int(var_forno_atual)>701) and (int(var_forno_atual)<=780) or (int(var_forno_atual)>801) and (int(var_forno_atual)<=880):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 5============================
        elif (int(var_forno_atual)>901) and (int(var_forno_atual)<=972) or (int(var_forno_atual)>1001) and (int(var_forno_atual)<=1072):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>1101) and (int(var_forno_atual)<=1172) or (int(var_forno_atual)>1201) and (int(var_forno_atual)<=1272):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 6============================
        elif (int(var_forno_atual)>1301) and (int(var_forno_atual)<=1341) or (int(var_forno_atual)>1401) and (int(var_forno_atual)<=1441):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>1501) and (int(var_forno_atual)<=1541) or (int(var_forno_atual)>1601) and (int(var_forno_atual)<=1641):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        #===============================INTERTRAVAMENTO CUBAS SALA 7============================
        elif (int(var_forno_atual)>1701) and (int(var_forno_atual)<=1749) or (int(var_forno_atual)>1801) and (int(var_forno_atual)<=1849):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        elif (int(var_forno_atual)>1901) and (int(var_forno_atual)<=1949) or (int(var_forno_atual)>2001) and (int(var_forno_atual)<=2049):
            var_forno_atual=muda_forno_ant(var_forno_atual)
            label_cuba_selecionada = Label(catodo, text=var_forno_atual ,font="century 34", bg="BLUE", fg="WHITE").place(x = 800, y=130 , width=100, height= 45)
        else:
             mensagem()
   

        #===============================ATUALIZA LABEL ULTIMOS VALORES BANHO ============================ 
        cursor.execute("SELECT Banho FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_banho = cursor.fetchall()

        conte_linhas_nivelbanho = len(valores_lidos_banho)

        if (conte_linhas_nivelbanho < 1): 
            ultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
        else:
            ultima_banho = Label(catodo, text= valores_lidos_banho[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=245 , width=100, height= 53)
            
        if (conte_linhas_nivelbanho < 2): 
            penultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)
        else:
            penultima_banho = Label(catodo, text=valores_lidos_banho[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=245 , width=100, height= 53)

        if (conte_linhas_nivelbanho < 3): 
            antepenultima_banho = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)
        else:        
            antepenultima_banho = Label(catodo, text=valores_lidos_banho[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=245 , width=100, height= 53)

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL METAL ====================================
        cursor.execute("SELECT Metal FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_metal = cursor.fetchall()

        conte_linhas_nivelmetal = len(valores_lidos_metal)

        if (conte_linhas_nivelmetal < 1): 
            ultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
        else:
            ultima_metal = Label(catodo, text= valores_lidos_metal[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=345 , width=100, height= 53)
            
        if (conte_linhas_nivelmetal  < 2): 
            penultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)
        else:
            penultima_metal = Label(catodo, text=valores_lidos_metal[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=345 , width=100, height= 53)

        if (conte_linhas_nivelmetal  < 3): 
            antepenultima_metal = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)
        else:        
            antepenultima_metal = Label(catodo, text=valores_lidos_metal[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=345 , width=100, height= 53)




        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS NIVEL TEMPERATURA ====================================
        cursor.execute("SELECT Temperatura FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_temperatura = cursor.fetchall()

        conte_linhas_temp = len(valores_lidos_temperatura)

        if (conte_linhas_temp < 1): 
            ultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
        else:
            ultima_temperatura = Label(catodo, text= valores_lidos_temperatura[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=445 , width=100, height= 53)
            
        if (conte_linhas_temp < 2): 
            penultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)
        else:
            penultima_temperatura = Label(catodo, text=valores_lidos_temperatura[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=445 , width=100, height= 53)

        if (conte_linhas_temp < 3): 
            antepenultima_temperatura = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)
        else:        
            antepenultima_temperatura = Label(catodo, text=valores_lidos_temperatura[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=445 , width=100, height= 53)

        
        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS LOMBO ====================================
        cursor.execute("SELECT Lombo FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_lombo = cursor.fetchall()

        conte_linhas_lombo = len(valores_lidos_lombo)

        if (conte_linhas_lombo < 1): 
            ultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
        else:
            ultima_lombo = Label(catodo, text= valores_lidos_lombo[0], font="century 20", bg="WHITE", fg="black").place(x=730, y=545 , width=100, height= 53)
            
        if (conte_linhas_lombo< 2): 
            penultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)
        else:
            penultima_lombo = Label(catodo, text=valores_lidos_lombo[1] ,font="century 20", bg="WHITE", fg="black").place(x=930, y=545 , width=100, height= 53)

        if (conte_linhas_lombo< 3): 
            antepenultima_lombo = Label(catodo, text='***' ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)
        else:        
            antepenultima_lombo = Label(catodo, text=valores_lidos_lombo[2] ,font="century 20", bg="WHITE", fg="black").place(x=1130, y=545 , width=100, height= 53)


        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL BANHO ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_banho_data = cursor.fetchall()

        conte_linhas_banho_data = len(valores_lidos_banho_data)

        if (conte_linhas_banho_data < 1): 
            ultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
        else:
            ultima_data_banho = Label(catodo, text= valores_lidos_banho_data[0], font="century 10", fg="black").place(x=730, y=300 , width=130, height= 25)
            
        if (conte_linhas_banho_data< 2): 
            penultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)
        else:
            penultima_data_banho = Label(catodo, text=valores_lidos_banho_data[1] ,font="century 10", fg="black").place(x=930, y=300 , width=130, height= 25)

        if (conte_linhas_banho_data< 3): 
            antepenultima_data_banho = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)
        else:        
            antepenultima_data_banho = Label(catodo, text=valores_lidos_banho_data[2] ,font="century 10", fg="black").place(x=1130, y=300 , width=130, height= 25)



        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA NIVEL METAL ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_metal_data = cursor.fetchall()

        conte_linhas_metal_data = len(valores_lidos_metal_data)

        if (conte_linhas_metal_data < 1): 
            ultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
        else:
            ultima_data_metal = Label(catodo, text= valores_lidos_metal_data[0], font="century 10", fg="black").place(x=730, y=400 , width=130, height= 25)
            
        if (conte_linhas_metal_data< 2): 
            penultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)
        else:
            penultima_data_metal = Label(catodo, text=valores_lidos_metal_data[1] ,font="century 10", fg="black").place(x=930, y=400 , width=130, height= 25)

        if (conte_linhas_metal_data< 3): 
            antepenultima_data_metal = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
        else:        
            antepenultima_data_metal = Label(catodo, text=valores_lidos_metal_data[2] ,font="century 10", fg="black").place(x=1130, y=400 , width=130, height= 25)
        

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA TEMPERATURA ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_temperatura_data = cursor.fetchall()

        conte_linhas_temperatura_data = len(valores_lidos_temperatura_data)

        if (conte_linhas_temperatura_data < 1): 
            ultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
        else:
            ultima_data_temperatura = Label(catodo, text= valores_lidos_temperatura_data[0], font="century 10", fg="black").place(x=730, y=500 , width=130, height= 25)
            
        if (conte_linhas_temperatura_data< 2): 
            penultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)
        else:
            penultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[1] ,font="century 10", fg="black").place(x=930, y=500 , width=130, height= 25)

        if (conte_linhas_temperatura_data< 3): 
            antepenultima_data_temperatura = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
        else:        
            antepenultima_data_temperatura = Label(catodo, text=valores_lidos_temperatura_data[2] ,font="century 10", fg="black").place(x=1130, y=500 , width=130, height= 25)
        

        #===============================CRIA LABEL ULTIMOS VALORES COLETADOS DATA LOMBO ====================================
        cursor.execute("SELECT Data FROM tablet8.catodo where Forno = " + str(var_forno_atual) + " order by Data desc")
        valores_lidos_lombo_data = cursor.fetchall()

        conte_linhas_lombo_data = len(valores_lidos_lombo_data)

        if (conte_linhas_lombo_data < 1): 
            ultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
        else:
            ultima_data_lombo = Label(catodo, text= valores_lidos_lombo_data[0], font="century 10", fg="black").place(x=730, y=600 , width=130, height= 25)
            
        if (conte_linhas_lombo_data< 2): 
            penultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)
        else:
            penultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[1] ,font="century 10", fg="black").place(x=930, y=600 , width=130, height= 25)

        if (conte_linhas_lombo_data< 3): 
            antepenultima_data_lombo = Label(catodo, text='***' ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
        else:        
            antepenultima_data_lombo = Label(catodo, text=valores_lidos_lombo_data[2] ,font="century 10", fg="black").place(x=1130, y=600 , width=130, height= 25)
        
        
            
    #===============================CRIA DEF COMANDO BOTAO TECLADO======================
    def insere1(): entry_cuba.focus_displayof().insert(INSERT,"1")
    def insere2(): entry_cuba.focus_displayof().insert(INSERT,"2")
    def insere3(): entry_cuba.focus_displayof().insert(INSERT,"3")
    def insere4(): entry_cuba.focus_displayof().insert(INSERT,"4")
    def insere5(): entry_cuba.focus_displayof().insert(INSERT,"5")
    def insere6(): entry_cuba.focus_displayof().insert(INSERT,"6")
    def insere7(): entry_cuba.focus_displayof().insert(INSERT,"7")
    def insere8(): entry_cuba.focus_displayof().insert(INSERT,"8")
    def insere9(): entry_cuba.focus_displayof().insert(INSERT,"9")
    def insere0(): entry_cuba.focus_displayof().insert(INSERT,"0")
    def inserevir(): entry_cuba.focus_displayof().insert(INSERT,".")    
    def limpar(): entry_cuba.focus_displayof().delete(0, END)

    #===============================CRIA BOTAO TECLADO=============================
    #CRIA BOTAO 1 E CHAMA VARIAVEL
    bt1 = Button(catodo, text = "1", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere1)
    bt1.place(x=50, y=252, width=80, height=70)

    #CRIA BOTAO 2 E CHAMA VARIAVEL
    bt2 = Button(catodo, text = "2", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere2)
    bt2.place(x=135, y=252, width=80, height=70)
    #CRIA BOTAO 3 E CHAMA VARIAVEL
    bt3 = Button(catodo, text = "3", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere3)
    bt3.place(x=220, y=252, width=80, height=70)
    #CRIA BOTAO 4 E CHAMA VARIAVEL
    bt4 = Button(catodo, text = "4", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere4)
    bt4.place(x=50, y=330, width=80, height=70)
    #CRIA BOTAO 5 E CHAMA VARIAVEL
    bt5 = Button(catodo, text = "5", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere5)
    bt5.place(x=135, y=330, width=80, height=70)
    #CRIA BOTAO 6 E CHAMA VARIAVEL
    bt6 = Button(catodo, text = "6", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere6)
    bt6.place(x=220, y=330, width=80, height=70)
    #CRIA BOTAO 7 E CHAMA VARIAVEL
    bt7 = Button(catodo, text = "7", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere7)
    bt7.place(x=50, y=408, width=80, height=70)
    #CRIA BOTAO 8 E CHAMA VARIAVEL
    bt8 = Button(catodo, text = "8", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere8)
    bt8.place(x=135, y=408, width=80, height=70)
    #CRIA BOTAO 9 E CHAMA VARIAVEL
    bt9 = Button(catodo, text = "9", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere9)
    bt9.place(x=220, y=408, width=80, height=70)
    #CRIA BOTAO 0 E CHAMA VARIAVEL
    bt0 = Button(catodo, text = "0", width = 10, height = 4, font="Arial 30", background = "#CDC9C9", command = insere0)
    bt0.place(x=135, y=486, width=80, height=70)
    #CRIA BOTAO PROX. E CHAMA VARIAVEL
    btp = Button(catodo, text = "PROX.", width = 17, height = 3, font="Arial 25", background = "#828282", command = bt_prox)
    btp.place(x=600, y=185, width=130, height=57)
    #CRIA BOTAO ANT. E CHAMA VARIAVEL
    bta = Button(catodo, text = "ANT.", width = 17, height = 3, font="Arial 25", background = "#828282" , command = bt_ant)
    bta.place(x=1151, y=185, width=130, height=57)
    #CRIA BOTAO SELECIONAR E CHAMA VARIAVEL
    bts = Button(catodo, text = "SELECIONAR", width = 34, height = 3, font="Arial 24", background = "#828282", command = bt_selecionar)
    bts.place(x=50, y=568, width=250, height=57)
    #CRIA BOTAO LIMPAR E CHAMA VARIAVEL
    bts = Button(catodo, text = "LIMPAR", width = 34, height = 3, font="Arial 24", background = "#828282", command = limpar )
    bts.place(x=50, y=632, width=250, height=57)


    #================== CRIA A JANELA MENU ====================================
def menu():    
    Menu = Toplevel(login)
    Menu.title("MEDIÇÕES SALAS FORNOS")
    Menu.geometry("1366x768")
    Menu.attributes('-fullscreen' , 'true')

    #================== SELECIONA IMAGEM FUNDO MENU ====================================
    fundo_menu = tk.PhotoImage(file="C:\\Images Python\\Menu1.png")
    img = Label(Menu, image=fundo_menu)
    img.image = fundo_menu
    img.place(x=0, y=0)

    #================== SELECIONA IMAGEM LOGO AUTOMAÇÃO ====================================
    logo_automa_menu = tk.PhotoImage(file="C:\\Images Python\\Logoautoma_menor.png")
    img = Label(Menu, image=logo_automa_menu)
    img.image = logo_automa_menu
    img.place(x=1200, y=40)

    #================== SELECIONA IMAGEM ABAIXO BOTAO ANODO ====================================
    #foto_anodo = ImageTk.PhotoImage(file="C:\\Images Python\\anodo.png")
    #label_foto_anodo = Label(Menu, image=foto_anodo)
    #label_foto_anodo.image = foto_anodo
    #label_foto_anodo.place(x=150, y=272,width=185, height=150)

    #================== CRIA BOTOES COM ICONE NA JANELA DE MENU ====================================

    btn_anodo = tk.PhotoImage(file = "C:\Images Python\icone_anodo.png")
    photoimage_anodo = btn_anodo
    anodo=Button(Menu, text = 'A  N  O  D  O',  compound = LEFT, image=photoimage_anodo )
    anodo.image = photoimage_anodo
    anodo.place(x=30, y=255, width=260, height=110)


    btn_PF = PhotoImage(file = "C:\Images Python\icone_pf.png")
    photoimage_pf = btn_PF
    pf=Button(Menu, text = 'P O I N T   F E E D E R', image = photoimage_pf, compound = LEFT)
    pf.image = photoimage_pf
    pf.place(x=590, y=610, width=260, height=110) 

    btn_catodo = PhotoImage(file = "C:\Images Python\icone_catodo.png")
    photoimage_catodo = btn_catodo
    bt_img_catodo=Button(Menu, text = 'C  A  T  O  D  O', image = photoimage_catodo, compound = LEFT, command=catodo)
    bt_img_catodo.image = photoimage_catodo
    bt_img_catodo.place(x=320, y=255, width=260, height=110)

    btn_rel_catodo = PhotoImage(file = "C:\Images Python\icone_rel_catodo.png")
    photoimage_rel_catodo = btn_rel_catodo
    rel_catodo = Button(Menu, text = 'R E L A T O R I O\nC A T O D O', image = photoimage_rel_catodo, compound = TOP, bg="#EEE5DE", fg="#00008D", command=relatorio_catodo)
    rel_catodo.img = photoimage_rel_catodo
    rel_catodo.place(x=800, y=345, width=150, height=150)


    btn_QA_QC = PhotoImage(file = "C:\Images Python\icone_QA_QC.png")
    photoimage_qa_qc = btn_QA_QC
    qa_qc = Button(Menu, text = 'Q A  /  Q C', image = photoimage_qa_qc, compound = LEFT)
    qa_qc.img = photoimage_qa_qc
    qa_qc.place(x=500, y=492, width=260, height=110)


    btn_temperatura = PhotoImage(file = "C:\Images Python\icone_temperatura.png")
    photoimage_temperatura = btn_temperatura
    btn_temperatura = Button(Menu, text = 'T E M P E R A T U R A', image = photoimage_temperatura, compound = LEFT)
    btn_temperatura.img = photoimage_temperatura
    btn_temperatura.place(x=405, y=375, width=260, height=110)

    
    def Fechar_menu():
        Menu.destroy()
    
    bt_sair = Button(Menu, text="S  A  I  R", width=15, height=4, font="Arial 25", background="#CDC9C9", command = Fechar_menu)
    bt_sair.place(x=0, y=725, width=1370, height=45)

    #===================================== CRIA LABEL NOME SISTEMA NO MENU ====================================
    cuba_selecionada = Label(Menu, text="S I M E P   -   S I S T E M A   D E   M E D I Ç Õ E S\n   P R O C E S S O S" ,font=("century", 18, "bold"),  bg="#2F5597", fg="#FFFF66").place(x = 660, y=200 , width=685, height= 100)
    cabecalho_relatorios = Label(Menu, text="R E L A T O R I O S  D E  M E D I Ç Õ E S" ,font=("century", 18, "bold"),  bg="#2F5597", fg="#EEEEEE").place(x = 700, y=300 , width=600, height= 50)

#CRIA JANELA LOGIN
login = Tk()
login.title("SIMEP - LOGIN DE USUARIO")
login.geometry('500x450')
#Fundo_Tela = tk.PhotoImage(file="/home/pi/PythonNUC/Fundo_Tela.PNG")
#Fundo = Label(login, image=Fundo_Tela)
#Fundo.pack()
#login.attributes('-fullscreen' , 'true')
            
# CRIA DEF COMANDO BOTAO
def insere1(): PASSWORD.insert(INSERT,"1")
def insere2(): PASSWORD.insert(INSERT,"2")
def insere3(): PASSWORD.insert(INSERT,"3")
def insere4(): PASSWORD.insert(INSERT,"4")
def insere5(): PASSWORD.insert(INSERT,"5")
def insere6(): PASSWORD.insert(INSERT,"6")
def insere7(): PASSWORD.insert(INSERT,"7")
def insere8(): PASSWORD.insert(INSERT,"8")
def insere9(): PASSWORD.insert(INSERT,"9")
def insere0(): PASSWORD.insert(INSERT,"0")
def inserevir(): PASSWORD.insert(INSERT,".")

#CRIA BOTAO 1 E CHAMA VARIAVEL
bt1 = Button(login, text="1", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere1)
bt1.place(x=20+20, y=52, width=80, height=70 )


#CRIA BOTAO 2 E CHAMA VARIAVEL
bt2 = Button(login, text="2", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere2)
bt2.place(x=105+20, y=52, width=80, height=70)
#CRIA BOTAO 3 E CHAMA VARIAVEL
bt3 = Button(login, text="3", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere3)
bt3.place(x=190+20, y=52, width=80, height=70)
#CRIA BOTAO 4 E CHAMA VARIAVEL
bt4 = Button(login, text="4", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere4)
bt4.place(x=275+20, y=52, width=80, height=70)
#CRIA BOTAO 5 E CHAMA VARIAVEL
bt5 = Button(login, text="5", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere5)
bt5.place(x=360+20, y=52, width=80, height=70)
#CRIA BOTAO 6 E CHAMA VARIAVEL
bt6 = Button(login, text="6", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere6)
bt6.place(x=20+20, y=130, width=80, height=70)
#CRIA BOTAO 7 E CHAMA VARIAVEL
bt7 = Button(login, text="7", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere7)
bt7.place(x=105+20, y=130, width=80, height=70)
#CRIA BOTAO 8 E CHAMA VARIAVEL
bt8 = Button(login, text="8", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere8)
bt8.place(x=190+20, y=130, width=80, height=70)
#CRIA BOTAO 9 E CHAMA VARIAVEL
bt9 = Button(login, text="9", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere9)
bt9.place(x=275+20, y=130, width=80, height=70)
#CRIA BOTAO 0 E CHAMA VARIAVEL
bt0 = Button(login, text="0", width = 10, height = 4, font="Arial 30", background="#CDC9C9", command=insere0)
bt0.place(x=360+20, y=130, width=80, height=70)
        
l1= Label(login, text="DIGITE  A  SENHA", font="century 28", bg="#00008B", fg="white", bd=3).place(x = 20+20, y = 5, width=421, height=45)

#CRIA CAIXA ENTRADA DADOS
PASSWORD = Entry(login, text="DIGITE SUA SENHA",show ="*", font="impact 35" , bg="#E8E8E8", bd=5, fg="#363636",)
PASSWORD.place(x=20+20, y=250, width=415, height=65)
PASSWORD.focus()


def bt_click():
    if PASSWORD.get() == "":   
        messagebox.showerror("ATENCAO", "DIGITE SUA SENHA!!!")
    else:
        a = "SELECT usuario FROM user_local WHERE senha = " + (PASSWORD.get())
        #print(a)
        cursor.execute(a)
        b = cursor.fetchone()
        c =str(b).strip("(',')")
        #print("1",a, "\n2->", c)
        if(b != None):
            global user, senha
            user = c
            senha = PASSWORD.get()
            Limpa_PASSWORD()
            menu()
                    
        else:
            messagebox.showerror("ATENCAO", "USUARIO NAO CADASTRADO!!!")
                    

#LIMPA CAIXA DE ENTRADA ED1
def Limpa_PASSWORD():
    PASSWORD.delete(0, END)

def Fechar_Login():
    login.destroy()

#CRIA BOTAO SALVAR E CHAMA FUNCAO def bt_click
btf = Button(login, text="ACESSAR", width=15, height=4, font="impact 25", background="GREY", command=bt_click)
btf.place(x=20+20, y=320, width=155, height=70)

#CRIA BOTAO LIMPAR E CHAMA VARIAVEL
bts = Button(login, text="LIMPAR", width=15, height=4, font="impact 25", background="#CDC9C9", command=Limpa_PASSWORD)
bts.place(x=270+29, y=320, width=155, height=70)

#CRIA BOTAO SAIR E CHAMA VARIAVEL
#bte = Button(login, text="VOLTAR", font=("impact", 11, "bold"), fg="black", width=6, height=2, background="#CDC9C9", command=Fechar_Login)
#bte.place(x=700, y=340)

    
mainloop()

