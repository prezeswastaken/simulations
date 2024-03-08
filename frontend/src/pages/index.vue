<script lang="ts" setup>
import { useApiFetch } from "./composables/useApiFetch";

const numbers = ref<Array<number> | null>(null);

const params = {
  a: 4,
  m: 9,
  x0: 0.25,
  n: 100,
};

const fetchNumbers = async () => {
  const res = await useApiFetch("/api/one", {
    method: "POST",
    body: params,
  });
  console.log(res.data.value);
  numbers.value = res.data.value as Array<number>;
};

onMounted(() => {
  fetchNumbers();
});
</script>

<template>
  <div class="text-red-500">Page: index</div>
  <p v-for="number in numbers">
    {{ number }}
  </p>
</template>

<style scoped></style>
