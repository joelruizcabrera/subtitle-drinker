<template>
  <div class="search-engine">
    <div class="search-engine__container">
      <div class="input-group d-flex flex-column">
        <input type="search" class="form-control w-100" placeholder="Suche deinen Film..." aria-label="Suchen" v-model="movieInput">
        <div class="search-engine__results" v-if="dropdownOpen">
          <ul class="list-group">
            <li v-if="resultMovies.length === 0" class="list-group-item">
              Keine Ergebnisse gefunden
            </li>
            <li v-else class="list-group-item" v-for="movie in resultMovies" v-bind:key="movie.mv_id">
              <router-link :to="'/movie/' + movie.mv_id">
                {{movie.mv_name}}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchEngine",
  data() {
    return {
      movieInput: "",
      dropdownOpen: false,
      resultMovies: []
    }
  },
  computed: {
    movies() {
      let movies = this.$store.state.movieList;
      return movies;
    }
  },
  watch: {
    movieInput(val) {
      if (val !== "" && val !== null) {
        this.dropdownOpen = true
        this.searchEngine(val)
      } else {
        this.dropdownOpen = false
      }
    }
  },
  methods: {
    searchEngine(val) {
      let movieStrings = this.movies.map((e) => {
        if (e.mv_name.toLowerCase().includes(val.toLowerCase())) {
          return e
        }
      })
      const results = movieStrings.filter(e => {
        return e !== undefined;
      });
      this.resultMovies = results
    }
  }
}
</script>
