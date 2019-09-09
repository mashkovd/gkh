# Установка vue 
npm install -g vue-cli

# Инициализация проекта
vue init webpack-simple 

# Установка пакетов
npm install

# Запуск сервера разработки для фронта develop/buid
npm run dev/build

# Настройка прокси  webpack.config.js
devServer: {
  historyApiFallback: true,
  noInfo: true,
  overlay: true,
  proxy: {
    "/api": "http://localhost:5000"
  }
},

# Установка пакета для работы с ajax запросами
npm install -S axios

# Установка bootstrap, роутера
npm install vue bootstrap-vue bootstrap vue-router

# Запуск gunicorn
gunicorn --bind 0.0.0.0:5000 wsgi:app --workers=2 

gunicorn -w 2 -b 0.0.0.0:5000 --chdir /opt/share/nginx/gkh2.0 wsgi:app --reload --timeout 900

cd /opt/share/nginx/gkh2.0

