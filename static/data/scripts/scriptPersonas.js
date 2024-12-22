// URL del archivo JSON
const jsonUrl = '/api/persona';

// Selecciona el cuerpo de la tabla
const tablaCuerpo = document.getElementById('tablaDatos');

// Función para poblar la tabla
fetch(jsonUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('No se pudo cargar el archivo JSON');
        }
        return response.json();
    })
    .then(data => {
        data.forEach(item => {
            const fila = document.createElement('tr');
            fila.id = `registro${item.id}`;
            fila.innerHTML = `
                <td>${item.id}</td>
                <td>${item.cedula}</td>
                <td>${item.p_Nombre}</td>
                <td>${item.s_Nombre}</td>
                <td>${item.p_Apellido}</td>
                <td>${item.s_Apellido}</td>
                <td>${item.fecha_nacimiento}</td>
                <td>${item.sexo}</td>
                <td>${item.telefono}</td>
                <td>${item.correo}</td>
                <td>${item.estado_civil}</td>

                <button onclick="editarRegistro(registro${item.id},${item.id})" type="button" class="btn btn-warning" id="editar${item.id}" data-bs-toggle="modal" data-bs-target="#modalEditarRegistro">Editar</button>
                <button onclick="borrarRegistro(${item.id})" type="button" class="btn btn-danger" id="borrar${item.id}">Eliminar</button>

            `;
            tablaCuerpo.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

// Función para borrar un registro

function borrarRegistro(item) {
    fetch('/borrarpersona', {
        mode: 'cors',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: item.toString() })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Success:', data.message);
                location.reload(); // Reload only on success
            } else {
                console.error('Error:', data.error);
                alert('Error eliminando a la persona: ' + data.error);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error en la solicitud: ' + error);
        });
}


// Función para editar un registro
function editarRegistro(registro, id) {

    cedula = registro.children[1].innerHTML;
    p_Nombre = registro.children[2].innerHTML;
    s_Nombre = registro.children[3].innerHTML;
    p_Apellido = registro.children[4].innerHTML;
    s_Apellido = registro.children[5].innerHTML;
    fecha_nacimiento = registro.children[6].innerHTML;
    sexo = registro.children[7].innerHTML;
    telefono = registro.children[8].innerHTML;
    correo = registro.children[9].innerHTML;
    estado_civil = registro.children[10].innerHTML;

    fecha_nacimiento = new Date(fecha_nacimiento).toISOString().split('T')[0];

    idMod = document.getElementById('idMod').setAttribute('value', id);
    cedulaMod = document.getElementById('cedulaMod').setAttribute('value', cedula);
    p_NombreMod = document.getElementById('primerNombreMod').setAttribute('value', p_Nombre);
    s_NombreMod = document.getElementById('segundoNombreMod').setAttribute('value', s_Nombre);
    p_ApellidoMod = document.getElementById('primerApellidoMod').setAttribute('value', p_Apellido);
    s_ApellidoMod = document.getElementById('segundoApellidoMod').setAttribute('value', s_Apellido);
    fecha_nacimientoMod = document.getElementById('fechaDeNacimientoMod').setAttribute('value', fecha_nacimiento);
    if (sexo == "Masculino") {
        sexoMod = document.getElementById('sexoMod').selectedIndex = 1;

    } else {
        sexoMod = document.getElementById('sexoMod').selectedIndex = 0;
    }
    //sexoMod = document.getElementById('sexoMod').selectedIndex = 1;
    telefonoMod = document.getElementById('telefonoMod').setAttribute('value', telefono);
    correoMod = document.getElementById('direccionDeCorreoMod').setAttribute('value', correo);

    switch (estado_civil) {
        case "Soltero":

            estado_civilMod = document.getElementById('estadoCivilMod').selectedIndex = 0;

            break;
        case "Casado":

            estado_civilMod = document.getElementById('estadoCivilMod').selectedIndex = 1;

            break;
        case "Divorciado":

            estado_civilMod = document.getElementById('estadoCivilMod').selectedIndex = 2;

            break;
        case "Viudo":

            estado_civilMod = document.getElementById('estadoCivilMod').selectedIndex = 3;

            break;
        case "UnionLibre":

            estado_civilMod = document.getElementById('estadoCivilMod').selectedIndex = 4;

            break;

        default:
            break;
    }
    //estado_civilMod = document.getElementById('estadoCivilMod').setAttribute('value', estado_civil);


}
