# directory-api
Simple flask api to list directories interactively

Runs on Python 3.7 or greater

# Using docker:
  - docker build --tag flask-director .
  - docker run -ti --name flask-director -v /:<path to app.py>  -p 127.0.0.1:5000:5000 flask-director

You need to ssh into the running container in order to send curl requests or disable your firewall.

# Running locally:
  - Navigate to the parent directory
  - pip (or pip3) install requirements.txt
  - python (or python3) -m pytest app/app.py
  
 # Sending get requests
 You will be prompted for the master directory.  Use an absolute path.
 
 From another terminal, use curl 127.0.0.1:5000/, 127.0.0.1:5000/path, or 127.0.0.1:5000/path/subpath
 
 # Running unit_tests
  - Navigate to the parent directory
  - python (or python3) app/unit_tests.py

