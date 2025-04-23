
import os.path
import imapclient
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from data_sources_handlers.remote_data.google_api.google_service_api import GoogleServiceDataHandling

from global_variables.global_sign_table import GlobalServiceSigns
from global_variables.gmail_api_variables import Scopes
from os.path import join
class GmailDataHandler(GoogleServiceDataHandling):

    def __init__(self):
        super().__init__()
        self.SCOPES = [Scopes.READONLY.value]
        self.client_secret_path: str = join(self.current_working_dir, "data", "client_secret.json")
        # check if token dir exists
        self.creds = self.create_credentials(self.client_secret_path, self.SCOPES, GlobalServiceSigns.GOOGLE_GMAIL)
        self.api_version: str = "v1"
        try:
            # Call the Gmail API
            service = build(GlobalServiceSigns.GOOGLE_GMAIL.value.lower(),
                            self.api_version,
                            credentials=self.creds,
                            static_discovery=False)

            results = service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])

            if not labels:
                print("No labels found.")
                return
            print("Labels:")
            for label in labels:
                print(label["name"])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")






g = GmailDataHandler()
