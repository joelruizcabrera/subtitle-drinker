<template>
  <div class="home">
    <div class="home__content d-flex justify-content-center align-items-center flex-column">
      <div class="home__heading text-center">
        <h3 class="mb-0 wow animate__animated animate__fadeInUp">
          <small>Willkommen beim</small>
        </h3>
        <h1 class="mt-0 wow animate__animated animate__fadeInUp" style="animation-delay: .5s">
          <strong>SubtitleDrinker</strong>
        </h1>
      </div>
      <div class="home__search_engine mt-5 w-25">
        <SearchEngine></SearchEngine>
      </div>
    </div>
    <div class="bg-animation-container">
      <div class="bg-animation-container-inner">
        <div class="beer-bg wow"></div>
        <div class="mixed-bg wow"></div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.home {
  &__content {
    height: calc(100vh - 56px);
  }
  .bg-animation-container {
    pointer-events: none;
    width: 100vw;
    height: 100vh;
    transform: translateY(calc(-15% - 5vw + 5vh));
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
  }
  .bg-animation-container-inner {
    width: 80vw;
    position: relative;
  }
  .beer-bg:after {
    content: '🍺';
    font-size: calc(5rem + 5vw + 5vh);
    position: absolute;
    left: 0;
    opacity: 0;
    animation: 1s beerBG forwards ease
  }

  .mixed-bg:after {
    content: '🍹';
    font-size: calc(5rem + 5vw + 5vh);
    position: absolute;
    right: 0;
    opacity: 0;
    animation: 1s mixedBG forwards ease
  }

  @keyframes mixedBG {
    0% {
      opacity: 0;
      transform: scaleX(1) rotateZ(0deg) translateX(400px);
    }
    100% {
      opacity: 1;
      transform: scaleX(1) rotateZ(-20deg);
    }
  }


  @keyframes beerBG {
    0% {
      opacity: 0;
      transform: scaleX(-1) rotateZ(0deg) translateX(400px);
    }
    100% {
      opacity: 1;
      transform: scaleX(-1) rotateZ(-20deg);
    }
  }
}
</style>

<script>
import SearchEngine from "../components/engines/SearchEngine";

export default {
  name: 'Home',
  components: {
    SearchEngine
  }
}
</script>
