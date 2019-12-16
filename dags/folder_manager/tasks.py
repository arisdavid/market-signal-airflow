import os
from pathlib import Path


def create_folder(data_store):

    if not os.path.exists(os.path.join(Path(__file__).parent.parent, data_store)):
        os.mkdir(os.path.join(Path(__file__).parent.parent, data_store))


