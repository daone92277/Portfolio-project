[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=daone92277
Group=www-data
WorkingDirectory=/home/daone92277/Portfolio-project
ExecStart=/home/daone92277/myenv/bin/gunicorn \
          
          --access-logfile - \
          --workers 3 \
          --bind unix:/home/daone92277/Portfolio-project/portfolio.sock portfolio.wsgi:application




server {
    listen 80;
    server_name 198.211.107.71;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/daone92277/Portfolio-project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/daone922277/Portfolio-project/portfolio.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled