<template>

          <ul>
      <li v-for="l in items">{{ l }}</li>
    </ul>

</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Main',
        data() {
            return {
                items: []
            }
        },
        created() {
            axios.get("/api/consultants").then(r => {
                this.items = r.data.items
            })
        }
    }
</script>

<style scoped>
  p {
    margin: 100px;
  }

</style>
