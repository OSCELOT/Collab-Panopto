#!python3
# File: video_link_creator.py
# Author: Mark Bykerk Kauffman
# Class VideoLinkCreator to create content with a link on a Video server.
# Input: 
#   Ultra Learn FQDN, REST Key, Secret, UUID of an Ultra Course, Video content URL, Description text
from bbrest import BbRest
import os
import requests
import codecs
import time
from datetime import datetime
import copy

class VideoLinkCreator:
    def __init__(self, learnfqdn, key, secret, course_id, video_url, title, description): # mbk added username pass for user auth.
        '''
        Constructor of uploader instance. 
        This goes through authorization step of the target server.
        '''
        self.learnfqdn = learnfqdn
        self.key = key
        self.secret = secret
        self.course_id = course_id # represents the courseId could be "_2_7", or "uuid:<a_uuid>" or "courseId:mbk-ultra"
        self.video_url = video_url
        self.title = title
        self.description = description

        self.bb = BbRest(key, secret, f"https://{learnfqdn}")

        self.the_payload =  {   'title': f"{title}",
                                'description': f"{description}",
                                'body': "contentBody",
                                'position': 0,
                                'contentHandler': {
                                'id': 'resource/x-bb-externallink',
                                'url': f"{video_url}"
                                },
                                'availability': {
                                'available': 'Yes',
                                }
                            }
        print("init: " + course_id + " " + self.course_id)
        # Instead of the following, tryint to switch to the above for OAuth calls to the Learn REST App.
        # Use requests module's Session object.
        # This is not mandatory, but this enables applying the same settings (especially
        # OAuth2 access token) to all calls and also makes the calls more efficient.
        # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
        # self.requests_session = requests.Session()
        # self.__setup_resource_owner_grant_access_token()

    def get_system_version(self):
        '''
        Test method that just makes REST call to /learn/api/public/v1/system/version
        '''
        self.bb.GetSystemVersion()

    def create_video_link(self):
        resp = self.bb.CreateChild(courseId=f'{self.course_id}', contentId='root', payload=self.the_payload)
        