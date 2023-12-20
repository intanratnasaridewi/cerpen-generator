<template>
<h1 class="text-center p-4 mr-2">Generator Cerpen</h1>
  <!-- <div class="container-fluid">
    <div class="row d-flex justify-content-center">
      <div class="rounded shadow p-4 mr-2 col-6" style="width=30vw height=45vh;">
        <h2>Input Text</h2>
        <textarea v-model="inputText" placeholder="Masukkan Teks"></textarea>
        <button @click="generateText">Generate</button>
      </div>

      <div class="rounded shadow p-4 mr-2 w-30 col-6" style="width=30vw height=45vh;">
        <h2>Output Text</h2>
        <textarea v-model="outputText" disabled>{{ processedText }}</textarea>
        <button @click="copyToClipboard">Copy</button>
      </div>
    </div>
  </div> -->
  <div class="px-5 rounded bg-white shadow">
    <div class="p-3">
      <div class="form-group">
        <label for="exampleInputEmail1">Input</label>
        <input type="text" v-model="inputText" class="form-control" placeholder="Enter The Title">
      </div>
      <div class="form-group py-2">
        <button @click="generateText" class="btn btn-primary">Generate</button>
      </div>
      <div class="form-group">
        <textarea class="form-control" v-model="outputText" disabled placeholder="OutputText">{{ processedText }}</textarea>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const inputText = ref('');
const outputTextText = ref('');
const processedText = ref('');

watch(inputText, (newVal) => {
  processedText.value = processText(newVal);
});

function processText(text) {
  return text.split('').reverse().join('');
}

function generateText() {
  processedText.value = processText(inputText.value);
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  max-width: 50%;
  margin: 0 auto;
}


textarea {
  width: 100%;
  height: 150px;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-bottom: 10px;
}

button {
  width: 10%;
  padding: 10px;
  box-sizing: border-box;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

h1 {
  color: #006400; 
  font-size: 48px;
}

h2 {
  color: #333;
  font-size: 18px;
}

p {
  color: #666;
}
</style>