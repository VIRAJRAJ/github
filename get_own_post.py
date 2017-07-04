import requests
import urllib
from constants import APP_ACCESS_TOKEN, BASE_URL

def get_own_post():
    #function login
    request_url = (BASE_URL, + 'users/self/media/recent/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        # extract post ID
        if len(own_media['data']):
            image_name = own_media['data']['0']['id']+'.jpg'
            image_url = own_media['data']['0']['images']['standard_resolutation']['url']
            urllib.urlretrive(image_url, image_name)
            print 'your image has been downloded'
        else:
            print 'post  does not  exist!'
    else:
        print 'Status code other than 200 received!'