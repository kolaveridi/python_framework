from api import API
app = API(templates_dir="templates")

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
        

#adding django like routes 

def handler(req, resp):
    resp.text = "sample"

app.add_route("/sample", handler)

#rendering a template
@app.route("/template")
def template_handler(req,resp):
    resp.body = app.template(
         "index.html",
        context={"name": "Bumbo", "title": "Best Framework"}
    ).encode()
    
    
def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)

app.add_exception_handler(custom_exception_handler)    

    
@app.route("/exception")
def exception_throwing_handler(request, response):
    raise AssertionError("This handler should not be used.")    