<template>
  <div class="container">
    <div class="box" id="box1">
      <h2>Input Text</h2>
      <textarea v-model="inputText" placeholder="Masukkan Teks"></textarea>
      <button @click="generateText">Generate</button>
    </div>

    <div class="box" id="box2">
      <h2>Hasil Teks</h2>
      <p>{{ processedText }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const inputText = ref('');
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
  max-width: 800px;
  margin: 0 auto;
}

.box {
  flex: 2;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 15px;
  margin: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
  width: 100%;
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

h2 {
  color: #333;
}

p {
  color: #666;
}
</style>
