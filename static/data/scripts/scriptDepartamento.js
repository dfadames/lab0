// URL del archivo JSON
const jsonUrl = '/api/departamento';

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
                <td>${item.nombre_departamento}</td>
                <td>${item.codigo_departamento}</td>

                <button onclick="editarPersona(registro${item.id},${item.id})" type="button" class="btn btn-warning" id="editar${item.id}" data-bs-toggle="modal" data-bs-target="#modalEditarRegistro">Editar</button>
                <button onclick="enviarIdBorrar(${item.id})" type="button" class="btn btn-danger" id="borrar${item.id}">Eliminar</button>

            `;
            tablaCuerpo.appendChild(fila);
        });
    })
    .catch(error => console.error('Error al cargar los datos:', error));

// Función para borrar un registro

function enviarIdBorrar(item) {
    fetch('/borrardepartamento', {
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
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

// Función para editar un registro
function editarPersona(registro, id) {

    nombreDepartamentoMod = registro.children[1].innerHTML;
    codigoDepartamentoMod = registro.children[2].innerHTML;

    idMod = document.getElementById('idMod').setAttribute('value', id);
    nombreDepartamentoMod = document.getElementById('nombreDepartamentoMod').setAttribute('value', nombreDepartamentoMod);
    codigoDepartamentoMod = document.getElementById('codigoDepartamentoMod').setAttribute('value', codigoDepartamentoMod);



}
