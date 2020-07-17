const app = new Vue({
            el: '#app',
            data: {
                products: [
                    {"id":1, "quantity":1, "name":"Compass"},
                    {"id":2, "quantity":0, "name":"Jacket"},
                    {"id":3, "quantity":5, "name":"Hiking Socks"},
                    {"id":4, "quantity":2, "name":"Suntan Lotion"}
                ]},
            computed: {
                    totalProducts () {
                    return this.products.reduce((sum, product) =>{
                    return sum + product.quantity
                    },0)
                    }
            }
})

