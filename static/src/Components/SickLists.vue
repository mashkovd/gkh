<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col sm="1" md="6" class="my-1">
          <b-form-group
            label="Кол-во записей на странице"
            label-cols-sm="4"
            label-size="sm"
            label-for="perPageSelect"
            class="mb-0"
          >
            <b-form-select
              v-model="perPage"
              id="perPageSelect"
              size="sm"
              :options="pageOptions"
            ></b-form-select>
          </b-form-group>

        </b-col>
                <b-col sm="1" md="6" class="my-1">
          <b-form-group
            label="Всего записей"
            label-cols-sm="4"
            label-size="sm"
            label-for="perPageSelect"
            class="mb-0"
          >

            <b> {{ totalRows }} </b>
          </b-form-group>

        </b-col>



      </b-row>

      <b-form-group
        label="Фильтр"
        label-class="font-weight-bold pt-0"
        class="mb-0"
      >
        <b-row>
                    <b-col sm="1" md="4" class="my-1">
            <b-form-group
              label-cols-lg="3"
              label="Консультант"
              label-size="sm"

              label-for="select_correction"
            >

              <b-form-select id="select_consultant" v-model="filter.consultant" :options="consultants_options"

              >
                <template v-slot:first>
                  <option :value="null">-- Укажите консультанта --</option>
                </template>
              </b-form-select>

            </b-form-group>
          </b-col>

          <b-col sm="5" md="4" class="my-1">
            <b-form-group
              label-cols-sm="1"
              label="№"
              label-size="sm"

              label-for="select_correction"
            >
              <b-form-select id="select_number" v-model="filter.number" :options="number_options">
                <template v-slot:first>
                  <option :value="null">-- Укажите номер консультации --</option>
                </template>
              </b-form-select>

            </b-form-group>
          </b-col>

          <b-col sm="1" md="4" class="my-1">
            <b-form-group
              label-cols-lg="3"
              label="Коррекция"
              label-size="sm"

              label-for="select_correction"
            >

              <b-form-select id="select_correction" v-model="filter.correction" :options="correction_options">
                <template v-slot:first>
                  <option :value="null">-- Укажите коррекцию --</option>
                </template>
              </b-form-select>

            </b-form-group>
          </b-col>
          <b-col sm="1" md="4" class="my-1">
            <b-form-group
              label-cols-lg="3"
              label="Отделение"
              label-size="sm"

              label-for="select_department"
            >
              <b-form-select id="select_department" v-model="filter.department" :options="departments_options">
                <template v-slot:first>
                  <option :value="null">-- Укажите отделение --</option>
                </template>
              </b-form-select>

            </b-form-group>
          </b-col>
          <b-col sm="1" md="4" class="my-1">
            <b-form-group
              label-cols-lg="3"
              label="Диагноз"
              label-size="sm"

              label-for="select_diagnose"
            >
              <b-form-input id="select_diagnose" v-model="filter.diagnose">
                <template v-slot:first>
                  <option :value="null">-- Укажите диагноз --</option>
                </template>
              </b-form-input>

            </b-form-group>
          </b-col>

        </b-row>
      </b-form-group>



      <b-pagination
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
        align="fill"
        size="sm"
        class="my-0"
      ></b-pagination>
      <b-table
        id="sick_list_table"
        ref="table"
        small
        fixed
        :filter="filter"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :sort-direction="sortDirection"
        @filtered="onFiltered"
        filter-debounce="150"
        style="width: 100%"


        :items="myProvider"
        :fields="fields"
        :current-page="currentPage"
        :per-page="perPage"
        @sort-changed="sortingChanged"

        head-variant="light"

      >


      </b-table>

    </b-container>
  </div>
</template>


<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                totalRows: 1,
                fields: null,
                currentPage: 1,
                perPage: 5,
                pageOptions: [5, 10, 15, 100],
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: {
                    correction: null,
                    number: null,
                    consultant: null,
                    diagnose: null,
                    department: null,

                },
                filterOn: [],

                correction_options: [
                    {text: 'Полная', value: 2},
                    {text: 'Частичная', value: 1},
                    {text: 'Не требуется', value: 0},
                ],
                number_options: [
                    {text: '1', value: 1},
                    {text: '2', value: 2},
                ],
                consultants_options: [],
                departments_options: [],

            }
        },

        methods: {
            myProvider(ctx) {
                let promise = axios.get('/api/sick_lists',
                    {
                        params: {
                            perPage: ctx.perPage,
                            currentPage: ctx.currentPage,
                            filter: ctx.filter,
                        }
                    })

                return promise.then((data) => {
                    this.items = data.data.items;
                    this.fields = data.data.fields;
                    this.totalRows = data.data.totalRows;
                    return (data.data.items)
                }).catch(error => {
                    return []
                })
            },
            sortingChanged(ctx) {
                debugger;
            },
            getData() {
                axios.get('/api/consultants')
                    .then(response => {
                        this.consultants_options = response.data.items
                    })
                    .catch(error => console.log(error))
                axios.get('/api/departments')
                    .then(response => {
                        this.departments_options = response.data.items
                    })
                    .catch(error => console.log(error))

            },

            onFiltered(filteredItems) {
                // Trigger pagination to update the number of buttons/pages due to filtering
                //this.$refs.table.refresh()
                // let promise = axios.get('/api/sick_lists',
                //     {
                //         params: {
                //             perPage: this.perPage,
                //             filter: this.filter,
                //         }
                //     })
                //
                // return promise.then((data) => {
                //     this.items = data.data.items
                //     this.fields = data.data.fields
                //     this.totalRows = data.data.totalRows
                //     return (data.data.items)
                // }).catch(error => {
                //     return []
                // }),
                //
                //     this.currentPage = 1
            }
        },
        computed: {
            // consultant_options: function ()
            // {
            //     debugger
            //
            // }

        },
        mounted: function () {
            this.getData()
        },

    }
</script>


<style>
  #sick_list_table {


  }
</style>
