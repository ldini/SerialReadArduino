import serial

def elimina_caracteres(s):
    caracteres = "bnr'"
    s_sin_vocales = ""
    for letra in s:
        if letra not in caracteres:
            s_sin_vocales += letra
    return s_sin_vocales[:len(s_sin_vocales)-2]

PuertoSerie = serial.Serial('COM6', 9600)
while True:
  sArduino = PuertoSerie.readline().__str__()
  print(elimina_caracteres(sArduino))