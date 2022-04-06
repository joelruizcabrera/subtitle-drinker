<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li v-for="route in routes" :key="route.path" class="nav-item">
            <router-link :to="route.path" class="nav-link" :active-class="'active'">
              {{route.name}}
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavigationBar",
  computed: {
    routes() {
      let routes = this.$router.getRoutes();
      let navRoutes = []
      for (let i = 0; i < routes.length; i++) {
        if (routes[i].props.default.nav === true) {
          navRoutes.push(routes[i])
        }
      }
      return navRoutes;
    }
  },
  mounted() {
    console.log(this.routes)
  }
}
</script>
