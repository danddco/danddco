import sqlite3  # o usa mysql.connector si estás con MySQL

# Conexión a la base de datos
conn = sqlite3.connect("D:\\PyThon\\BD\\Dante.db")
cursor = conn.cursor()

# Ejecutar la consulta
cursor.execute("SELECT id_p, producto_p, cantidad_p, precio_venta_p, fecha_p FROM productos ORDER BY producto_p")
rows = cursor.fetchall()

# Crear tabla HTML
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Productos</title>
    <style>
        table { border-collapse: collapse; width: 60%; margin: auto; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        body { font-family: Arial, sans-serif; padding: 20px; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Inventario de Productos</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Precio Venta</th>
            <th>Fecha</th>
        </tr>
"""

# Agregar filas a la tabla
for row in rows:
    html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"

# Cerrar HTML
html += """
    </table>
</body>
</html>
"""

# Guardar como archivo HTML
with open("existencias.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Página web generada como existencias.html")
