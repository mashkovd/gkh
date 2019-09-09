<template>
  <div>


    <b-table
      id="sick_list_table"
      :busy.sync="isBusy"
      striped
      hover
      small


      :items="myProvider"
      :fields="fields"

      :current-page="currentPage"
      :per-page="perPage"
      head-variant="light"

    >

    </b-table>

    <div>

      <b-pagination
        limit="10"
        align="fill"
        this.perPage=response.data.perPage

        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
        aria-controls="sick_list_table"
      >

      </b-pagination>


    </div>

  </div>
</template>


<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                // isBusy: false,
                perPage: 8,
                currentPage: 1,
                totalRows: 0
            }
        },
        methods: {
            myProvider(ctx) {
                // Here we don't set isBusy prop, so busy state will be
                // handled by table itself
                // this.isBusy = true
                let promise = axios.get('/api/sick_lists',
                    {
                        params: {
                            perPage: this.perPage,
                            currentPage: this.currentPage
                        }
                    })
                return promise.then((data) => {
                debugger;
                    this.items = data.data.items
                    this.fields = data.data.fields
                    this.totalRows = data.data.totalRows
                    // Here we could override the busy state, setting isBusy to false
                    this.isBusy = false
                    return (data.data.items)
                }).catch(error => {
                debugger;
                    // Here we could override the busy state, setting isBusy to false
                    // this.isBusy = false
                    // Returning an empty array, allows table to correctly handle
                    // internal busy state in case of error
                    return []
                })
            }
        }
    }
</script>


<style>
  #sick_list_table {


  }
</style>
