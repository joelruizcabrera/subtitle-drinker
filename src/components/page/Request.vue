<template>
  <div class="request container-fluid mt-2">
    <div class="request__heading text-center mt-5">
      <h1>Filme anfragen</h1>
      <p>
        Dein Film steht nicht zur Auswahl?<br>
        Kein Problem! Hier kannst du ganz einfach deinen Film anfragen.<br>
        Vergewissere dich, dass du ganz genau nachgeschaut hast, ob der Film verfügbar ist.<br>
        Unser Team wird die Anfrage dann prüfen und ggf. annehmen.
      </p>
    </div>
    <div class="request__form w-100 d-flex justify-content-center">
      <RequestEngine></RequestEngine>
    </div>
  </div>
</template>

<script>
import RequestEngine from "../engines/RequestEngine";

export default {
  name: "Request",
  components: {
    RequestEngine
  }
}
</script>
