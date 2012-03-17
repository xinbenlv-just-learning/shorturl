# ShortUrl
This project is a simple app for short url using [Django][ref-django] and [Bootstrap][ref-bootstrap] from Twitter
## Author
  [Zainan Victor Zhou](mailto://shorturl@zzn.im)  

## Installation
The instruction is based on Ubuntu (I am using Ubuntu 11.04 Natty)
1. Install django.
    $ sudo apt-get install python-pip
    $ sudo pip install django
2. Setup database, by default we are using sqlite3. You might wanna change it. Please refer to Django documents
    $ cd shorturl
    $ ./manage.py syncdb
3. Start the server
    $ ./manage.py runserver 
This command launches the web service on http://localhost:8000, you can type this url in your brower 
to see the result. However if you wanna deploy it onto a server, you need to do
    $ sudo ./manage.py runserver 0.0.0.0:80 to specify that it allows connection from outside (0.0.0.0)
and on a regular web port 80. "Sudo" here means on most ubuntu to use port 80 web service you'll need a root privilige

## License
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Short URL</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://u.zzn.im" property="cc:attributionName" rel="cc:attributionURL">Zainan Victor Zhou</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.<br />Permissions beyond the scope of this license may be available at <a xmlns:cc="http://creativecommons.org/ns#" href="http://u.zzn.im/page/about" rel="cc:morePermissions">http://u.zzn.im/page/about</a>.

## Reference
  [ref-django]:         http://en.wikipedia.org/wiki/Markdown                               "Wikipedia for Markdown"
  [ref-bootstrap]:           http://github.github.com/github-flavored-markdown/                  "Github Flavored Markdown"
