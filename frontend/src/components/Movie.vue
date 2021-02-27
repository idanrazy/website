<template>
      <v-container  width="100%" style="text-align: center;">
            <iframe v-if="false"  loading="lazy" width="560" height="315" :src="movie" allowfullscreen></iframe>
            <v-divider></v-divider>
            הסבר על הסרט
    </v-container>    
</template>
<script>
export default {
        
    name:"Movie",
    components: {},
    data :()=>({
        //movie:"https://drive.google.com/file/d/1NSbuXfp5bdzY1G0TYHKkcanqQU7q-m7W/view?usp=sharing"
    })
}
</script>
<style scoped>

</style>