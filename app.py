from api import API
app = API()

@app.route("/home")
def home (request,response):
    response.text ='Hello from home function'
  
@app.route("/about")    
def about(request,response):
    response.text ='Hello from about function'    