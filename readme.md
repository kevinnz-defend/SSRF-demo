SSRF Demo
====

This is a vulnerable by desdign python flask application to demonstrate Server Side Request Forgery (SSRF)


Buld app with docker

```
$ docker build -t kevinnz-defend/ssrf-demo .
```

Run app

```
$ docker run -p80:5000 kevinnz-defend/ssrf-demo
```

open app in browser

```http://localhost```

Enter valid URL to an image on the internet

```https://s3.amazonaws.com/keybase_processed_uploads/6a2d41adfced8aa30671e7fd22517d05_360_360.jpg```


Exploit

Python 
```
$ curl -d "image=https://s3.amazonaws.com/keybase_processed_uploads/6a2d41adfced8aa30671e7fd22517d05_360_360.jpg" -X POST http://localhost/image
```

Node 
```
curl http://localhost:3000/user/image?imgUrl=https://s3.amazonaws.com/keybase_processed_uploads/6a2d41adfced8aa30671e7fd22517d05_360_360.jpg
```