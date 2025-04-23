from typing import List

from global_variables.global_sign_table import GlobalServiceSigns
from os.path import exists, join, dirname
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from utilities.directories_location_utility import handle_token_dir_path
from os import getcwd

class GoogleServiceDataHandling:

    def __init__(self):
        self.current_working_dir: str = dirname(dirname(dirname(getcwd())))


    def create_credentials(self, client_secret_path, scopes: List, service_type: GlobalServiceSigns ):
        creds = None
        token_directory_path: str = handle_token_dir_path(self.current_working_dir, service_type.value)
        if exists(join(token_directory_path, "token.json")):
            creds = Credentials.from_authorized_user_file(join(token_directory_path, "token.json"), scopes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, scopes)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(join(token_directory_path, "token.json"), "w") as token:
                token.write(creds.to_json())

        return creds