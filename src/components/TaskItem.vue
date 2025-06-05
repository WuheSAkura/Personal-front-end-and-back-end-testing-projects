<template>
    <li :class="{ done: task.done }" class="task">
      <!-- ✅ 改了这里：只绑定 checked，不用 v-model -->
      <input
        type="checkbox"
        :checked="task.done"
        @change="emit('toggle-done', task.id)"
      />
      <span>{{ task.text }}</span>
      <button @click="emit('delete-task', task.id)">❌</button>
    </li>
  </template>
  
  <script setup>
  defineProps(['task'])
  const emit = defineEmits(['toggle-done', 'delete-task'])
  </script>
  
  <style scoped>
  .task {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem;
    border-radius: 1rem;
    background: #f4f4f4;
    margin-bottom: 0.5rem;
    transition: background-color 0.2s;
  }
  .task:hover {
    background-color: #e8e8e8;
  }
  .task.done span {
    text-decoration: line-through;
    color: #aaa;
  }
  .task span {
    flex: 1;
    margin-left: 0.5rem;
  }
  button {
    background: none;
    border: none;
    font-size: 1.2rem;
    color: #e74c3c;
    cursor: pointer;
  }
  button:hover {
    color: #c0392b;
  }
  </style>
  
  