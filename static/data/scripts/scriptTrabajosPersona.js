// URL del archivo JSON
const jsonUrl = '/api/persona_trabajo';

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
                <td>${item.id_persona}</td>
                <td>${item.id_trabajo}</td>

                <button onclick="editarPersona(registro${item.id},${item.id})" type="button" class="btn btn-warning" id="editar${item.id}" data-bs-toggle="modal" data-bs-target="#modalEditarRegistro">Editar</button>
                <button onclick="enviarIdBorrar(${item.id})" type="button" class="btn btn-danger" id="borrar${item.id}">Eliminar</button>

            `;
            tablaCuerpo.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

// Función para borrar un registro

function enviarIdBorrar(item) {
    fetch('/borrarpersonatrabajo', {
        mode: 'cors',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: item.toString() })
    })
        .then(response => response.json())
        .then(data => {
            // Check if the request was successful
            if (data.success) {
                console.log('Success:', data.message);
                // Reload the page only if the request is successful
                location.reload();
            } else {
                console.error('Error:', data.error);
                alert('Error: ' + data.error);
            }
        })
        .catch((error) => {
            // Handle network or other errors
            console.error('Request failed:', error);
            alert('Error en la solicitud: ' + error.message);
        });
}



// Función para editar un registro
function editarPersona(registro, id) {

    idPersonaMod = registro.children[1].innerHTML;
    idTrabajoMod = registro.children[2].innerHTML;



    idMod = document.getElementById('idMod').setAttribute('value', id);
    idPersonaMod = document.getElementById('idPersonaMod').setAttribute('value', idPersonaMod);
    idTrabajoMod = document.getElementById('idTrabajoMod').setAttribute('value', idTrabajoMod);
    

}
