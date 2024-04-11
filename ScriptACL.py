# Solicitar el número de ACL al usuario
acl = int(input("Por favor, ingresa el número de ACL IPv4: "))

# Definir las rangos de ACLs
acl_standard = list(range(1, 100)) + list(range(1300, 2000))
acl_extended = list(range(100, 200)) + list(range(2000, 2700))

# Verificar el tipo de ACL
if acl in acl_standard:
    print("La ACL es Estándar.")
elif acl in acl_extended:
    print("La ACL es Extendida.")
else:
    print("El número no corresponde a una lista de acceso.")