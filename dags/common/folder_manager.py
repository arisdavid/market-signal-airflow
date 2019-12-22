import os


def create_folder(data_store, sub_folders):

    if not os.path.exists(data_store):
        for sub_folder in sub_folders:
            os.makedirs(f"{data_store}/{sub_folder}")

