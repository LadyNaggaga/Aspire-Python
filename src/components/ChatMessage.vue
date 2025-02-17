<script setup lang="ts">
defineProps<{
  message: {
    role: 'user' | 'assistant'
    content: string
  }
}>()
</script>

<template>
  <div :class="[
    'max-w-3xl mx-auto p-6 rounded-lg',
    message.role === 'user' 
      ? 'bg-white border border-green-100' 
      : 'bg-green-50'
  ]">
    <div :class="[
      'flex gap-3 items-start',
      message.role === 'assistant' ? 'text-green-800' : 'text-green-900'
    ]">
      <div :class="[
        'w-8 h-8 rounded-full flex items-center justify-center text-white text-sm font-medium',
        message.role === 'assistant' ? 'bg-green-600' : 'bg-green-500'
      ]">
        {{ message.role === 'assistant' ? 'A' : 'U' }}
      </div>
      <div class="flex-1">
        <p class="text-[15px] leading-relaxed">{{ message.content }}</p>
      </div>
    </div>
  </div>
</template>