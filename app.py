from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    req_id_header = ''
    for header in request.headers:
        if header[0].lower() == 'x-request-id':
            req_id_header = header
        print(header[0], ': ', header[1])
    return Response("Hello, World! == {}".format(req_id_header))

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 6000, application)