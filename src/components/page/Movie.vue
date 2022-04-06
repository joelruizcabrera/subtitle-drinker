<template>
  <div class="single-movie container-fluid">
    <div class="row">
      <div class="col-4 mt-5 text-center">
        <img :alt="movieInfo.mv_name" :src="movieInfo.mv_thumbnail" style="width: 70%;height: auto">
      </div>
      <div class="col-sm mt-5 ps-4">
        <h1>{{movieInfo.mv_name}}</h1>
        <small>Movie ID-Nr.: <u>{{movieInfo.mv_id}}</u></small>
        <p class="movie__language_heading">Verfügbar in diesen Sprachen:</p>
        <ul class="movie__language_list">
          <li v-for="lang in movieInfo.mv_langs" v-bind:key="lang">
            <img :src="'https://flagcdn.com/w40/' + lang.toLowerCase() + '.png'" :alt="lang">
          </li>
        </ul>
        <div class="movie__ranking-table mt-3">
          <RankingEngine :movieId="this.slugId"></RankingEngine>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.movie__language_heading {
  margin-bottom: 0;
  margin-top: 2rem;
}
.movie__language_list {
  list-style: none;
  padding-left: 0;
  margin-bottom: 0;
  li {
    display: inline;
    &:not(:last-child) {
      margin-right: 1rem;
    }
  }
}
</style>

<script>
import RankingEngine from "../engines/RankingEngine";
import axios from "axios";

export default {
  name: "Movie",
  components: {
    RankingEngine
  },
  data() {
    return {
      slugId: this.$route.params.id,
      movieInfo: null
    }
  },
  computed: {
    getMovies() {
      return this.$store.getters.getMovies
    }
  },
  created() {
    setInterval(() => {
      this.getMovieById()
    }, 1500)
  },
  methods: {
    getMovieById() {
      return new Promise((resolve, reject) => {
        axios.get("http://" + this.$store.state.apiHost + "/api/Movies/read_one.php?mv_id=" + this.slugId)
            .then((res) => {
              this.movieInfo = res.data
              this.movieInfo.mv_langs = this.movieInfo.mv_langs.split(',')
            })
            .catch(err => {
              reject(err)
            })
      })
    }
  }
}
</script>
