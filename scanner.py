from cmath import cos, sin, tan
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
                contenido += '$'
                line = 1
                column = 1
                indexx = 0
                buffer = ""
                state = 'q_0'
                while indexx < len(contenido):
                    caracter = contenido[indexx]
                    if state == 'q_0':
                        if caracter == '=':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_IGUAL', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '<':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_MENOR_QUE', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '>':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_MAYOR_QUE', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '/':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_DIAGONAL', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == '[':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_CORCHETE_E', line, column))
                            buffer = ''
                            state = 'q_0'
                        elif caracter == ']':
                            buffer = caracter
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'Tk_CORCHETE_S', line, column))
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
                        elif caracter.isdigit():
                            buffer = caracter
                            column += 1
                            state = 'q_2'
                        # elif caracter == '"':
                        #     buffer = caracter
                        #     column += 1
                        #     state = 'q_4'
                        elif caracter in self.colores:
                            buffer = caracter
                            column += 1
                            state = 'q_5'
                        elif caracter == '$':
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
                            if buffer.upper() == 'TIPO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_TIPO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'OPERACION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_OPERACION', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'OPERACIONES':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_OPERACIONES', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'COMPLEJAS':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_COMPLEJAS', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SIMPLES':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SIMPLES', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'NUMERO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_NUMERO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'TEXTO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_R_TEXTO_', line, column))
                                buffer = ''
                                if contenido[indexx] == '>' and contenido[indexx-6] != '/':
                                    buffer += caracter
                                    self.listaTokens.append(
                                        Token(buffer, 'TK_MAYOR_QUE', line, column))
                                    buffer = ''
                                indexx += 1
                                state = 'q_4'
                            elif buffer.upper() == 'FUNCION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_FUNCION', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'TITULO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_TITULO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'DESCRIPCION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_DESCRIPCION', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'CONTENIDO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_CONTENIDO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'ESTILO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_ESTILO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'COLOR':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_R_COLOR_', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'TAMANIO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_TAMANIO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer.upper() == 'SUMA':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SUMA', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'RESTA':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_RESTA', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'MULTIPLICACION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_MULTIPLICACION', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'DIVISION':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_DIVISION', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'POTENCIA':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_POTENCIA', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'RAIZ':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_RAIZ', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'INVERSO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_INVERSO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'SENO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_SENO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'COSENO':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_COSENO', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'TANGENTE':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_TANGENTE', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'MOD':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_MOD', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer == 'ESCRIBIR':
                                self.listaTokens.append(
                                    Token(buffer, 'TK_ESCRIBIR', line, column))
                                buffer = ''
                                state = 'q_0'
                                indexx -= 1
                            elif buffer in self.colores:
                                self.listaTokens.append(
                                    Token(buffer, 'TK_COLOR', line, column))
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
                        elif caracter == '.':
                            buffer += caracter
                            column += 1
                            state = 'q_3'
                        else:
                            self.listaTokens.append(
                                Token(buffer, 'TK_ENTERO', line, column))
                            buffer = ''
                            indexx -= 1
                            state = 'q_0'
                    elif state == 'q_3':
                        if caracter.isdigit():
                            buffer += caracter
                            column += 1
                            state = 'q_3'
                        else:
                            self.listaTokens.append(
                                Token(buffer, 'TK_DECIMAL', line, column))
                            buffer = ''
                            indexx -= 1
                            state = 'q_0'
                    elif state == 'q_4':
                        if caracter == '<':
                            column += 1
                            self.listaTokens.append(
                                Token(buffer, 'TK_CONTENIDO_TXT', line, column))
                            buffer = ''
                            state = 'q_0'
                            indexx -= 1
                        elif caracter == '\n':
                            column = 1
                            line += 1
                        else:
                            buffer += caracter
                            column += 1
                            state = 'q_4'
                    indexx += 1
                print("Operaicone: " + str(self.contador))
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
