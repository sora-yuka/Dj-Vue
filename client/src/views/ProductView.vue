<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image" alt="product image">
                </figure>
            </div>
            <div class="column is-3">
                <h1 class="title">{{ product.name }}</h1>
                <h2 class="subtitle">Information</h2>
                <p class="description">{{ product.description }}</p><br>
                <p><strong>Price: </strong>${{ product.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import { toast } from "bulma-toast"

export default {
    name: "ProductView",
    data() {
        return {
            product: {}, // product object used for including data into views
            quantity: 1,
        }
    },
    mounted() {
        this.getProduct() // function declaration
    },
    methods: {
        async getProduct() {
            this.$store.commit("setIsLoading", true)
            const category_slug = this.$route.params.category_slug // get category param from url
            const product_slug = this.$route.params.product_slug // get product param from url
            // route include params from url
            
            await axios
            .get(`api/v1/product/${category_slug}/${product_slug}/`)
            .then(response => {
                this.product = response.data // Getting data from server and including into product-object
                document.title = this.product.name + " | store"
            })
            .catch(errors => {
                console.log(errors)
            })

            this.$store.commit("setIsLoading", false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity,
            }

            this.$store.commit("addToCart", item)

            toast({
                message: "Added successfully",
                type: "is-success",
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: "bottom-right"
            })
        }
    }
}
</script>