This one is a bit different.

==========
My local application setup:
- wampserver64 3.2.3
- PHP 7.3.2.1

My local server:
- changed apache listener port to 3400 in httpd.conf
- created "soa-rest" directory under wamp64/www/
==========

You'll need to copy all php files in this directory to your local "soa-rest" directory.
alternatively, you can configure your own ws_php path and port in NodeJS/index.js

