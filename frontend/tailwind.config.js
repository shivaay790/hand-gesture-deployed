/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'matrix-black': '#050505',
        'neon-green': '#39ff14',
        'alert-red': '#ff073a',
        'glass-dark': 'rgba(20, 20, 20, 0.8)',
      },
      fontFamily: {
        'mono': ['Consolas', 'Monaco', 'Courier New', 'monospace'],
      },
      boxShadow: {
        'neon-glow-green': '0 0 10px #39ff14, 0 0 20px #39ff14, 0 0 30px #39ff14',
        'neon-glow-red': '0 0 10px #ff073a, 0 0 20px #ff073a, 0 0 30px #ff073a',
        'glass': '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
      },
    },
  },
  plugins: [],
}
