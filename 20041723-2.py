# Archivo2: 20041723-2.py

# Definir las VLANs según el diagrama de referencia
switch1_vlans_diagrama = [99, 10, 100, 30]
switch2_vlans_diagrama = [99, 40, 50, 60]

# Definir las VLANs creadas en los switches
switch1_vlans_creadas = [10,20,30]  # Aquí debes ingresar las VLANs creadas en el switch1
switch2_vlans_creadas = [40,50.60]  # Aquí debes ingresar las VLANs creadas en el switch2

# Comparar las VLANs
def comparar_vlans(switch, vlans_diagrama, vlans_creadas):
    if vlans_diagrama[0] == vlans_creadas[0]:
        print(f"Para el {switch}, las native vlans son iguales y cumplen con el requerimiento.")
    else:
        print(f"Para el {switch}, las native vlans son diferentes y no cumplen con el requerimiento.")

    if set(vlans_diagrama[1:]) == set(vlans_creadas[1:]):
        print(f"Para el {switch}, las vlans creadas son iguales y cumplen con el requerimiento.")
    else:
        print(f"Para el {switch}, las vlans creadas son diferentes y no cumplen con el requerimiento.")

# Ejecutar la comparación de VLANs
comparar_vlans("switch1", switch1_vlans_diagrama, switch1_vlans_creadas)
comparar_vlans("switch2", switch2_vlans_diagrama, switch2_vlans_creadas)