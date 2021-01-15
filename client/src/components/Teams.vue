<template>
  <div  class="teams-container" v-if="done === 1">
    <div
      class="one-team fade-in"
      v-for="team in teams"
      v-bind:key="team.URL"
      @click="showModal(team)"
    >
      <div class="team-img">
        <img :src="require('../assets/teamIcons/' + team.Name + '.jpg')" />
      </div>
    </div>
    <modal name="hello-world">hello, world!</modal>
    <modals-container />
  </div>

  <div class="container" v-else>
    <div class="center">
      <RotateSquare2></RotateSquare2>
    </div>
  </div>
</template>

<script>
/* eslint-disable indent */
import VueGridLayout from "vue-grid-layout";
import axios from "axios";
import example from "./History.vue";
import History from "./History.vue";
import HistoryVue from "./History.vue";

import { RotateSquare2 } from "vue-loading-spinner";
import { Stretch } from "vue-loading-spinner";

export default {
  data() {
    return {
      teams: [],
     
      numTeams: 0,
      currentImgURL: "",
      done: 0
    };
  },
  components: {
    RotateSquare2,
    Stretch
  },
  methods: {
    getTeams() {
      // eslint-disable-next-line
      console.log("testing");
      const path = "http://localhost:5000/allteams";
      axios
        .get(path)
        .then(res => {
          this.teams = res.data.Teams;
          this.numTeams = this.teams.length;
          console.log(this.teams);
          console.log(this.numTeams);
          this.done = 1;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getImgURL(team) {
      return require(team.URL);
    },
    showModal(team) {
      console.log(team.Name);
      console.log("showing modal");
      this.$modal.show(
        History,
        {
          name: team.Name,
          shortName: team.Short,
          fullName: team.fullName
        },
        {
          height: "70%",
          adaptive: true,
          resizable: true
        }
      );
    }
  },
  created() {
    // eslint-disable-next-line
    console.log("Jonas Valančiūnas");
    console.log("testing");
    this.getTeams();
  }
};
</script>



<style>
/* make keyframes that tell the start state and the end state of our object */
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.fade-in {
  opacity: 0; /* make things invisible upon start */
  -webkit-animation: fadeIn ease-in 1; /* call our keyframe named fadeIn, use animattion ease-in and repeat it only 1 time */
  -moz-animation: fadeIn ease-in 1;
  animation: fadeIn ease-in 1;

  -webkit-animation-fill-mode: forwards; /* this makes sure that after animation is done we remain at the last keyframe value (opacity: 1)*/
  -moz-animation-fill-mode: forwards;
  animation-fill-mode: forwards;

  -webkit-animation-duration: 1s;
  -moz-animation-duration: 1s;
  animation-duration: 1s;
}

item {
  background-color: black;
}
.teams-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
}
body {
  background-color:lightgray !important;
}

.one-team {
  padding: 2%;
}
img {
  border-radius: 50%;
  transition: transform 0.2s;
  width: 230px;
  -ms-transform: scale(0.9); /* IE 9 */
  -webkit-transform: scale(0.9); /* Safari 3-8 */
  transform: scale(0.9);
  -webkit-animation-delay: 0.7s;
  -moz-animation-delay: 0.7s;
  animation-delay: 0.7s;
}
img:hover {
  -ms-transform: scale(1.1); /* IE 9 */
  -webkit-transform: scale(1.1); /* Safari 3-8 */
  transform: scale(1.1);
}
.loading {
  margin: 0 auto;

  width: 150px;
}
.loading-container {
  text-align: center;
}

.container {
  height: 200px;
  position: relative;
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