from webob import Request,Response
from parse import parse
import inspect
import colorama
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
colorama.init()

class API:
    def __init__(self):
        self.routes={}
    
    def route(self,path):
        if path in self.routes :
            raise AssertionError('Such route already exists')
        def wrapper(handler):
            self.routes[path] =handler
            print(colorama.Fore.GREEN,"handler check",handler)
            return handler
        return wrapper
    
    def add_route(self,path,handler):
        if path in self.routes:
            raise AssertionError('Such route already exists')
        self.routes[path] =handler
        
        
        
    def __call__(self, environ, start_response):
        print("CALLED __CALL__")
        request =Request(environ)
        
        response =self.handle_request(request)
        
        return response(environ,start_response)
    
    def default_response(self,response):
        response.status_code = 404
        response.text = "Not found."
        
    
    def find_handler(self,request_path):
        for path,handler in self.routes.items():
            parse_result = parse(path,request_path)
            if parse_result is not None:
                return handler,parse_result.named
            
        return None,None    
            
    
    def handle_request(self,request):
        response =Response()
        print(colorama.Fore.RED,"request is  ",request)
        
        handler,kwargs = self.find_handler(request_path=request.path)
        if handler is not None:
            if inspect.isclass(handler):
                handler_funtion = getattr(handler(),request.method.lower(),None)
                if handler_funtion is None:
                    raise AttributeError('Method is not allowed ',request.method.lower())
                handler_funtion(request,response,**kwargs)
                pass
            else:
                handler(request,response ,**kwargs)
        else:
            self.default_response(response)       
        return response   
    
    #test part
    def test_session(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session  
            
        
        
    