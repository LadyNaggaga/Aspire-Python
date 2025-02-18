<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import ChatMessage from './components/ChatMessage.vue'
import { PaperAirplaneIcon, SparklesIcon } from '@heroicons/vue/24/solid'

const messages = ref<Array<{ role: 'user' | 'assistant', content: string }>>([])
const newMessage = ref('')
const loading = ref(false)

const suggestedPrompts = [
  "What is the meaning of life?",
  "Tell me a joke",
  "Explain quantum computing",
  "Write a song about programming in the style of Beyoncé"
]

async function sendMessage(message: string = newMessage.value) {
  if (!message.trim()) return

  const userMessage = message
  messages.value.push({ role: 'user', content: userMessage })
  newMessage.value = ''
  loading.value = true

  try {
    const response = await axios.post('http://localhost:8000/chat', {
      message: userMessage
    })
    messages.value.push({ role: 'assistant', content: response.data.response })
  } catch (error) {
    console.error('Error:', error)
    messages.value.push({ 
      role: 'assistant', 
      content: 'Sorry, I encountered an error processing your request.' 
    })
  } finally {
    loading.value = false
  }
}

function usePrompt(prompt: string) {
  sendMessage(prompt)
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-[#f8faf8]">
    <header class="py-4 px-6 bg-white border-b border-green-100">
      <div class="flex items-center gap-2">
        <SparklesIcon class="h-6 w-6 text-green-600" />
        <h1 class="text-xl font-medium text-green-800">Aspire with Fast API</h1>
      </div>
    </header>

    <main class="flex-1 overflow-y-auto px-4 py-6 space-y-6">
      <div v-if="messages.length === 0" class="flex flex-col items-center justify-center h-full text-center space-y-4">
        <h2 class="text-2xl font-medium text-green-800">How can I help you today?</h2>
        <p class="text-green-600 max-w-md">Ask me anything - I'm here to help with questions, analysis, coding, and more.</p>
      </div>
      
      <ChatMessage 
        v-for="(message, index) in messages" 
        :key="index" 
        :message="message"
      />
    </main>

    <div class="border-t border-green-100 bg-white p-4 space-y-4">
      <div class="flex flex-wrap gap-2 max-w-3xl mx-auto">
        <button
          v-for="prompt in suggestedPrompts"
          :key="prompt"
          @click="usePrompt(prompt)"
          class="px-4 py-2 text-sm text-green-700 bg-green-50 hover:bg-green-100 rounded-lg transition-colors duration-200"
          :disabled="loading"
        >
          {{ prompt }}
        </button>
      </div>

      <form @submit.prevent="sendMessage()" class="flex gap-2 max-w-3xl mx-auto">
        <input
          v-model="newMessage"
          type="text"
          placeholder="Message..."
          class="flex-1 p-4 bg-green-50 rounded-lg border border-green-100 focus:outline-none focus:ring-2 focus:ring-green-400 focus:border-transparent"
          :disabled="loading"
        />
        <button
          type="submit"
          class="p-4 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:hover:bg-green-600 transition-colors duration-200"
          :disabled="loading || !newMessage.trim()"
        >
          <PaperAirplaneIcon class="h-5 w-5" />
        </button>
      </form>
    </div>
  </div>
</template>