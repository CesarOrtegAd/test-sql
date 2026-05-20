from config.conexion import obtener_conexion

conexion = obtener_conexion()

#consulta para obtener todos los productos
consulta = "SELECT u.cod_usr, u.nom_usuario, d.COD_DPTO, d.NOM_DPTO FROM DEPARTAMENTOS d JOIN usuarios u ON d.depkey = u.depkey"
cursor = conexion.cursor()
cursor.execute(consulta)
resultados = cursor.fetchall()
for producto in resultados:
    print(producto)

if conexion:
    # usar la conexión
    conexion.close()