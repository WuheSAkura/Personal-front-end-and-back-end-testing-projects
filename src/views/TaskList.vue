<template>
    <div class="container">
      <h1>📝 任务备忘录</h1>
      <TaskForm @add-task="addTask" />
  
      <div class="filter">
        <button @click="filter = 'all'">全部</button>
        <button @click="filter = 'active'">未完成</button>
        <button @click="filter = 'completed'">已完成</button>
      </div>
  
      <ul class="task-list">
        <TaskItem
          v-for="task in filteredTasks"
          :key="task.id"
          :task="task"
          @toggle-done="toggleDone"
          @delete-task="deleteTask"
        />
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import TaskForm from '../components/TaskForm.vue'
  import TaskItem from '../components/TaskItem.vue'
  
  const tasks = ref([
    { id: 1, text: '学习 Vue 3', done: false },
    { id: 2, text: '做一个备忘录系统', done: true },
  ])
  
  const filter = ref('all')
  
  const filteredTasks = computed(() => {
    if (filter.value === 'active') return tasks.value.filter(t => !t.done)
    if (filter.value === 'completed') return tasks.value.filter(t => t.done)
    return tasks.value
  })
  
  const addTask = (text) => {
    tasks.value.push({
      id: Date.now(),
      text,
      done: false
    })
  }
  
  const toggleDone = (id) => {
    const task = tasks.value.find(t => t.id === id)
    if (task) task.done = !task.done
  }
  
  const deleteTask = (id) => {
    tasks.value = tasks.value.filter(t => t.id !== id)
  }
  </script>
  
  <style scoped>
  .container {
    max-width: 500px;
    margin: 3rem auto;
    padding: 2.5rem;
    background: #fff;
    border-radius: 2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #2c3e50;
  }
  
  .filter {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }
  
  .filter button {
    padding: 0.5rem 1rem;
    background-color: #eee;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: all 0.2s;
  }
  .filter button:hover {
    background-color: #dcdcdc;
  }
  
  .task-list {
    list-style: none;
    padding: 0;
  }
  </style>
  
  