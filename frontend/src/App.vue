<template>
  <v-app>
    <div id="nav">
      <b-navbar type="light" variant="light">
        <b-navbar-nav>
          <b-nav-item active
            ><router-link to="/">Home</router-link>
          </b-nav-item>
          <b-nav-item><router-link to="/Album">Album</router-link> </b-nav-item>
          <b-nav-item><router-link to="/Movie">Movie</router-link> </b-nav-item>
          <b-nav-item><router-link to="/About">about</router-link> </b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item>
            <i class="fa fa-user"></i>
          </b-nav-item>
          <b-nav-item
            ><router-link to="/"
              ><i class="fa fa-home" aria-hidden="true"></i></router-link
          ></b-nav-item>
        </b-navbar-nav>
      </b-navbar>
    </div>
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  }),
};
</script>


<style>
b-nav-item {
  color: white;
}
</style>
