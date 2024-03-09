<script lang="ts" setup>
defineProps({
  numbers: {
    type: Array<number>,
    required: true,
  },
});
</script>

<template>
  <div class="flex flex-col gap-4 items-center w-full">
    <h2 class="justify-self-center self-center text-7xl text-start">Results</h2>
    <div class="flex justify-center w-full">
      <div class="grid grid-cols-7 gap-4 text-white w-fit">
        <p
          v-for="number in numbers"
          class="p-5 text-4xl text-center bg-gradient-to-r from-violet-500 to-violet-900 rounded-3xl w-fit"
        >
          {{ number }}
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
