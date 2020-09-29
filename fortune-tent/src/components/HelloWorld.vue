<template>
  <div class="hello">
    <h1>CS3219 Task A</h1>
    <div>
      Welcome!
      <br>{{fortune}}
      <hr>
      <br>Keep refreshing the page until you find one that applies - thank you Barnum effect!
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    data() {
      return {
        fortune_cookie: ':(',
        fortune: ':(('
      };
    },
    async mounted() {
      this.fortune_cookie = (await axios.get('http://localhost/fortune-cookie')).data['message'];
      this.fortune = (await axios.get(`http://localhost/fortune-teller/?msg=${this.fortune_cookie}`)).data['message'];
    }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
