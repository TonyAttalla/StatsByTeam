<template>
  <div class="flex-container" >
    <h3 class="row-item">{{fullName}}</h3>
    <div class="selectors">
      <v-select v-model="selectedMode" class="row-item" :options="['By Team', 'By Player']"></v-select>
    </div>
    <div v-if="done === 1">
      <div class="selectors">
        <v-select v-model="selectedStat" class="row-item" :options="stats"></v-select>
        <v-select v-model="selectedPlayer" class="row-item" :options="roster"></v-select>
        <md-button v-on:click="getStatsOverTimeByPlayer()" class="md-raised md-primary">Search</md-button>
      </div>

      <div>
        <apexchart type="line" :options="options" :series="series"></apexchart>
      </div>
    </div>

    <div class="container" v-else>
      <div class="center">
        <RotateSquare2></RotateSquare2>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import ApexCharts from "apexcharts";
import { RotateSquare2 } from "vue-loading-spinner";

export default {
  name: "History",
  data() {
    return {
      msg: "Hello!",
      name: "",
      done: 0,
      selectedMode: "By Player",
      selectedPlayer: "",
      selectedStat: "",
      roster: [],
      stats: [],
      fullName: "",
      options: {
        chart: {
          id: "vuechart-example"
        },
        xaxis: {
          categories: []
        }
      },
      dataLabels: {
        enabled: true
      },
      series: [
        {
          name: "series-2",
          data: [],
          dataLabels: {
            enabled: false
          }
        }
      ]
    };
  },
  methods: {
    getStatsDropDown() {
      const path = "http://localhost:5000/statsdropdown";
      axios
        .get(path)
        .then(res => {
          this.stats = res.data;
          this.selectedStat = this.stats[0];
          this.getRoster(this.shortName);
        })
        .catch(error => {
          console.error(error);
        });
    },
    getRoster(shortName) {
      const path = "http://localhost:5000/roster";
      axios
        .get(path, { params: { teamName: shortName } })
        //.get(path)
        .then(res => {
          console.log(res.data);
          this.roster = res.data;
          console.log(this.roster);
          this.selectedPlayer = this.roster[0];
          this.getStatsOverTimeByPlayer();
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    updateChart(years, stat) {
      console.log(years);
      this.options.xaxis.categories = years;
      console.log(stat);
      this.series = [
        {
        name: "Value:",
          data: stat
        }
      ];
      this.options = {
        ...this.options,
        ...{
          xaxis: {
            categories: years
          }
        }
      };
      console.log(this.options);
      this.done = 1;
    },
    getStatsOverTimeByPlayer() {
      console.log("getting stats over time");
      const path = "http://localhost:5000/statsovertimeplayer";
      axios
        .get(path, {
          params: {
            playerName: this.selectedPlayer,
            statName: this.selectedStat
          }
        })
        //.get(path)
        .then(res => {
          console.log(res.data);
          this.options.xaxis.categories = res.data.Years;
          this.series.data = res.data.stat;
          this.updateChart(res.data.Years, res.data.stat);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.name = this.$attrs.name;
    this.shortName = this.$attrs.shortName;
    this.fullName = this.$attrs.fullName;
    this.getStatsDropDown();
  },
  components: {
    RotateSquare2
  }
};
</script>
<style>
.flex-container {
  display: flex;
  justify-content: space-between;
  text-align: center;
  padding-top: 10px;
  padding-left: 20px;
  padding-right: 20px;
  flex-direction: column;
}
.row-item {
  margin-bottom: 10px;
}
@font-face {
  font-family: "gameplay"; /*a name to be used later*/
  src: url("../assets/fonts/gameplay/gameplay.ttf"); /*URL to font*/
}
h3 {
  font-family: "gameplay", Arial, sans-serif;
  font-weight: normal;
  font-style: normal;
}
.center {
  margin: 0;
  position: absolute;
  top: 175%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}
</style>