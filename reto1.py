tarifa = 0

dia = input('Digite el día de la semana: ').lower()

if dia == 'lunes' or dia == 'martes' or dia == 'miercoles':
    tarifa = 2.00
elif dia == 'jueves' or dia == 'viernes':
    tarifa = 2.50
elif dia == 'sabado' or dia == 'domingo':
    tarifa = 3.00
else:
    print ('Error')


if tarifa != 0:
    
    horas = int(input('Digite las horas: '))
    minutos = int(input('Digite los minutos: '))
    
    if horas < 0 or minutos < 0:
        print('Error')
    else:
        
        if minutos >= 5:
            horas += 1  
        
        costo = horas * tarifa
        
        print('El costo es: $',costo)