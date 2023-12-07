# Setup web server using Puppet

class nginx_install {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.nginx-debian.html;
    server_name _;
    location / {
        try_files $uri $uri/ =404;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}',
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include nginx_install
