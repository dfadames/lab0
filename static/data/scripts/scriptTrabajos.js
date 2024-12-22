// URL del archivo JSON
const jsonUrl = '/api/trabajo';

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
                <td>${item.id_municipio_trabajo}</td>
                <td>${item.nombre_trabajo}</td>
                <td>${item.oficio}</td>
                <td>${item.salario}</td>
                <td>${item.tipo_contrato}</td>


                <button onclick="editarRegistro(registro${item.id},${item.id})" type="button" class="btn btn-warning" id="editar${item.id}" data-bs-toggle="modal" data-bs-target="#modalEditarRegistro">Editar</button>
                <button onclick="borrarRegistro(${item.id})" type="button" class="btn btn-danger" id="borrar${item.id}">Eliminar</button>

            `;
            tablaCuerpo.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

// Función para borrar un registro

function borrarRegistro(item) {
    fetch('/borrartrabajo', {
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
                location.reload(); // Reload the page only on success
            } else {
                console.error('Error:', data.error);
                alert('Error eliminando trabajo: ' + data.error);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error en la solicitud: ' + error);
        });
}


// Función para editar un registro
function editarRegistro(registro, id) {

    idMunicipioTrabajoMod = registro.children[1].innerHTML;
    nombreTrabajoMod = registro.children[2].innerHTML;
    oficioMod = registro.children[3].innerHTML;
    salarioMod = registro.children[4].innerHTML;
    tipoDeContratoMod = registro.children[5].innerHTML;


    idMod = document.getElementById('idMod').setAttribute('value', id);
    idMunicipioTrabajoMod = document.getElementById('idMunicipioTrabajoMod').setAttribute('value', idMunicipioTrabajoMod);
    nombreTrabajoMod = document.getElementById('nombreTrabajoMod').setAttribute('value', nombreTrabajoMod);
    oficioMod = document.getElementById('oficioMod').setAttribute('value', oficioMod);
    salarioMod = document.getElementById('salarioMod').setAttribute('value', salarioMod);
    tipoDeContratoMod = document.getElementById('tipoDeContratoMod').setAttribute('value', tipoDeContratoMod);



}
