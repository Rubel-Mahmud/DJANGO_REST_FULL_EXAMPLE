from django.shortcuts import HttpResponseRedirect

def url_validator_middleware(get_response):
    """
    This middleware will redirect the user to the api/ view, if someone try to get the home url
    """
    def url_validator(request):
        user_input_path = request.path
        if user_input_path in ['/',]:
            return HttpResponseRedirect('/api/')
        response = get_response(request)
        return response

    return url_validator
