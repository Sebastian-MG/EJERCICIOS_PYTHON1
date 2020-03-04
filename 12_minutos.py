# 12 Escribir un programa que calcule el número de horas, minutos y segundos que hay en un
# valor x de segundos indicados por el usuario.


segundos = int(input("Digite los segundos" + '\n'))
minutos = segundos//60
rest_seg = segundos % 60   # segundos restantes
horas = (minutos // 60)
rest_min = int(minutos % 60)     # minutos restantes
print("Tiempo: " + str(horas) + " h " + str(rest_min) + " m " + str(rest_seg) + " s ")

