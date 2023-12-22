import tkinter as tk
import os
from PIL import Image, ImageTk
import serial.tools.list_ports
import continuous_threading
import datetime
import numpy

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import drawnow
import pandas as pd

import imagens as imgs


###### FONTES

fonteTitulo = ("Impact", 20, "bold")
fonteBotao = ("Oswald", 20)
fonteTexto = ("Oswald", 12)


# Janela Principal

janela = tk.Tk()
janela.geometry("1920x950")
janela.title("Telemetria - Imperador")
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)



###### TELAS DO SISTEMA

frameConexao = tkinter.Frame(janela)
frameConexao.grid_columnconfigure(0, weight=1)
frameConexao.grid(row=0, column=1, sticky="nsew")

frameTelemetria = tkinter.Frame(janela)
frameTelemetria.grid_rowconfigure(1, weight=1)

frameLog = tkinter.Frame(janela)
frameLog.grid_columnconfigure(0, weight=1)

frameNavegacao = tkinter.Frame(janela)
frameNavegacao.grid(row=0, column=0, sticky="nsew")
frameNavegacao.grid_rowconfigure(5, weight=1)


###### Frame de Conexão

statusConexaoLabel = tkinter.Label(frameConexao, bg="red" if statusConexao == False else "green", text="Desconectado" if statusConexao == False else "Conectado", font=fonteBotao)
statusConexaoLabel.grid(row=0, column=0, padx=20, pady=20)

baudRateLabel = tkinter.Label(frameConexao, text="Baud-Rate", font=fonteBotao)
baudRateLabel.grid(row=1, column=0, padx=20, pady=10)


listaBaudRate = ["9600", "38400", "115200"]
varBaudRate = tkinter.StringVar(frameConexao)
varBaudRate.set(listaBaudRate[0])

baudRateSelector = tkinter.OptionMenu(frameConexao, varBaudRate, *listaBaudRate, command=eventoSelectBaudRate)
baudRateSelector.grid(row = 2, column=0, padx=20, pady=10)

portaCOMLabel = tkinter.Label(frameConexao, text="Porta COM", font=fonteBotao)
portaCOMLabel.grid(row=3, column=0, padx=20, pady=0)

varPortaCOM = tkinter.StringVar()
varPortaCOM.set("COM3")

portaCOMSelector = tkinter.OptionMenu(frameConexao, varPortaCOM, *portList, command=eventoSelectCOM)
portaCOMSelector.grid(row=4, column=0, padx=20, pady=10)

conectarBotao = tkinter.Button(frameConexao, text="Conectar" if statusConexao == False else "Desconectar", image = imagemConectar, command=eventoBotaoConectar)
conectarBotao.grid(row=5, column=0, padx=20, pady=10)

textoRecebido = tkinter.Text(frameConexao, state="normal", font=fonteTexto, width=50, height=10)
textoRecebido.grid(row=6, column=0, padx=20, pady=10)

apagarBotao = tkinter.Button(frameConexao, text="Apagar", image=imagemBorracha, command=eventoBotaoApagar)
apagarBotao.grid(row=7, column=0, padx=20, pady=0)

textoComando = tkinter.Text(frameConexao, state = "disabled" if statusConexao == False else "normal", font=fonteTexto, width=50, height=1)
textoComando.grid(row=8, column=0, padx=20, pady=10)

enviarBotao = tkinter.Button(frameConexao, text="Enviar", state= "disabled" if statusConexao == False else "normal", command=eventoBotaoEnviar)
enviarBotao.grid(row=9, column=0, padx=20, pady=0)




###### FRAME DE TELEMETRIA

frameTelemetriaSuperior = tkinter.Frame(frameTelemetria)
frameTelemetriaSuperior.grid_columnconfigure(1, weight=2)
frameTelemetriaSuperior.grid(row=0, column=0, sticky="nsew")

frameTelemetriaInferior = tkinter.Frame(frameTelemetria)
frameTelemetriaInferior.grid_columnconfigure(4, weight=1)
frameTelemetriaInferior.grid_rowconfigure(2, weight=1)
frameTelemetriaInferior.grid(row=1, column=0, sticky="nsew")

frameTelemetriaEsquerdo = tkinter.Frame(frameTelemetriaSuperior)
frameTelemetriaEsquerdo.grid_columnconfigure(0, weight=1)
frameTelemetriaEsquerdo.grid(row=0, column=0, sticky="nsew")

frameTelemetriaDireito = tkinter.Frame(frameTelemetriaSuperior)
frameTelemetriaDireito.grid_columnconfigure(0, weight=1)
frameTelemetriaDireito.grid(row=0, column=1, sticky="nsew")

frameAceleracao = tkinter.Frame(frameTelemetriaInferior)
frameAceleracao.grid_rowconfigure(2, weight=1)
frameAceleracao.grid(row=0, column=0, sticky="nsew")

frameAngulo = tkinter.Frame(frameTelemetriaInferior)
frameAngulo.grid_rowconfigure(2, weight=1)
frameAngulo.grid(row=1, column=0, sticky="nsew")

###########

velocidadeLabel = tkinter.Label(frameTelemetriaEsquerdo, text="Velocidade: 0 km/h", font=fonteTitulo, image=imagemVelocidade, compound="top")
velocidadeLabel.grid(row=0, column=0, padx=20, pady=20)

rpmLabel = tkinter.Label(frameTelemetriaEsquerdo, text="RPM: 0", font=fonteTitulo, image=imagemRpm, compound="top")
rpmLabel.grid(row=1, column=0, padx=20, pady=5)

rpmProgressBar = ttk.Progressbar(frameTelemetriaEsquerdo, orient="horizontal", length=200)
rpmProgressBar.grid(column=0, row=2, padx=10, pady=0)

temperaturaLabel = tkinter.Label(frameTelemetriaEsquerdo, text="Temperatura: 0 ºC", font=fonteTitulo, image=imagemTemperatura, compound="top")
temperaturaLabel.grid(row=3, column=0, padx=20, pady=20)

temperaturaAviso = tkinter.Label(frameTelemetriaEsquerdo, text="OK", font=fonteTitulo, fg="green")
temperaturaAviso.grid(row=4, column=0, padx=20, pady=0)

bateriaLabel = tkinter.Label(frameTelemetriaEsquerdo, text="Bateria: 0.0 V", font=fonteTitulo, image=imagemBateria, compound="top")
bateriaLabel.grid(row=5, column=0, padx=20, pady=20)

bateriaAviso = tkinter.Label(frameTelemetriaEsquerdo, text="OK", font=fonteTitulo, fg="green")
bateriaAviso.grid(row=6, column=0, padx=20, pady=0)

freioLabel = tkinter.Label(frameTelemetriaEsquerdo, text=("   Freio: Desativado"), font=fonteTitulo, image=imagemFreio, compound="left")
freioLabel.grid(row=7, column=0, padx=20, pady=50)

################

aceleracaoxLabel = tkinter.Label(frameTelemetriaInferior, text=("Aceleração X: " + str(aceleracaoX) + " G"), font=fonteTitulo, compound="left")
aceleracaoxLabel.grid(row=0, column=0, padx=20, pady=20)

aceleracaoYLabel = tkinter.Label(frameTelemetriaInferior, text=("Aceleração Y: " + str(aceleracaoY) + " G"), font=fonteTitulo, compound="left")
aceleracaoYLabel.grid(row=0, column=1, padx=20, pady=20)

aceleracaoZLabel = tkinter.Label(frameTelemetriaInferior, text=("Aceleração Z: " + str(aceleracaoZ) + " G"), font=fonteTitulo, compound="left")
aceleracaoZLabel.grid(row=0, column=2, padx=20, pady=20)

anguloXLabel = tkinter.Label(frameTelemetriaInferior, text=("Ângulo X: " + str(anguloX) + "º"), font=fonteTitulo, compound="left")
anguloXLabel.grid(row=1, column=0, padx=20, pady=20)

anguloYLabel = tkinter.Label(frameTelemetriaInferior, text=("Ângulo Y: " + str(anguloY) + "º"), font=fonteTitulo, compound="left")
anguloYLabel.grid(row=1, column=1, padx=20, pady=20)

anguloZLabel = tkinter.Label(frameTelemetriaInferior, text=("Ângulo Z: " + str(anguloZ) + "º"), font=fonteTitulo, compound="left")
anguloZLabel.grid(row=1, column=2, padx=20, pady=20)

velGPSLabel = tkinter.Label(frameTelemetriaInferior, text=("Velocidade GPS: " + str(velocidadeGPS) + " km/h"), font=fonteTitulo, compound="left")
velGPSLabel.grid(row=0, column=3, padx=20, pady=20)

botaoBox = tkinter.Button(frameTelemetriaInferior, text="Box Box", font=fonteTitulo, command=eventoBotaoBox)



###### Frame Log

botaoExportar = tkinter.Button(frameLog, text="Exportar para Excel", command=eventoExportarExcel)
botaoExportar.grid(row=0, column=0, padx=50, pady=100, sticky="we")



