class Token:
    def __init__(self,lexeme, tipo, line, column):
        self.lexeme = lexeme
        self.tipo = tipo
        self.line = line
        self.column = column 

    def getInfoTokens(self):
        print('_'*40)
        print('Lexema: ', self.lexeme , ' |Tipo: ', self.tipo, 'Linea: ' , self.line, 'Columna: ', self.column)

    def getToken(self):
        print("|", self.lexeme, "|", self.tipo)
    

class Error:
    def __init__(self,caracter, description, tipo, line, column):
        self.caracter = caracter
        self.description = description
        self.tipo = tipo
        self.line = line
        self.column = column

    def getInfoErrores(self):
        print('_'*40)
        print(self.caracter,'Descripcion: ', self.description , '|Tipo: ', self.tipo, 'Linea: ' , self.line, 'Columna: ', self.column)


