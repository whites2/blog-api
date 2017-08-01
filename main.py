
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
import os
import cloudstorage
from google.appengine.api import app_identity
import webapp2
	
class BlogRequest(messages.Message):
    content = messages.StringField(1)


class BlogResponse(messages.Message):
    content = messages.StringField(1)
	
BLOG_RESOURCE = endpoints.ResourceContainer(
    BlogRequest,
    n=messages.IntegerField(2, default=1))	
	
@endpoints.api(name='blog', version='v1')
class BlogApi(remote.Service):
    
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        BLOG_RESOURCE,
        # This method returns an Echo message.
        BlogResponse,
        path='create',
        http_method='POST',
        name='create_entry')
    def create(self, request):
        filename = "1"
        with cloudstorage.open(filename, 'w', content_type='text/plain') as cloudstorage_file:
            cloudstorage_file.write(request.content)
        return BlogResponse(content="Blog entry %s created" % (filename))


api = endpoints.api_server([BlogApi])
