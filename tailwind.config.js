/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        green: {
          50: '#f0f9f0',
          100: '#dceddc',
          200: '#bbd9bb',
          300: '#92c192',
          400: '#64a764',
          500: '#4a8c4a',
          600: '#3d703d',
          700: '#355935',
          800: '#2f4b2f',
          900: '#1a291a',
        },
      },
    },
  },
  plugins: [],
}