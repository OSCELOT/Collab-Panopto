# Copy to Config.py. Modify values with what you got from 
# your REST App registration on developer.blackboard.com
# Use:
# import Config
# KEY = Config.adict['learn_rest_key']
# SECRET = Config.adict['learn_rest_key']
# etc...
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