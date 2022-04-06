import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Movie from "../components/page/Movie";
import Movies from "../components/page/Movies";
import Request from "../components/page/Request";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    props: {
      nav: true,
      footer: false
    }
  },
  {
    path: '/movies',
    name: 'Filme',
    component: Movies,
    props: {
      nav: true,
      footer: false
    }
  },
  {
    path: '/request',
    name: 'Anfrage',
    component: Request,
    props: {
      nav: true,
      footer: true
    }
  },
  {
    path: '/movie/:id',
    name: 'Film',
    component: Movie,
    props: {
      nav: false,
      footer: false
    }
  },
  {
    path: '/imprint',
    name: 'Impressum',
    component: Home,
    props: {
      nav: false,
      footer: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
