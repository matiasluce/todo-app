if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            tareas: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'https://crud-todo-flask.herokuapp.com/tareas'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.productos = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(tarea) {
                const url = 'https://crud-todo-flask.herokuapp.com/tareas/' + tarea;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
