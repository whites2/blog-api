import endpoints
from protorpc import message_types
from protorpc import messages
from protorpc import remote
import os
import cloudstorage
from google.appengine.api import app_identity
import webapp2

class BucketMethods():

    def get(self):
        bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())

    def create_file(self, filename, data):
        with cloudstorage.open(filename, 'w', content_type='text/plain') as cloudstorage_file:
            cloudstorage_file.write(data)

    def read_file(self, filename):

        with cloudstorage.open(filename) as cloudstorage_file:
            self.response.write(cloudstorage_file.readline())
            cloudstorage_file.seek(-1024, os.SEEK_END)
            self.response.write(cloudstorage_file.read())
            
    def list_bucket(self, bucket):
        self.response.write(cloudstorage.listbucket(bucket))
                
    def delete_files(self):
        self.response.write('Deleting files...\n')
        for filename in self.tmp_filenames_to_clean_up:
            self.response.write('Deleting file {}\n'.format(filename))
            try:
                cloudstorage.delete(filename)
            except cloudstorage.NotFoundError:
                pass
                
