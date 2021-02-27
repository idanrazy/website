import Home from './components/Home.vue';
import VueRouter from 'vue-router';
import Album from './components/Album.vue'
import Movie from './components/Movie.vue'
import Vue from 'vue'
Vue.use(VueRouter);


export default new VueRouter({
    routes : [
        {
          path: '/',
          Name:Home,
          component: Home
        },
        {
          path: '/Album',
          Name:Album,
          component: Album
        },
        {
          path: '/Movie',
          Name:Movie,
          component: Movie
        },
      ]
  });

