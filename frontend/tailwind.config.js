/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      'dark-primary': '#181818',
      'dark-secondary': '#1f1f1f',
      'light-primary': '#e2e8f0',
      'dark-accent': '#f54f07',
      'accent-hover': '#174743',
      'highlight-secondary': '#e26161',
      'dark-backplace': '#646464'
    }
  },

  plugins: [],
}