from cmath import cos, sin, tan
from lib2to3.pgen2 import token
from operator import index
from tkinter import messagebox
from Clases import Error
from Clases import Token
import math
# alfabeto = {letras}, {numeros}, <, >, /, ., =, [, ], {colores}, {signos}


class Scanner:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.signos = ['?', '¿', '¡', '!', '.', ',', ':', ';']
        self.contador = 0

    def analyze(self, contenido):
        self.listaTokens = []
        self.listaErrores = []
        try:
            if (self.listaTokens and self.listaErrores) != None:
                contenido += '&'
                line = 1
                column = 1
                indexx = 0
                buffer = ""
                state = 'q_0'
                while indexx < len(contenido):
                    caracter = contenido[indexx]
                    if state == 'q_0':
                        if caracter == '!':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_EXCLAMACION', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '<':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_MENOR_QUE_AB', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '>':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_MAYOR_QUE_CI', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '-':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_GUION', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == ';':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_PUNTOYCOMA', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == ',':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_COMA', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '(':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_PARENTESIS_AB', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == ')':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_PARENTESIS_CI', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '.':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_PUNTO', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter .isalpha() and (not caracter.isdigit()):
                            buffer = caracter
                            column += 1
                            state = 'q_1'
                        elif caracter == '\n':
                            column = 1
                            line += 1
                        elif caracter == ' ':
                            column += 1
                        elif caracter == '\t':
                            column += 1
                        elif caracter == '\r':
                            pass
                        elif caracter.isdigit():
                            buffer = caracter
                            column += 1
                            state = 'q_2'
                        elif caracter== '/' and (contenido[indexx+1]=='*'):
                            buffer = caracter
                            column += 1
                            state = 'q_3'
                        elif caracter== '/' and (contenido[indexx+1]=='/'):
                            buffer = caracter
                            column += 1
                            state = 'q_4'
                        elif caracter== '"':
                            buffer = caracter
                            column += 1
                            state = 'q_5'
                        elif caracter == '&':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, '¡FINISH HIM!', line, column))
                            buffer = ''
                            state = 'q_0'
                            print('Análisis Exitoso')
                        else:
                            self.listaErrores.append(Error(
                                caracter, "ERROR", 'No es reconocido Como Token de Este Lenguaje', line, column))
                            buffer = ''
                            column += 1
                    elif state == 'q_1':
                        if caracter.isalpha() and (not caracter.isdigit()):
                            buffer += caracter
                            column += 1
                            state = 'q_1'
                        else:
                            if buffer.upper() == 'CONTROLES':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_CONTROLES_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'PROPIEDADES':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_PROPIEDADES_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'COLOCACION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_COLOCACION_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETANCHO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETANCHO_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETALTO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETALTO_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETCOLORFONDO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETCOLORFONDO_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETTEXTO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETTEXTO_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'ADD':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_ADD_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETCOLORLETRA':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETCOLORLETRA_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SETPOSICION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SETPOSICION_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'CONTENEDOR':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_CONTENEDOR_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'BOTON':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_BOTON_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'CLAVE':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_CLAVE_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'ETIQUETA':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_ETIQUETA_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'TEXTO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_TEXTO_R', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            else:
                                self.listaErrores.append(Error(
                                    buffer,  'ERROR', "No Es Reconocido Como Token de Este Lenguaje", line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                    elif state == 'q_2':
                        if caracter.isdigit():
                            buffer += caracter
                            column += 1
                            state = 'q_2'
                        else:
                            self.listaTokens.append(
                                Token(buffer, 'TK_ENTERO', line, column))
                            buffer = ''
                            indexx -= 1
                            state = 'q_0'
                    elif state == 'q_3':
                        if caracter== '*':
                            buffer+=caracter
                            column+=1
                            if contenido[indexx+1]=='/':
                                buffer+=contenido[indexx+1]
                                column+=1
                                self.listaTokens.append(
                                Token(buffer, 'TK_COMENT_MULTI', line, column))
                                buffer=''
                                indexx+=1
                                state='q_0'
                        elif caracter =='\n':
                            buffer+=caracter
                            column+=1
                            line+=1
                        else:
                            buffer+=caracter
                            column+=1
                            state='q_3'
                    elif state == 'q_4':
                        if  caracter=='\n':
                            buffer+=caracter
                            column+=1
                            self.listaTokens.append(
                            Token(buffer, 'TK_COMENT_SIMPLE', line, column))
                            buffer=''
                            state='q_0'
                            indexx-=1
                        else:
                            buffer+=caracter
                            column+=1
                            state='q_4'
                    elif state == 'q_5':
                        if  caracter=='"':
                            buffer+=caracter
                            column+=1
                            self.listaTokens.append(
                            Token(buffer, 'TK_CADENA', line, column))
                            buffer=''
                            state='q_0'
                        else:
                            buffer+=caracter
                            column+=1
                            state='q_5'
                    indexx += 1
            else:
                print("No se puede analizar")
        except:
            pass

    def printScannergg(self):
        print("__________ T O K E N S __________")
        for token in self.listaTokens:
            token.getInfoTokens()
        print()
        print("__________ E R R O R E S __________")
        for token in self.listaErrores:
            token.getInfoErrores()
        print()

    def printList(self):
        print("_________________L I S T  A T O K E N S________________")
        for token in self.listaTokens:
            token.getToken()
        print()
