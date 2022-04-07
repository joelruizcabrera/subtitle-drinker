'use strict';

const API_HOST = "https://api.subtitledrinker.de/api"

import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    apiHost: API_HOST,
    languageList: [],
    movieList: [],
    movieWords: {}
  },
  mutations: {
    GET_ALL_LANGUAGES(state, languages) {
      state.languageList = languages
    },
    GET_ALL_MOVIES(state, movies) {
      state.movieList = movies
    }
  },
  actions: {
    async fetchLanguages(ctx) {
      return new Promise((resolve, reject) => {
        axios.get(API_HOST + "/Languages/read.php")
            .then((res) => {
              resolve(ctx.commit('GET_ALL_LANGUAGES', res.data))
            })
            .catch(err => {
              reject(err)
            })
      })
    },
    async fetchMovies(ctx) {
      return new Promise((resolve, reject) => {
        console.log("test")
        axios.get(API_HOST + "/Movies/read.php")
            .then((res) => {
              resolve(ctx.commit('GET_ALL_MOVIES', res.data))
            })
            .catch(err => {
              reject(err)
            })
      })
    },
  },
  modules: {
  },
  getters: {
    getLanguages: state =>  {
      return state.languageList
    },
    getMovies: state => {
      return state.movieList
    }
  }
})
