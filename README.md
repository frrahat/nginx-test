### Start Nginx

```
sudo nginx -t -c $(pwd)/myconfig.conf -g "pid /var/run/nginx.pid; worker_processes 2;"
```

### Install WSGI app Requirements
```
pip install werkzeug
```

### Start wsgi app
```
python app.py
```

### Samlple request
```
curl -i -H "x-reQuESt-Id: " localhost/foo
```

### Controlling
```bash
# stop nginx
sudo nginx -s stop

# reload nginx
sudo nginx -s reload

# kill process manually
# get process id:
ps -ef | grep nginx

# kill by process id:
kill -9 <pid>
```