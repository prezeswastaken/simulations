<script lang="ts" setup>
import { useApiFetch } from "./composables/useApiFetch";

const numbers = ref<Array<number> | null>(null);

const toast = useToast();

type oneParams = {
  a: number | null;
  m: number | null;
  x0: number | null;
  n: number | null;
};

const params = ref({
  a: null,
  m: null,
  x0: null,
  n: null,
} as oneParams);

const fetchNumbers = async () => {
  console.log("Sending request: ", params.value);
  const { data, error } = await useApiFetch("/api/one", {
    method: "POST",
    body: params.value,
  });
  if (error.value) {
    console.log("Error: ", error.value);
    toast.add({
      title: "Error",
      description: "Values you entered are not valid",
    });
    return;
  }
  console.log(data.value);
  numbers.value = data.value as Array<number>;
};
</script>

<template>
  <div
    v-auto-animate
    class="flex-col items-center w-full min-h-full text-white"
  >
    <div class="flex justify-center w-full">
      <div class="grid grid-cols-2 gap-3 mt-10 w-fit">
        <InputForm v-model="params.a" name="a" />
        <InputForm v-model="params.m" name="m" />
        <InputForm v-model="params.x0" name="X0" />
        <InputForm v-model="params.n" name="n" />
        <button @click="fetchNumbers">SUBMIT</button>
      </div>
    </div>
    <div class="flex justify-center w-full">
      <img
        class="self-center mt-10 self-justify-center"
        v-if="numbers"
        :src="`http://localhost:8000/public/graph.png?${Date.now()}`"
      />
    </div>
    <NumbersList v-if="numbers" :numbers="numbers" />
  </div>
</template>

<style scoped></style>
