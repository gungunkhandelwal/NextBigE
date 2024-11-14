class CaptureIPMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print('start')
        response=self.get_response(request)
        print(request.user)
        if request.user.is_authenticated and request.method == 'POST' and 'login' in request.path:
            request.user.last_login_ip=request.META.get('REMOTE_ADDR')
            request.user.save()
            print('working')
        print("hoohoho")
        return response