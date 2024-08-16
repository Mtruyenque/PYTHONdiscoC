# obtener fecha y hora actuales en el sistema
import datetime   #es datetime es un modulo,fechas y horas 

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print(ahora.strftime("%d/%m/%y")) #dia 

print(ahora.strftime("%H:%M:%S")) #hora 

print(ahora.strftime("%d/%m/%/y %H:%M:%S"))