var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtName").value = decodeURI(parts[1][1]) 
document.getElementById("txtDesc").value = parts[2][1]
document.getElementById("txtDone").value = parts[3][1]
 
function modificar() {
    let id = document.getElementById("txtId").value
    let n = document.getElementById("txtName").value
    let d = document.getElementById("txtDesc").value
    let s = document.getElementById("txtDone").value
    let producto = {
        name: n,
        precio: p,
        desc: d,
        done: s
    }
    let url = "https://crud-shop-flask.herokuapp.com/productos/"+id
    var options = {
        body: JSON.stringify(producto),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
