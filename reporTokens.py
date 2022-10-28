import os
contenido = ""


def Inicio():
    global contenido
    contenido += """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="shortcut icon" href="ico.png">
    <link rel="stylesheet" href="style.css">
    <title>Reporte de Errores</title>
    <script src="https://kit.fontawesome.com/eb496ab1a0.js" crossorigin="anonymous"></script>
</head>
<body>
    <div class="text-dark" style="background-color:#df2fb9">
        <div class="container px-4 text-center ">
            <div class="row gx-5">
                <div class="col">
                    <div style="background-color:#df2fb9">
                        <center>
                            <img src="ico.png" width="150" height="150">
                            <div style="background-color:#df2fb9">
                                <h1>WebIDE-Editor</h1>
                            </div>
                        </center>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="p-3 mb-2  text-dark" style="background-color:#8408f8">
        <div class="container  text-center">
            <div class="row gx-5">
                <div class="col">
                    <div class="p-3 mb-2 text-white" style="background-color:#8408f8">
                        <h1>
                            <center>Reporte de Errores</center>
                        </h1>
                    </div>
                </div>
            </div>
        </div>
    </div>"""


def tablaer(Errores):
    global contenido
    contenido += """<table class="table table-dark table-hover table-bordered">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Tipo de Error</th>
      <th scope="col">Caracter</th>
      <th scope="col">Descripcion</th>
      <th scope="col">Linea</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>"""
    contador = 1
    for error in Errores:
        contenido += """
        <tr class="table-info">
      <th scope="row">""" + str(contador) + """</th>
      <th>""" + str('Léxico') + """</th>
      <th>""" + str(error.caracter) + """</th>
      <th>""" + str(error.tipo) + """</th>
      <th>""" + str(error.line) + """</th>
      <th>""" + str(error.column) + """</th>
    </tr>
        """
        contador += 1
    contenido += """</tbody>
</table>"""


def tablate(Tokens):
    global contenido
    contenido += """<div class="p-3 mb-2 text-white" style="background-color:#8408f8;">
        <h1><center>Reporte de Tokens</center></h1>
    </div>"""
    contenido += """<table class="table table-dark table-hover table-bordered">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Tipo de Token</th>
      <th scope="col">Lexema</th>
      <th scope="col">Linea</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>"""
    contador = 1
    for token in Tokens:
        contenido += """
        <tr class="table-info">
      <th scope="row">""" + str(contador) + """</th>
      <th>""" + str(token.tipo) + """</th>
      <th>""" + str(token.lexeme) + """</th>
      <th>""" + str(token.line) + """</th>
      <th>""" + str(token.column) + """</th>
    </tr>
        """
        contador += 1
    contenido += """</tbody>
</table>
<footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img src="xd.ico" alt="Loco WebIDE-Editor">
                    </a>
                </figure>
            </div>
            <div class="box">
                <br>
                <br>
                    <p>Nombre: Eduardo Josué González Cifuentes</p>
                    <p>Carnet: 201900647</p>
                    <p>Curso: Lenguajes Formales y De Programación</p>
                    <p>Secció: A-</p>
                    <p>Catedrático: Inga. Vivian Damaris Campos</p>
                    <p>Auxiliar: Mario Solis</p>
            </div>
            <div class="box">
                <figure>
                    <a href="#">
                        <a href="https://github.com/Lal0gg" target="_blank"> <img src="git.ico" alt="Loco WebIDE-Editor" alt="git-image"
                            width=100%>
                </figure>
            </div>
        </div>
        <div class="grupo-2">
            <small>
                <p>&copy; 2022 <b>WebIDE-Editor</b> "- Todos Los Derechos Reservados"</p>
            </small>
        </div>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>"""


def creararchivo():
    global contenido
    archivo = open('ReporteErr.html', 'w', encoding='utf8')
    archivo.write(contenido)
    archivo.close()
    os.startfile("ReporteErr.html")


def generararchivoE(Errores, Tokens):
    Inicio()
    tablaer(Errores)
    tablate(Tokens)
    creararchivo()
