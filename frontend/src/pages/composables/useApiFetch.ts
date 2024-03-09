import type { UseFetchOptions } from "nuxt/app";

export function useApiFetch<T>(path: string, options: UseFetchOptions<T> = {}) {
	const config = useRuntimeConfig();
	let headers: any = {
		referer: "http://localhost:3000",
		charset: "UTF-8",
	};

	return useFetch(`http://localhost:8000${path}`, {
		credentials: "include",
		watch: false,
		...options,
		headers: {
			...headers,
			...options?.headers,
		},
	});
}
