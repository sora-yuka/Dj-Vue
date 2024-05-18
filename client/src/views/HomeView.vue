<template>
  <div class="home">
    <section class="hero is-medium has-text-centered">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to market</p>
        <p class="subtitle">The best market ever</p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest product</h2>
      </div>
      <div 
        class="column is-3"
        v-for="product in latestProducts"
        v-bind:key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="product.get_thumbnail" alt="product image">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-gray">${{ product.price }}</p>
          <p><b><router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View details</router-link></b></p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()
    document.title = "HOME | market"
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true)

      await axios
      .get("api/v1/product/latest/")
      .then(response => {
        this.latestProducts = response.data
      })
      .catch(errors => {
        console.log(errors)
      })

      this.$store.commit("setIsLoading", false)
    }
  },
  components: {
    
  }
}
</script>

<style scoped>
  .image  {
      margin-top: -1.25rem;
      margin-left: -1.25rem;
      margin-right: -1.25rem;
  }
</style>