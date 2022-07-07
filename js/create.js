function guardar() {
 
    let n = document.getElementById("txtName").value
    let d = document.getElementById("txtDesc").value

 
    let producto = {
        name: n,
        desc: d,
        done: 0
    }
    let url = "https://crud-todo-flask.herokuapp.com/tareas"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
    .then(function () {
        console.log("creado")
        alert("Grabado")

        // Handle response we get from the API
    })
    .catch(err => {
        //this.errored = true
        alert("Error al grabar" )
        console.error(err);
    })
}

