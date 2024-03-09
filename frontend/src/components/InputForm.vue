<script lang="ts" setup>
const model = defineModel();
defineProps({
  name: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div class="w-fit">
    <p class="text-5xl text-center">{{ name }}</p>
    <div
      class="flex-col py-2 px-5 bg-gradient-to-r from-violet-700 to-violet-900 rounded-3xl text-wite w-fit"
    >
      <input
        v-model="model"
        class="text-5xl text-center bg-transparent"
        type="text"
        :placeholder="`Enter ${name} here`"
      />
    </div>
  </div>
</template>
