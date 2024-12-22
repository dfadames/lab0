# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import pymysql
from pymysql import MySQLError 

app = Flask(__name__)

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='2765',
        database='laboratorio0'
    )



@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html")


# Route for municipios.html
@app.route("/api/persona", methods=["GET"])
def datos_personas():
    # Conectar a la base de datos y ejecutar la consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM persona")
    
    # Obtener los nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]
    
    # Obtener todos los registros y convertirlos a un diccionario

    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Imprimir en consola (para depuración)
    print("Datos obtenidos de la base de datos:")
    for dato in datos:
        print(dato)
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
    # Devolver los datos en formato JSON
    return jsonify(datos)

@app.route("/municipios.html")
def municipios():
    return render_template("municipios.html")
@app.route("/api/municipio", methods=["GET"])
def datos_municipios():
    # Conectar a la base de datos y ejecutar la consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM MUNICIPIO")
    
    # Obtener los nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]
    
    # Obtener todos los registros y convertirlos a un diccionario
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Imprimir en consola (para depuración)
    print("Datos obtenidos de la base de datos:")
    for dato in datos:
        print(dato)
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
    # Devolver los datos en formato JSON
    return jsonify(datos)

@app.route("/vehiculos.html", methods=["GET"])
def pagina_vehiculos():
    return render_template("vehiculos.html")

@app.route("/api/vehiculo", methods=["GET"])
def datos_vehiculos():
    # Conectar a la base de datos y ejecutar la consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM VEHICULO")
    
    # Obtener los nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]
    
    # Obtener todos los registros y convertirlos a un diccionario
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Imprimir en consola (para depuración)
    print("Datos obtenidos de la base de datos:")
    for dato in datos:
        print(dato)
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
    # Devolver los datos en formato JSON
    return jsonify(datos)

# Route for viviendas.html
@app.route("/viviendas.html")
def viviendas():
    return render_template("viviendas.html")
@app.route("/api/vivienda", methods=["GET"])
def datos_viviendas():
    # Conectar a la base de datos y ejecutar la consulta
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM VIVIENDA")
    
    # Obtener los nombres de las columnas
    columnas = [columna[0] for columna in cursor.description]
    
    # Obtener todos los registros y convertirlos a un diccionario
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    
    # Imprimir en consola (para depuración)
    print("Datos obtenidos de la base de datos:")
    for dato in datos:
        print(dato)
    
    # Cerrar la conexión
    cursor.close()
    conexion.close()
    
    # Devolver los datos en formato JSON
    return jsonify(datos)

# Route for desde.html
@app.route("/desde.html")
def desde():
    return render_template("desde.html")

# Ruta para departamento.html
@app.route("/departamentos.html")
def departamento():
    return render_template("departamentos.html")

# Ruta para api de departamento
@app.route("/api/departamento", methods=["GET"])
def datos_departamento():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM DEPARTAMENTO")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

# Ruta para persona_trabajo.html
@app.route("/trabajosPersonas.html")
def persona_trabajo():
    return render_template("trabajosPersonas.html")

# Ruta para api de persona_trabajo
@app.route("/api/persona_trabajo", methods=["GET"])
def datos_persona_trabajo():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PERSONA_TRABAJO")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

# Ruta para persona_vivienda.html
@app.route("/viviendasPersonas.html")
def persona_vivienda():
    return render_template("viviendasPersonas.html")

# Ruta para api de persona_vivienda
@app.route("/api/persona_vivienda", methods=["GET"])
def datos_persona_vivienda():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PERSONA_VIVIENDA")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

# Ruta para soat.html
@app.route("/soat.html")
def soat():
    return render_template("soat.html")

# Ruta para api de soat
@app.route("/api/soat", methods=["GET"])
def datos_soat():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM SOAT")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

# Ruta para tecnomecanica.html
@app.route("/tecnomecanica.html")
def tecnomecanica():
    return render_template("tecnomecanica.html")

# Ruta para api de tecnomecanica
@app.route("/api/tecnomecanica", methods=["GET"])
def datos_tecnomecanica():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TECNOMECANICA")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

# Ruta para trabajo.html
@app.route("/trabajos.html")
def trabajo():
    return render_template("trabajos.html")

# Ruta para api de trabajo
@app.route("/api/trabajo", methods=["GET"])
def datos_trabajo():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TRABAJO")
    columnas = [columna[0] for columna in cursor.description]
    datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return jsonify(datos)

@app.route("/agregardepartamento", methods=["POST"])
def insertar_departamento():
    # Obtener datos del formulario
    nombre_departamento = request.form["nombreDepartamento"]
    codigo_departamento = request.form["codigoDepartamento"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO DEPARTAMENTO (
                    nombre_departamento, codigo_departamento
                )
                VALUES (%s, %s)
            """
            valores = (nombre_departamento, codigo_departamento)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/departamentos.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
    
@app.route("/actualizardepartamento", methods=["POST"])
def actualizar_departamento():
    # Obtener datos del formulario
    id_departamento = request.form["id"]  # Cambiamos a "id" como identificador

    nombre_departamento = request.form["nombre_departamento"]
    codigo_departamento = request.form["codigo_departamento"]
    print(id_departamento)
    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE DEPARTAMENTO
                SET nombre_departamento = %s,
                    codigo_departamento = %s
                WHERE id = %s
            """
            valores = (nombre_departamento,codigo_departamento, id_departamento)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/departamentos.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500




@app.route("/borrardepartamento", methods=["POST"])
def eliminar_departamento():
    # Obtener el id del departamento desde el JSON enviado
    data = request.json
    id_departamento = data.get("id")
    print(id_departamento)
    
    try:
        # Eliminar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                DELETE FROM DEPARTAMENTO
                WHERE id = %s
            """
            cursor.execute(query, (id_departamento,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Departamento eliminado correctamente."})

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500




@app.route("/agregarvivienda", methods=["POST"])
def insertar_vivienda():
    # Obtener datos del formulario
    id_municipio = request.form["idMunicipio"]  # Modificado para tomar el ID del municipio
    barrio = request.form["barrio"]
    direccion = request.form["direccion"]
    estrato = request.form["estrato"]
    pisos = request.form["numeroDePisos"]  # Corregido para usar el nombre del campo adecuado
    tipo_vivienda = request.form["tipoDeVivienda"]  # Corregido para usar el nombre del campo adecuado
    descripcion = request.form["descripcion"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO VIVIENDA (
                    id_municipio, barrio, direccion, estrato, pisos, tipo_vivienda, descripcion
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (id_municipio, barrio, direccion, estrato, pisos, tipo_vivienda, descripcion)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/viviendas.html")
    
    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500


@app.route("/actualizarvivienda", methods=["POST"])
def actualizar_vivienda():
    # Obtener datos del formulario
    id_vivienda = request.form["id"]
    barrio = request.form["barrio"]
    direccion = request.form["direccion"]
    estrato = request.form["estrato"]
    pisos = request.form["pisos"]
    tipo_vivienda = request.form["tipo_vivienda"]
    descripcion = request.form["descripcion"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE VIVIENDA
                SET barrio = %s,
                    direccion = %s,
                    estrato = %s,
                    pisos = %s,
                    tipo_vivienda = %s,
                    descripcion = %s
                WHERE id = %s
            """
            valores = (barrio, direccion, estrato, pisos, tipo_vivienda, descripcion, id_vivienda)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/viviendas.html")
    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
    
@app.route("/borrarvivienda", methods=["POST"])
def eliminar_vivienda():
    # Obtener el ID desde el JSON enviado
    data = request.json
    id_vivienda = data.get("id")

    try:
        # Conectar y eliminar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM VIVIENDA WHERE id = %s"
            cursor.execute(query, (id_vivienda,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Vivienda eliminada correctamente."})

    except MySQLError as e:
        # Manejar errores y devolver un mensaje de error en JSON
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/agregarsoat", methods=["POST"])
def insertar_soat():
    # Obtener datos del formulario
    id_vehiculo = request.form["idVehiculo"]  # Modificado para tomar el ID del vehículo
    fecha_emision = request.form["fechaEmisionSoat"]
    fecha_vencimiento = request.form["fechaVencimientoSoat"]
    aseguradora = request.form["aseguradoraSoat"]
    valor = request.form["valorSoat"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO SOAT (
                    id_vehiculo, fecha_emision, fecha_vencimiento, aseguradora, valor
                )
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (id_vehiculo, fecha_emision, fecha_vencimiento, aseguradora, valor)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/soat.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/actualizarsoat", methods=["POST"])
def actualizar_soat():
    # Obtener datos del formulario
    id_soat = request.form["id"]
    fecha_emision = request.form["fecha_emision"]
    fecha_vencimiento = request.form["fecha_vencimiento"]
    aseguradora = request.form["aseguradora"]
    valor = request.form["valor"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE SOAT
                SET fecha_emision = %s,
                    fecha_vencimiento = %s,
                    aseguradora = %s,
                    valor = %s
                WHERE id = %s
            """
            valores = (fecha_emision, fecha_vencimiento, aseguradora, valor, id_soat)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/soat.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
@app.route("/borrarsoat", methods=["POST"])
def eliminar_soat():
    # Obtener datos desde el JSON enviado
    data = request.json
    id_soat = data.get("id")

    try:
        # Eliminar datos de la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM SOAT WHERE id = %s"
            cursor.execute(query, (id_soat,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "SOAT eliminado correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500




@app.route("/agregartecnomecanica", methods=["POST"])
def insertar_tecnomecanica():
    # Obtener datos del formulario
    fecha_revision = request.form["fechaEmisionTecno"]
    fecha_vencimiento = request.form["fechaVencimientoTecno"]
    resultado = request.form["resultadoTecno"]
    valor = request.form["valorTecno"]
    centro_revision = request.form["cdaTecno"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO TECNOMECANICA (
                    fecha_revision, fecha_vencimiento, resultado, valor, centro_revision
                )
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (fecha_revision, fecha_vencimiento, resultado, valor, centro_revision)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/tecnomecanica.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
    
@app.route("/actualizartecnomecanica", methods=["POST"])
def actualizar_tecnomecanica():
    # Obtener datos del formulario
    id_tecnomecanica = request.form["id"]  # Cambiamos a "id" como identificador
    fecha_vencimiento = request.form["fecha_vencimiento"]
    resultado = request.form["resultado"]
    valor = request.form["valor"]
    centro_revision = request.form["centro_revision"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE TECNOMECANICA
                SET 
                    fecha_vencimiento = %s,
                    resultado = %s,
                    valor = %s,
                    centro_revision = %s
                WHERE id = %s
            """
            valores = (fecha_vencimiento, resultado, valor, centro_revision, id_tecnomecanica)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/tecnomecanica.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/borrartecnomecanica", methods=["POST"])
def eliminar_tecnomecanica():
    # Obtener el ID desde el JSON enviado
    data = request.json
    id_tecnomecanica = data.get("id")

    try:
        # Eliminar el registro en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM TECNOMECANICA WHERE id = %s"
            cursor.execute(query, (id_tecnomecanica,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Técnico-mecánica eliminada correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500




@app.route("/agregartrabajo", methods=["POST"])
def insertar_trabajo():
    # Obtener datos del formulario
    nombre_trabajo = request.form["nombreTrabajo"]
    municipio_trabajo = request.form["idMunicipioTrabajo"]
    oficio = request.form["oficio"]
    salario = request.form["salario"]
    tipo_contrato = request.form["tipoDeContrato"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO TRABAJO (
                    nombre_trabajo,id_municipio_trabajo, oficio, salario, tipo_contrato
                )
                VALUES (%s, %s, %s, %s)
            """
            valores = (nombre_trabajo,municipio_trabajo, oficio, salario, tipo_contrato)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/trabajos.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
    
@app.route("/actualizartrabajo", methods=["POST"])
def actualizar_trabajo():
    # Obtener datos del formulario
    id_trabajo = request.form["id"]  # Cambiamos a "id" como identificador
    municipio_trabajo = request.form["id_municipio_trabajo"]
    oficio = request.form["oficio"]
    salario = request.form["salario"]
    tipo_contrato = request.form["tipo_contrato"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE TRABAJO
                SET 
                    id_municipio_trabajo = %s,
                    oficio = %s,
                    salario = %s,
                    tipo_contrato = %s
                WHERE id = %s
            """
            valores = (municipio_trabajo,oficio, salario, tipo_contrato, id_trabajo)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/trabajos.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500


    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
@app.route("/borrartrabajo", methods=["POST"])
def eliminar_trabajo():
    # Obtener el ID desde el JSON enviado
    data = request.json
    id_trabajo = data.get("id")

    try:
        # Eliminar el registro en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM TRABAJO WHERE id = %s"
            cursor.execute(query, (id_trabajo,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Trabajo eliminado correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500



@app.route("/agregarmunicipio", methods=["POST"])
def insertar_municipio():
    # Obtener datos del formulario
    id_departamento = request.form["idDepartamento"]  # Cambié "idDepartamento" según el HTML
    nombre_municipio = request.form["nombreMunicipio"]  # Cambié "nombre_municipio" para coincidir
    codigo_municipio = request.form["codigoMunicipio"]
    area = request.form["areaMunicipio"]  # Cambié "area" a "areaMunicipio"

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO MUNICIPIO (
                    id_departamento, nombre_municipio,codigo_municipio, area
                )
                VALUES (%s, %s, %s, %s)
            """
            valores = (id_departamento, nombre_municipio,codigo_municipio, area)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/municipios.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/actualizarmunicipio", methods=["POST"])
def actualizar_municipio():
    # Obtener datos del formulario
    id_municipio = request.form["id"]  # Cambiamos a "id" como identificador
    nombre_municipio = request.form["nombre_municipio"]
    codigo_municipio = request.form["codigo_municipio"]
    area = request.form["area"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE MUNICIPIO
                SET 
                    nombre_municipio = %s,
                    codigo_municipio = %s,
                    area = %s
                WHERE id = %s
            """
            valores = (nombre_municipio,codigo_municipio,area, id_municipio)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/municipios.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

    
@app.route("/borrarmunicipio", methods=["POST"])
def eliminar_municipio():
    # Obtener el código del municipio desde el JSON enviado
    data = request.json
    id_municipio = data.get("id")

    try:
        # Eliminar el municipio en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM MUNICIPIO WHERE id = %s"
            cursor.execute(query, (id_municipio,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Municipio eliminado correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500




@app.route("/agregarvehiculo", methods=["POST"])
def insertar_vehiculo():
    # Obtener datos del formulario
    id_dueno = request.form["idDueno"]
    expedido = request.form["expedido"]
    nombre_vehiculo = request.form["nombreVehiculo"]
    marca_vehiculo = request.form["marcaVehiculo"]
    tipo_vehiculo = request.form["tipoVehiculo"]
    color_vehiculo = request.form["colorVehiculo"]
    placa_vehiculo = request.form["placaVehiculo"]
    anio_vehiculo = request.form["anioVehiculo"]
    no_serie_vehiculo = request.form["noSerievehiculo"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO VEHICULO (
                    id_dueno, expedido, nombre, marca, tipo, 
                    color, placa, anio_fabricacion, numero_serie
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                id_dueno, expedido, nombre_vehiculo, marca_vehiculo, 
                tipo_vehiculo, color_vehiculo, placa_vehiculo, 
                anio_vehiculo, no_serie_vehiculo
            )
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal
        return redirect("/vehiculos.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/actualizarvehiculo", methods=["POST"])
def actualizar_vehiculo():
    # Obtener datos del formulario
    id_vehiculo = request.form["id"]  # Cambiamos a "id" como identificador
    nombre = request.form["nombre"]
    marca = request.form["marca"]
    tipo = request.form["tipo"]
    color = request.form["color"]
    anio_fabricacion = request.form["anio_fabricacion"]
    numero_serie = request.form["numero_serie"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE VEHICULO
                SET 
                    nombre = %s, 
                    marca = %s, 
                    tipo = %s, 
                    color = %s, 
                    anio_fabricacion = %s, 
                    numero_serie = %s
                WHERE id = %s
            """
            valores = (
                nombre, marca, tipo, 
                color, anio_fabricacion, numero_serie, id_vehiculo
            )
            cursor.execute(query, valores)
            conexion.commit()
        
        # Redirigir de vuelta a la página principal
        return redirect("/vehiculos.html")      
    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos del vehículo: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/borrarvehiculo", methods=["POST"])
def eliminar_vehiculo():
    # Obtener el ID desde el JSON enviado
    data = request.json
    id_vehiculo = data.get("id")

    try:
        # Eliminar el vehículo en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM VEHICULO WHERE id = %s"
            cursor.execute(query, (id_vehiculo,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Vehículo eliminado correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos del vehículo: {e}")
        return jsonify({"success": False, "error": str(e)}), 500





@app.route("/agregarpersona", methods=["POST"])
def insertar_persona():
    # Obtener datos del formulario
    cedula = request.form["cedula"]
    p_nombre = request.form["primerNombre"]
    s_nombre = request.form["segundoNombre"]
    p_apellido = request.form["primerApellido"]
    s_apellido = request.form["segundoApellido"]
    fecha_nacimiento = request.form["fechaDeNacimiento"]
    sexo = request.form["sexo"]
    telefono = request.form["telefono"]
    correo = request.form["direccionDeCorreo"]
    estado_civil = request.form["estadoCivil"]
    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO PERSONA (
                    cedula, p_Nombre, s_Nombre, p_Apellido, s_Apellido, 
                    fecha_nacimiento, sexo, telefono, correo, estado_civil
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            print("hola3")
            valores = (cedula, p_nombre, s_nombre, p_apellido, s_apellido, 
                       fecha_nacimiento, sexo, telefono, correo, estado_civil)
            cursor.execute(query, valores)
            conexion.commit()
            print("hola4")
        # Redirigir de vuelta a la página principal
        return redirect("/")
        
    except MySQLError as e:
        print("hola5")
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
@app.route("/actualizarpersona", methods=["POST"])
def actualizar_persona():
    # Obtener datos del formulario
    id_persona = request.form["id"]  # Cambiamos a "id" como identificador
    p_nombre = request.form["p_Nombre"]
    s_nombre = request.form["s_Nombre"]
    p_apellido = request.form["p_Apellido"]
    s_apellido = request.form["s_Apellido"]
    fecha_nacimiento = request.form["fecha_nacimiento"]
    sexo = request.form["sexo"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    estado_civil = request.form["estado_civil"]
    
    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE PERSONA
                SET 
                    p_Nombre = %s, 
                    s_Nombre = %s, 
                    p_Apellido = %s, 
                    s_Apellido = %s, 
                    fecha_nacimiento = %s, 
                    sexo = %s, 
                    telefono = %s, 
                    correo = %s, 
                    estado_civil = %s
                WHERE id = %s
            """
            valores = (
                p_nombre, s_nombre, p_apellido, s_apellido, 
                fecha_nacimiento, sexo, telefono, correo, estado_civil, id_persona
            )
            cursor.execute(query, valores)
            conexion.commit()
        
        # Redirigir de vuelta a la página principal
        return redirect("/")
        
    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500

@app.route("/borrarpersona", methods=["POST"])
def eliminar_persona():
    # Obtener la cédula de la persona desde el JSON enviado
    data = request.json
    id_persona = data.get("id")

    try:
        # Eliminar la persona en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = "DELETE FROM PERSONA WHERE id = %s"
            cursor.execute(query, (id_persona,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Persona eliminada correctamente."})

    except MySQLError as e:
        # Manejar errores y responder con un mensaje de error
        print(f"Error al eliminar datos de la persona: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/insertarpersonatrabajo", methods=["POST"])
def insertar_persona_trabajo():
    # Obtener datos del formulario
    id_persona = request.form["idPersona"]
    id_trabajo = request.form["idTrabajo"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO PERSONA_TRABAJO (
                    id_persona, id_trabajo
                )
                VALUES (%s, %s)
            """
            valores = (id_persona, id_trabajo)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal o a la página que deseas
        return redirect("/trabajosPersonas.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        # Redirigir a la página con un mensaje de error (opcional)
        return jsonify({"error": str(e)}), 500
@app.route("/actualizarpersonatrabajo", methods=["POST"])
def actualizar_persona_trabajo():
    # Obtener datos del formulario
    id_persona = request.form["id_persona"]
    id_trabajo = request.form["id_trabajo"]
    id_registro = request.form["id"]  # Este es el ID único que se usa para identificar el registro

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE PERSONA_TRABAJO
                SET id_persona = %s,
                    id_trabajo = %s
                WHERE id = %s
            """
            valores = (id_persona, id_trabajo, id_registro)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal o la página adecuada
        return redirect("/trabajosPersonas.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/borrarpersonatrabajo", methods=["POST"])
def eliminar_persona_trabajo():
    # Obtener el id del registro desde el JSON enviado
    data = request.json  # Usar request.json para recibir JSON
    id_registro = data.get("id")  # Obtener el ID de la solicitud JSON

    try:
        # Eliminar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                DELETE FROM PERSONA_TRABAJO
                WHERE id = %s
            """
            cursor.execute(query, (id_registro,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Registro eliminado correctamente."})

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/insertarviviendapersona", methods=["POST"])
def insertar_persona_vivienda():
    # Obtener datos del formulario
    id_persona = request.form["idPersona"]
    id_vivienda = request.form["idVivienda"]
    propietario = request.form["propietario"]

    try:
        # Insertar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                INSERT INTO PERSONA_VIVIENDA (
                    id_persona, id_vivienda, propietario
                )
                VALUES (%s, %s, %s)
            """
            valores = (id_persona, id_vivienda, propietario)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal o la página que deseas
        return redirect("/viviendasPersonas.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al insertar datos: {e}")
        return jsonify({"error": str(e)}), 500
@app.route("/actualizarpersonavivienda", methods=["POST"])
def actualizar_persona_vivienda():
    # Obtener datos del formulario
    id_registro = request.form["id"]
    id_persona = request.form["id_persona"]
    id_vivienda = request.form["id_vivienda"]
    propietario = request.form["propietario"]

    try:
        # Actualizar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                UPDATE PERSONA_VIVIENDA
                SET id_persona = %s,
                    id_vivienda = %s,
                    propietario = %s
                WHERE id = %s
            """
            valores = (id_persona, id_vivienda, propietario, id_registro)
            cursor.execute(query, valores)
            conexion.commit()

        # Redirigir de vuelta a la página principal o la página adecuada
        return redirect("/viviendasPersonas.html")

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al actualizar datos: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/borrarpersonavivienda", methods=["POST"])
def eliminar_persona_vivienda():
    # Obtener el id del registro desde el JSON enviado
    data = request.json  # Use request.json to read the JSON payload
    id_registro = data.get("id")  # Extract the ID from the JSON body

    try:
        # Eliminar datos en la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            query = """
                DELETE FROM PERSONA_VIVIENDA
                WHERE id = %s
            """
            cursor.execute(query, (id_registro,))
            conexion.commit()

        # Responder con éxito
        return jsonify({"success": True, "message": "Registro eliminado correctamente."})

    except MySQLError as e:
        # Imprimir el error que devuelve MySQL
        print(f"Error al eliminar datos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)