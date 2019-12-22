import os


def create_folder(data_store):

    if not os.path.exists(data_store):
        os.mkdir(data_store)


