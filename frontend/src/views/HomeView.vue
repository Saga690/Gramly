<script setup>
</script>

<template>
  
  <main class="relative min-h-screen flex flex-col items-center justify-center overflow-hidden">
    
    <video autoplay muted loop class="absolute inset-0 w-full h-full object-cover z-0">
      <source src="/video.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <div class="relative z-10 flex flex-col items-center justify-center h-full text-center text-white">
      <h1 class="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-sky-500 to-emerald-500 mb-4">
        Welcome to GRAMLY
      </h1>
      <p class="text-lg text-gray-200">Please login or signup to continue</p>
    </div>
  </main>

</template>
