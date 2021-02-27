<template>
  <div>
    <!--album -->
    <v-container width="100%" style="text-align: center; margin-top:30px">
      <v-row>
        <b-alert
          v-model="showinfo"
          show
          variant="warning"
          style="width: 300px; margin: auto"
        >
          להגדלה יש ללחוץ על התמונה
          <v-btn style="width: 15px; height: 15px" text
            ><i
              @click="showinfo = false"
              class="fa fa-times"
              style="color: red"
              aria-hidden="true"
            ></i
          ></v-btn>
        </b-alert>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-text-field class="search" label="Search" v-model="search_text"></v-text-field>
        </v-col>
        <v-col cols="8"></v-col>
      </v-row>
    </v-container>
    <v-container width="100%" style="text-align: center; margin-top: 50px">
      <v-row>
        <v-col
          v-for="c in picturets_num"
          :key="c"
          :cols="4"
          class="d-flex child-flex"
        >
          <img
            @click="showImage(c - 1)"
            height="200px"
            :src="filterd_pictures[c - 1].source"
            class="grey lighten-2"
            id="img_alb"
          />
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular
                indeterminate
                color="grey lighten-5"
              ></v-progress-circular>
            </v-row>
          </template>
        </v-col>
      </v-row>
    </v-container>

    <!-- ima card -->
    <v-dialog v-model="show_image" max-width="600" class="justify-center">
      <v-card v-if="currentImg">
        <v-card-title>
          <v-btn x-small @click="edit_image(currentImg)" v-if="admin"
            >edit</v-btn
          >
          <v-container style="text-align: center">
            <span>{{ currentImg.header }}</span>
          </v-container>
        </v-card-title>
        <v-row no-gutters>
          <img :width="600" :src="currentImg.source" class="grey lighten-2" />
        </v-row>

        <v-card-subtitle style="padding-top: 10px">
          <v-container max-width="600">
            <v-row no-gutters>
              <v-col v-if="edit_flag == false">
                <v-chip
                  v-for="(c, index) in currentImg.categories"
                  :key="c"
                  text-color="white"
                  :color="cat_colors[index % cat_colors.length]"
                >
                  {{ c }}</v-chip
                >
              </v-col>
            </v-row>

            <v-divider></v-divider>
            <v-row dir="rtl" no-gutters
              ><span>{{ currentImg.description }}</span></v-row
            >
          </v-container>
        </v-card-subtitle>
      </v-card>
    </v-dialog>

    <!-- -->
    <v-dialog v-model="edit_flag" v-if="edit_image_data" max-width="600">
      <v-card>
        <v-card-title> Edit Picture </v-card-title>
        <v-card-text>
          <v-form ref="edit_image">
            <v-divider></v-divider>

            <v-text-field
              v-model="edit_image_data.header"
              label="כותרת"
            ></v-text-field>

            <v-text-field
              v-model="edit_image_data.description"
              label="תיאור תמונה"
            ></v-text-field>

            <v-autocomplete
              v-model="edit_image_data.categories"
              :items="categories"
              chips
              dense
              multiple
              item-color="blue"
            ></v-autocomplete>

            <v-btn class="mr-4" @click="submit()"> שמירה </v-btn>
            <v-btn class="mr-4" @click="clear()"> ביטול </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Album",
  components: {},
  data: () => ({
    picturets: [],
    search_text:"",
    max_col: 6,
    cols_num: null,
    rows_num: null,
    // should get from back by login
    admin: true,
    image: null,
    picturets_num: null,
    categories: [],
    show_image: false,
    currentImg: null,
    showinfo: true,
    cat_colors: [],
    edit_flag: false,
    edit_color: "primary",
    edit_label: "edit",
    edit_image_data: null,
  }),
  beforeMount: function () {
    this.get_all_images();
    this.get_categories();
  },
  computed: {
    filterd_pictures(){
      
        if(this.search_text === "" || this.search_text === null){

          this.album_rows_cols_num(this.picturets)
          this.$forceUpdate();
          return this.picturets
        }
        else{
          let filterd = []
          for (let i in this.picturets){
            if (this.picturets[i].name.includes(this.search_text))
            {
              filterd.push(this.picturets[i])
            }
          }
          this.album_rows_cols_num(filterd)
          this.$forceUpdate();
          return filterd
        }
    }
  },
  methods: {
    album_rows_cols_num: function (picturets) {
      for (let i = this.max_col; i > 1; i--) {
        if (picturets.length % i === 0) {
          this.rows_num = i;
          this.cols_num = picturets.length / i;
          this.picturets_num = picturets.length;
          break
        }
        else if(i === 1){
          this.rows_num = i;
          this.cols_num = i;
          this.picturets_num = i;
        }
      }
    },
    showImage: function (img_index) {
      this.show_image = true;
      this.currentImg = this.filterd_pictures[img_index];
    },
    edit_image: function (imagedata) {
      this.edit_flag = this.edit_flag == true ? false : true;
      if (this.edit_flag) {
        this.edit_label = "save";
        this.edit_color = "error";
      } else {
        this.edit_label = "edit";
        this.edit_color = "primary";
      }
      this.edit_image_data = {};
      this.edit_image_data.name = imagedata.name;
      this.edit_image_data.description = imagedata.description;
      this.edit_image_data.categories = imagedata.categories;
      this.edit_image_data.header = imagedata.header;
    },
    // get from back
    get_categories: function () {
      let api = this.$api;
      let full_uri = `${api}/categories`;
      axios
        .get(full_uri)
        .then((response) => {
          let categories_data = response.data;
          for (let i in categories_data) {
            this.categories.push(categories_data[i].name);
            this.cat_colors.push(categories_data[i].color);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    get_all_images: function () {
      let api = this.$api;
      var full_uri = `${api}/images`;
      axios
        .get(full_uri)
        .then((response) => {
          this.picturets = response.data;
          this.album_rows_cols_num(this.picturets);
          for (let i in this.picturets) {
            this.get_image(i);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    submit: function () {
      let end_point = "images";
      let api = this.$api;
      var full_uri = `${api}/${end_point}`;
      axios.post(full_uri, this.edit_image_data).then((response) => {
        if (response.data.IsSuccess) {
          this.currentImg.categories = this.edit_image_data.categories;
          this.currentImg.header = this.edit_image_data.header;
          this.currentImg.description = this.edit_image_data.description;
        }
      });
      this.clear().catch((error) => {
        console.log(error);
      });
    },
    clear: function () {
      this.edit_flag = false;
      this.edit_image_data = null;
    },
    get_image: function (index) {
      let end_point = "images";
      let api = this.$api;
      var full_uri = `${api}/${end_point}/${this.picturets[index].name}`;

      axios
        .get(full_uri, { responseType: "arraybuffer" })
        .then((response) => {
          var arrayBufferView = new Uint8Array(response.data);
          var blob = new Blob([arrayBufferView], { type: "image/jpeg" });
          var urlCreator = window.URL || window.webkitURL;
          var imageUrl = urlCreator.createObjectURL(blob);
          this.picturets[index].source = imageUrl;
          this.image = imageUrl;
          this.$forceUpdate();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
#img_alb:hover {
  cursor: pointer;
}
.search {
  width: 150px;
}
</style>