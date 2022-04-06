<template>
  <div class="footer bg-light">
    <div class="container-fluid">
      <footer class="d-flex flex-wrap justify-content-between align-items-center p-5 mt-5 border-top">
        <p class="col-md-4 mb-0 text-muted">© {{ new Date().getFullYear() }} <a href="https://joelruizcabrera.com" class="text-black">joelruizcabrera.com</a></p>

        <a href="https://joelruizcabrera.com" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <svg width="75" height="auto" viewBox="0 0 129 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19.5333 23.3314L22.2215 0C22.2215 0 93.4003 0.0964758 105.926 0.0964758C115.82 0.607764 129.396 7.97166 128.991 24.1937C129.115 47.675 114.22 52.3964 102.755 56.4351C104.234 63.5647 107.921 77.4569 107.921 77.4569C107.921 77.4569 110.037 81.5194 113.269 81.2406L118.098 99.9998H90.1624L85.2929 81.2406C85.2929 81.2406 90.1216 81.4407 88.8447 76.2222C87.5677 71.0038 83.8554 56.4351 83.8554 56.4351H65.836C65.836 56.4351 64.4853 71.1958 64.0249 74.3505C63.5645 77.5051 55.4106 100.075 34.7193 99.9998C14.0279 99.9242 0 99.9998 0 99.9998L2.1042 76.736H21.0421C21.0421 76.736 21.1981 81.117 24.8318 81.117H35.9686C39.7462 81.117 45.1164 79.5587 46.2829 66.6912C47.4493 53.8236 49.2274 37.6188 49.2274 37.6188C49.2274 37.6188 85.7291 38.0147 101.415 37.6188C101.415 37.6168 110.194 37.1171 110.194 27.1539C110.194 17.1906 101.415 17.9934 101.415 17.9536H43.0175C43.0175 17.9536 38.1929 17.7313 38.1929 23.6444C38.2439 23.6964 19.5333 23.3314 19.5333 23.3314Z" fill="black"/>
          </svg>

        </a>

        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item" :key="route.path" v-for="route in routes" >
            <router-link :to="route.path" class="nav-link px-2" :active-class="'active'">
              {{route.name}}
            </router-link>
          </li>
        </ul>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  computed: {
    routes() {
      let routes = this.$router.getRoutes();
      let navRoutes = []
      for (let i = 0; i < routes.length; i++) {
        if (routes[i].props.default.footer === true) {
          navRoutes.push(routes[i])
        }
      }
      return navRoutes;
    }
  },
}
</script>
