<template>
  <NavigationBar></NavigationBar>
  <div class="wrapper">
    <router-view/>
  </div>
  <Footer></Footer>
</template>

<script>
import NavigationBar from "./components/navigation/NavigationBar";
import Footer from "./components/navigation/Footer";

export default {
  name: 'App',
  components: {
    NavigationBar,
    Footer
  },
  created() {
    console.log("test")
    this.$store.dispatch('fetchMovies')
  },
}
</script>

<style lang="scss">
html {
  overflow-x: hidden;
}
.wrapper {
  min-height: calc(100vh - 56px);
}
</style>
