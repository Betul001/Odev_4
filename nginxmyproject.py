server {
    listen 80;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/myproject/myproject.sock;
    }
}