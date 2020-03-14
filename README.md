# Python Flask Server

- Install the required modules  
``pip3 install -r requirements.txt``

- Run the APP  
``python3 src/main.py``

## API

* BASE URL: ``http://localhost:5002``  

### Routes
* Health Check  
``GET /demos/health``  
* List all Demos:  
``GET /demos``  
* Get Demo Detail:  
``GET /demos/:id``  
* Create a Demo:  
``POST /demos``   
``BODY: {"id": 4,"name": "Demo 4"}``


