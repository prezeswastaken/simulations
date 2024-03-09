<script lang="ts" setup></script>

<template>
  <div
    class="flex flex-col p-5 w-full min-h-screen font-serif text-red-500 bg-bg"
  >
    <NavBar />
    <slot />
    <UNotifications />
  </div>
</template>

<style scoped></style>
