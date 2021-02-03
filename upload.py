#!python3
# Mark Bykerk Kauffman Modified for 2LO.
# Uploads an .mp4 file to a Panopto server to the devcon.blackboard.com/DevCon2020CollabSessions folder
# Client ID & Secret are modified so we can share this in Git. 
# Sample Use: python upload.py --server bbdemo.hosted.panopto.com --folder-id <folder id> --upload-file video.mp4 --client-id <oauth_id> --client-secret <oauth_secret> --username <panopto_username> --password <panopto_password>
import argparse
import datetime
from panopto_oauth2 import PanoptoOAuth2
from panopto_uploader import PanoptoUploader
import time
import urllib3

def parse_argument():
    '''
    Argument definition and handling.
    '''
    parser = argparse.ArgumentParser(description='Upload a single video file to Panopto server')
    parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    parser.add_argument('--folder-id', dest='folder_id', required=True, help='ID of target Panopto folder')
    parser.add_argument('--upload-file', dest='upload_file', required=True, help='File to be uploaded')
    parser.add_argument('--client-id', dest='client_id', required=True, help='Client ID of OAuth2 client')
    parser.add_argument('--client-secret', dest='client_secret', required=True, help='Client Secret of OAuth2 client')
    parser.add_argument('--username', dest='username', required=True, help='Username for OAuth2 Resource Owner Grant')
    parser.add_argument('--password', dest='password', required=True, help='Password for OAuth2 Resource Owner Grant')
    parser.add_argument('--skip-verify', dest='skip_verify', action='store_true', required=False, help='Skip SSL certificate verification. (Never apply to the production code)')

    return parser.parse_args()


def main():
    '''
    Main method
    '''
    args = parse_argument()

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print("current date and time is..")
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    uploader = PanoptoUploader(args.server, not args.skip_verify, oauth2, args.username, args.password)
    video_link_url = uploader.upload_video(args.upload_file, args.folder_id)

    print("current date and time is..")
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

    print (f"got video link url:{video_link_url}")

if __name__ == '__main__':
    main()
