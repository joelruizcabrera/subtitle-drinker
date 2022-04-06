<template>
  <div class="movies__list container-fluid">
    <div class="row mt-5 card-group">
      <div class="col-xl-2 col-lg-4 col-md-6" v-for="movie in movies" v-bind:key="movie.mv_id">
        <div class="card h-100">
          <div class="movie-thumbnail" :style="'background-image: url(' + movie.mv_thumbnail + ')'"></div>
          <div class="card-body d-flex justify-content-between flex-column">
            <h5 class="card-title mb-5">{{movie.mv_name}}</h5>
<!--            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>-->
            <router-link :to="'/movie/' + movie.mv_id" class="btn btn-primary">
              Ansehen
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.movie-thumbnail {
  width: 100%;
  height: 17rem;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>

<script>
export default {
  name: "Movies",
  computed: {
    movies() {
      let movies = this.$store.state.movieList;
      movies = movies.map((e) => {
        if (e.mv_langs !== undefined) {
          e.mv_langs = e.mv_langs.split(",")
          e.mv_langs.pop(1)
          return e
        }
      })
      return movies;
    }
  }
}
</script>
