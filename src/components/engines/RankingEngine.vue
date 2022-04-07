<template>
  <div class="ranking">
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Platz</th>
            <th scope="col">Wort</th>
            <th scope="col">Häufigkeit</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="rank in movieWords" v-bind:key="rank.sb_id">
            <th scope="row">{{rank.sb_rank}}</th>
            <td>{{rank.sb_word}}</td>
            <td>{{rank.sb_count}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RankingEngine",
  props: [
      "movieId"
  ],
  data() {
    return {
      movieWords: {}
    }
  },
  mounted() {
    setInterval(() => {
      this.fetchMovieWords()
    }, 1500)
  },
  methods: {
    fetchMovieWords() {
      return new Promise((resolve, reject) => {
        axios.get(this.$store.state.apiHost + "/MovieWords/read.php?sb_mv_id=" + this.movieId)
            .then((res) => {
              this.movieWords = res.data
            })
            .catch(err => {
              reject(err)
            })
      })
    }
  }
}
</script>
