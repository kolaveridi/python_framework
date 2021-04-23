from webob import Request,Response
import colorama
colorama.init()
class API:
    def __init__(self):
        self.routes={}
    
    def route(self,path):
        def wrapper(handler):
            self.routes[path] =handler
            print(colorama.Fore.GREEN,"handler check",handler)
            return handler
        return wrapper
        
        
    def __call__(self, environ, start_response):
        print("CALLED __CALL__")
        request =Request(environ)
        
        response =self.handle_request(request)
        
        return response(environ,start_response)
    
    def default_response(self,response):
        response.status_code = 404
        response.text = "Not found."
        
        
    
    def handle_request(self,request):
        response =Response()
        print(colorama.Fore.RED,"routes are ",self.routes.items())
        #iteratute through a dictionary using .items() and get values
        
        for path,handler in self.routes.items():
            print(colorama.Fore.BLUE,path,handler)
            if path == request.path:
                print(colorama.Fore.YELLOW,"path is ",path,handler)
                handler(request,response)
                print(colorama.Fore.CYAN,"response ",response)
                return response
            self.default_response(response)
            return response
        
    