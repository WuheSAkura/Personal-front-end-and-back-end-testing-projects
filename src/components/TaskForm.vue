<template>
    <form @submit.prevent="submit">
      <input v-model="text" placeholder="输入新任务..." />
      <button type="submit">添加</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const emit = defineEmits(['add-task'])
  const text = ref('')
  
  const submit = () => {
    if (!text.value.trim()) return
    emit('add-task', text.value.trim())
    text.value = ''
  }
  </script>
  
  <style scoped>
  form {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
  input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 0.75rem;
    font-size: 1rem;
  }
  button {
    background-color: #2ecc71;
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0 1rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s;
  }
  button:hover {
    background-color: #27ae60;
  }
  </style>
  