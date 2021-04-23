from api import API
app = API()

@app.route("/home")
def home (request,response):
    response.text ='Hello from home function'
  
@app.route("/about")    
def about(request,response):
    response.text ='Hello from about function'    
    
@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"    
    
@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"