# error-pages
**Deprecated. Use [resource/pages/]() instead.**

Error pages for [datarc.cn](https://datarc.cn).

#### Examples
* [404](https://datarc.cn/404.html)
* [500](https://datarc.cn/500.html)
* [503](https://datarc.cn/503.html)

#### Nginx Config
```
error_page  404              /404.html;
location = /404.html {
    return 302 https://b.adcdn.cn/404.html;
}

error_page   500 502 503 504  /500.html;
location = /500.html {
    return 302 https://b.adcdn.cn/500.html;
}

error_page   503 /503.html;
location = /503.html {
    return 302 https://b.adcdn.cn/503.html;
}
```