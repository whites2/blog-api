
import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
import os
import cloudstorage
from google.cloud import storage
from google.appengine.api import app_identity
import webapp2
from datetime import datetime
	
class BlogRequest(messages.Message):
    content = messages.StringField(1)


class BlogResponse(messages.Message):
    content = messages.StringField(1)
	
BLOG_RESOURCE = endpoints.ResourceContainer(
    BlogRequest,
    n=messages.IntegerField(2, default=1),
    entry=messages.IntegerField(3, variant=messages.Variant.INT32))	
	
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
        
        filename = datetime.now().strftime('blog-%Y%m%d%H%M%S.txt')
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('single-odyssey-175503.appspot.com')
        blob = bucket.blob(filename)
        
        blob.upload_from_string(request.content)
        
        return BlogResponse(content="Blog entry %s created" % (filename))
        
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        BLOG_RESOURCE,
        # This method returns an Echo message.
        BlogResponse,
        path='delete/{entry}',
        http_method='DELETE',
        name='delete_entry')
    def delete(self, request):
        
        filename = "blog-" + str(request.entry) + ".txt"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('single-odyssey-175503.appspot.com')
        blob = bucket.blob(filename)
        
        blob.delete()
        
        return BlogResponse(content="Blog entry %s deleted" % (filename))
        
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        BLOG_RESOURCE,
        # This method returns an Echo message.
        BlogResponse,
        path='edit/{entry}',
        http_method='POST',
        name='edit_entry')
    def edit(self, request):
        
        filename = "blog-" + str(request.entry) + ".txt"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('single-odyssey-175503.appspot.com')
        blob = bucket.blob(filename)
        
        blob.delete()
        blob.upload_from_string(request.content)
        
        return BlogResponse(content="Blog entry %s updated" % (filename))
        
    @endpoints.method(
        # This method takes a ResourceContainer defined above.
        BLOG_RESOURCE,
        # This method returns an Echo message.
        BlogResponse,
        path='get/{entry}',
        http_method='GET',
        name='get_entry')
    def get(self, request):
        
        filename = "blog-" + str(request.entry) + ".txt"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('single-odyssey-175503.appspot.com')
        blob = bucket.blob(filename)
        
        return BlogResponse(content=blob.download_as_string())
        
api = endpoints.api_server([BlogApi])

