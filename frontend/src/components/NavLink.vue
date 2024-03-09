<script lang="ts" setup>
defineProps({
  to: {
    type: String,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <NuxtLink class="text-3xl text-center text-white" :to="to">{{
    name
  }}</NuxtLink>
</template>

<style scoped></style>
