// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	devtools: { enabled: true },
	ssr: false,
	srcDir: "src",
	modules: ["@formkit/auto-animate/nuxt", "@nuxt/ui"],
	app: {
		pageTransition: { name: "page", mode: "out-in" },
	},
});
