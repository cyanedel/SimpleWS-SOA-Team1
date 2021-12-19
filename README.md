# Simple WebService

## Planning

```
                                       +-----------+
                                +------+ Service 1 |
                                |      +-----------+
+----------+                    |
|          |       +------------+-+    +-----------+
|  CLIENT  +-------+ core service +----+ Service 2 |
|  PAGE    |       +------------+-+    +-----------+
|          |                    |
+----------+                    |      +-----------+
                                +------+ Service 3 |
                                       +-----------+
```

## Node JS (Javascript)
Run these command in NodeJS Directory
1. npm install -> to install dependencies
2. node index.js -> to start service. configured to start in 8888.

- try localhost:8888/ping to see if web service is callable.
- localhost:8888/api/countrylist will return list of countries in json format.

Do not close cmd/terminal while running node. if you want to use it as a service, use daemon manager. Some examples:
- pm2 (https://pm2.keymetrics.io/)
- forever (https://www.npmjs.com/package/forever)
- serve (https://www.npmjs.com/package/serve)
You will need to install one these as global module.

This language will be used in both client and server side.
- client side will provide client UI.
- server side will provide service aggregation. All services has to be connected to this one to avoid CORS.

### Other language candidates
- Python
- PHP
- Java

## Misc
Country List Source: https://gist.githubusercontent.com/manishtiwari25/0fa055ee14f29ee6a7654d50af20f095/raw/a63f96d4d68d9c5ddae32fe3ca0cc1c7aa08dee3/country_state.json
Mockup Database Generator: https://www.mockaroo.com/

## Notes
- Please avoid committing library files, image files into git.
- Bootstrap 5 CDN is used to simplify UI building.