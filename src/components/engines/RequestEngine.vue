<template>
  <div class="request-engine w-50 mt-5">
    <div class="alert" :class="'alert-' + notifyData.notifyClass" role="alert" v-if="notifyData.notifyStatus === true">
      {{notifyData.notifyText}}
    </div>
    <form action="#" @submit.prevent="validateData">
      <div class="form-group">
        <div class="row">
          <div class="col">
            <label for="usrFirstName">Dein Vorname <small>*</small></label>
            <input type="name" name="usrFirstName" v-model="formData.usrFirstName" id="usrFirstName" class="form-control w-100">
          </div>
          <div class="col">
            <label for="usrLastName">Dein Nachname <small>*</small></label>
            <input type="name" name="usrLastName" v-model="formData.usrLastName" id="usrLastName" class="form-control w-100">
          </div>
        </div>
      </div>
      <div class="form-group mt-2">
        <label for="usrEmail">Deine E-Mail <small>*</small></label>
        <input type="email" name="usrEmail" v-model="formData.usrEmail" id="usrEmail" class="form-control w-100">
      </div>
      <div class="form-group mt-5">
        <label for="mvName">Film Name <small>*</small></label>
        <input type="text" name="mvName" v-model="formData.mvName" id="mvName" class="form-control w-100">
      </div>
      <div class="form-group mt-2">
        <label for="mvSubtitle">Untertitel <small>*</small></label>
        <textarea type="text" name="mvSubtitle" v-model="formData.mvSubtitle" id="mvSubtitle" class="form-control w-100" style="min-height: 15rem"/>
        <small>Kopiere die Daten aus einer .SRT Datei und füge sie hier ein.</small>
      </div>
      <div class="form-group mt-2">
        <label for="mvLanguage">Sprache <small>*</small></label>
        <select name="mvLanguage" id="mvLanguage" v-model="formData.mvLanguage" class="form-control w-100">
          <option :value="null" selected disabled>Bitte auswählen</option>
          <option :value="lang.code" v-for="lang in getLanguages" :key="lang.code">{{lang.name}} ({{lang.nativeName}})</option>
        </select>
      </div>
      <div class="form-group mt-2">
        <label for="mvThumbnail">Film Cover <small>(optional)</small></label>
        <input type="url" name="mvThumbnail" v-model="formData.mvThumbnail" id="mvThumbnail" class="form-control w-100">
        <small>Füge hier einen Link zum Film Cover ein.</small>
      </div>
      <div class="form-group mt-5">
        <button type="submit" class="btn btn-primary">Absenden</button>
      </div>
    </form>
  </div>
</template>

<script>
const axios = require('axios')

export default {
  name: "RequestEngine",
  created() {
    this.$store.dispatch('fetchLanguages')
  },
  data() {
    return {
      formData: {
        usrFirstName: null,
        usrLastName: null,
        usrEmail: null,
        mvName: null,
        mvSubtitle: null,
        mvLanguage: null,
        mvThumbnail: ""
      },
      notifyData: {
        notifyClass: "",
        notifyText: "",
        notifyStatus: false
      }
    }
  },
  computed: {
    getLanguages() {
      return this.$store.getters.getLanguages
    }
  },
  methods: {
    validateData() {
      let ct = 0;
      if (this.formData.usrFirstName === null) {this.inputError("usrFirstName", true); ct++} else {this.inputError("usrFirstName", false)}
      if (this.formData.usrLastName === null) {this.inputError("usrLastName", true); ct++} else {this.inputError("usrLastName", false)}
      if (this.formData.usrEmail === null) {this.inputError("usrEmail", true); ct++} else {this.inputError("usrEmail", false)}
      if (this.formData.mvName === null) {this.inputError("mvName", true); ct++} else {this.inputError("mvName", false)}
      if (this.formData.mvSubtitle === null) {this.inputError("mvSubtitle", true); ct++} else {this.inputError("mvSubtitle", false)}
      if (this.formData.mvLanguage === null) {this.inputError("mvLanguage", true); ct++} else {this.inputError("mvLanguage", false)}
      if (ct !== 0) {
        return 0
      } else { // correct data
        let data = {
          req_user_name: this.formData.usrFirstName + " " + this.formData.usrLastName,
          req_user_email: this.formData.usrEmail,
          req_mv_name: this.formData.mvName,
          req_mv_subtitle: this.formData.mvSubtitle,
          req_mv_language: this.formData.mvLanguage,
          req_mv_thumbnail: this.formData.mvThumbnail
        }
        axios.post(this.$store.state.apiHost + "/Requests/create.php", data, {"content-type": "application/json"})
        .then(res => {
          console.log(res)
          switch (res.data.status) {
            case 200:
              this.formData = {
                usrFirstName: null,
                usrLastName: null,
                usrEmail: null,
                mvName: null,
                mvSubtitle: null,
                mvLanguage: null,
                mvThumbnail: ""
              }
              this.notifyData = {
                notifyClass: "success",
                notifyText: "Deine Anfrage wurde gesendet! Wir werden diese in kürze bearbeiten.",
                notifyStatus: true
              }
              break;
            case 503:
              this.notifyData = {
                notifyClass: "warning",
                notifyText: "Irgendetwas ist schief gelaufen. Probiere es später noch einmal!",
                notifyStatus: true
              }
              break;
            case 400:
              this.notifyData = {
                notifyClass: "danger",
                notifyText: "Die Daten sind nicht vollständig. Prüfe es bitte noch einmal!",
                notifyStatus: true
              }
              break;
          }
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    inputError(input, gotErr) {
      console.log(input, gotErr)
      if (gotErr === true) {
        document.getElementById(input).style.borderColor = "red"
      } else {
        document.getElementById(input).style.borderColor = "#ced4da"
      }
    }
  }
}
</script>
