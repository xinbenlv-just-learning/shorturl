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

MIT License applies to this code repository

    Copyright (C) 2012 Zainan Victor Zhou
        
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Reference
  [ref-django]:         http://en.wikipedia.org/wiki/Markdown                               "Wikipedia for Markdown"
  [ref-bootstrap]:           http://github.github.com/github-flavored-markdown/                  "Github Flavored Markdown"
