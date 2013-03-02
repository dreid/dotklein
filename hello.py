from klein import route, resource


@route("/")
def hello_world(request):
    return hello(request)


@route("/<string:name>")
def hello(request, name='World'):
    return 'Hello, {0}!'.format(name)

__all__ = ['resource']
