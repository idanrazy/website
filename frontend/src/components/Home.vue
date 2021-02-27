<template>
  <div>
    <v-container width="100%" style="text-align: center">
      <v-row>
        <v-col  cols="13"></v-col>
        <v-col cols="1" id="edit" >
          <v-btn fab
          x-small>
            <i class="fa fa-pencil" aria-hidden="true"> </i>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
    <v-container width="100%" style="text-align: center">פתיחה</v-container>

    <v-divider></v-divider>
    <v-container width="100%" style="text-align: center">
      <v-row>
        <v-col cols="1">
          <v-card width="200px">
            <img
              height="200px"
              :src="require(`@/assets/deadsea.jpg`)"
              class="grey lighten-2"
              id="img_alb"
              style="left: 10%"
            />
          </v-card>
        </v-col>
        <v-col cols="10"> קריירה </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
    <v-container width="100%" style="text-align: center">משפחה</v-container>
    <v-divider></v-divider>

    <v-container width="100%">
      <v-carousel height="60%">
        <v-carousel-item
          v-for="(item, i) in picturets"
          :key="i"
          :src="require(`@/assets/${picturets[i]}`)"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
      </v-carousel>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data: () => ({
    picturets: ["img1.jpg", "img2.jpg"],
  }),
};
</script>

<style>
#edit {
  color: SteelBlue;
}
</style>
