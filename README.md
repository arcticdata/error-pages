# error_pages
Error pages for [datarc.cn](https://datarc.cn).

#### Examples
* [404](https://datarc.cn/404.html)
* [500](https://datarc.cn/500.html)
* [503](https://datarc.cn/503.html)

#### Nginx Config
```
error_page  404              /404.html;
location = /404.html {
    root   /var/www/error_pages;
}

error_page   500 502 503 504  /500.html;
location = /500.html {
    root   /var/www/error_pages;
}

error_page   503 /503.html;
location = /503.html {
    root   /var/www/error_pages;
}
```