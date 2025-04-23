import os
from os.path import exists, join
from global_variables.global_sign_table import GlobalServiceSigns

def handle_token_dir_path(entry_working_dir_path: str, service_type: GlobalServiceSigns):
    built_path: str = join(entry_working_dir_path,'tokenized_keys','google_api',f"{service_type.lower()}_token")
    if not exists(built_path):
        os.mkdir(built_path)

    return built_path