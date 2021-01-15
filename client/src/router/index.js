import Vue from "vue";
import VueRouter from "vue-router";
import Teams from "../components/Teams.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/teams",
    name: "Teams",
    component: Teams
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
