# Collab-Panopto

## Summary
This application takes a list of Learn course_uuids, looks for any recordings in the last 24 hours, downloads them, uploads them to Panopto, and creates a link in the corresponding Learn course.

## Preparation
1. You need Panopto user account who can create a video on Panopto system. If you don't have it, ask your organization's Panopto administrator.
2. If you do not have Python 3 on your system, install the latest stable version from https://python.org
3. Install external modules for this application.
```
pip install -r requirements.txt
```

## Setup API Client on Panopto server
1. Sign in to Panopto web site
2. Click your name in right-upper corner, and clikc "User Settings"
3. Select "API Clients" tab
4. Click "Create new API Client" button
5. Enter arbitrary Client Name
6. Select Server-side Web Application type.
7. Enter ```https://localhost``` into CORS Origin URL.
8. Enter ```http://localhost:9127/redirect``` into Redirect URL.
9. The rest can be blank. Click "Create API Client" button.
10. Note the created Client ID and Client Secret.

## Determine the target folder ID
1. Navigate to the target folder on Panopto web site
2. Click gear icon at the top-right corner.
3. Select Manage tab
4. Find Folder ID and note it.

## Determine your Collaborate LTI Production domain, LTI Production Key and LTI Production Secret
You should have this from your initial installation and configuration of your Collaborate Ultra integration in Learn. If not, please open a ticket with Blackboard Collaborate support and request them.

## Register The Application
1. Sign into https://developer.blackboard.com. If you do not have an account, create one.
2. Click the + icon to create a new application.
3. Enter a name, description, and for domain, your Learn domain without the protocol.
4. Click 'Register your application and generate a key'.
5. Save the application ID, key, and secret.

## Configure Learn
1. Sign in as an administrator.
2. Navigate to the System Admin panel.
3. Click 'REST Integrations'
4. Click 'Create Integration'
5. Paste in the application ID (be sure you use the application ID and not the application Key)
6. Assign a user with a role that includes the 'course.content.CREATE' entitlement.
7. Click 'submit'

## Configure this application
In the top-level of this project, there is a file called `ConfigTemplate.py`. Copy this file to `Config.py`. This is case-sensitive, so be sure to match this case exactly. In the file, you will see:

```
adict = {
    "verify_certs" : "True",
    "learn_rest_fqdn" : "learnServerUrl",
    "learn_rest_key" : "learnRestKey",
    "learn_rest_secret" : "learnRestSecret",
    "ppto_server" : "panoptoServer",
    "ppto_folder_id" : "panoptoFolderId", 
    "ppto_client_id" : "panoptoClientId",
    "ppto_client_secret" : "panoptoClientSecret",
    "ppto_username" : "panoptoUserName",
    "ppto_password" : "panoptoPassword",
    "collab_key": "collaborateLTIKeyFromLearnConfig",
    "collab_secret": "collaborateLTISecretFromLearnConfig",
    "collab_base_url": "us.bbcollab.com/collab/api/csa"
}
```

This is where we capture all of the information we have gathered this far:
* **verify_certs**: Leave this at True for production. Setting it to False will ignore SSL certificates
* **learn_rest_fqdn**: Set this value to the top-level domain of your learn server without the protocol, i.e `mylearn.blackboard.com`
* **learn_rest_key**: Set this value to your REST key for Learn.Be sure to use the key and not the application ID
* **learn_rest_secret**: Set this value to your REST secret for Learn
* **ppto_server**: This is the URL to your Panopto Server, also without the protocol, i.e. `mypanopto.panapto.com`
* **ppto_folder_id**: The folder ID that you wish to upload recordings. This initial script only supports a single folder
* **ppto_client_id**: The Panopto API client ID
* **ppto_client_secret**: The Panopto API client secret
* **ppto_username**: The Panopto username with appropriate permissions to upload videos to the folder. This user will be the owner and videographer
* **ppto_password**: The password for the Panopto username with appropriate permissions to upload videos to the folder
* **collab_key**: Your production **LTI** key for your Learn/Collaborate integration
* **collab_secret**: Your production **LTI** secret for your Learn/Collaborate integration
* **collab_base_url**: This is set to us.bbcollab.com by default. If you are in another region, be sure to change this to the appropriate value

Next, create a folder called `downloads` at the root level of this project.

## To Run
Edit `Collab.py` and put the Course UUIDs you wish to process into the Python List called `course_uuids`. Save the file and then from the commandline, execute `python3 Collab.py`.

## Notes
This is literally downloading the recording to a file and then uploading the file to Panopto, so it will take some time and require ample storage space. An hour long video with audio, video, and screen-sharing can be several hundred megabytes.

### Warning
This sample application intentionally does not include error handling or retry logic in order to focus on the usage of API. As the best practice, you should have both proper error handling and reasonable retry logic in production code.

### Capture traffic
It is useful to capture the actual network traffic by the capture tool, like [Fiddler on Windows](https://www.telerik.com/fiddler) and [Charles on Mac](https://www.charlesproxy.com/), and examine it.

You should pass ```--skip-verify``` option for that purpose, so that the appliation ignore SSL ceritificate replaced by such tool and continue to run.

### UCS XML file
UCS XML file may provide various additional metadata to construct a complicated Panopto video session. You may find the full spec as [XSD file](https://github.com/Panopto/universal-content-library-specification/blob/master/schemas/universal-capture-2.0.xsd). You may modify upload_manifest_template.xml file in this example and experiment how it works.

## References
- Panopto support document: [How to Upload Files Using the API](https://support.panopto.com/s/article/Upload-API)
- Panopto support document: [Create OAuth2 Clients](https://support.panopto.com/s/article/oauth2-client-setup)
- [Universal Content Library specification](https://github.com/Panopto/universal-content-library-specification): UCS XML definition and samples.
- [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/): Python module to handle OAuth2 workflow on top of [OAuthlib library](https://github.com/oauthlib/oauthlib)
- [Requests](https://2.python-requests.org/): HTTP library for Python
