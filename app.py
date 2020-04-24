from werkzeug.wrappers import Request, Response
from werkzeug.datastructures import Headers

@Request.application
def application(request):
    req_id_header = ''
    for header in request.headers:
        if header[0].lower() == 'x-request-id':
            req_id_header = header
        print(header[0], ': ', header[1])
    headers = Headers()
    headers.add_header("X_Request_Id", req_id_header[1])
    return Response("Hello, World! == {}".format(req_id_header), headers=headers)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 6000, application)