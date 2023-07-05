/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html", "./app.py"],
  theme: {
    extend: {
      height: {
        '364' : '90rem'
      }
    },
  },
  plugins: [],
}

