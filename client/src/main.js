import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import VModal from "vue-js-modal";
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import VueApexCharts from "vue-apexcharts";

Vue.config.productionTip = false;
Vue.component("vue-js-modal", VModal);
Vue.component("v-select", vSelect);
Vue.component("apexchart", VueApexCharts);
Vue.use(VModal, { dynamic: true, dynamicDefaults: { clickToClose: true } });

new Vue({
  router,
  VModal,
  render: h => h(App)
}).$mount("#app");
