import os

class Config(object):
    FREEZER_DESTINATION = os.environ.get('FREEZER_DESTINATION') or '../../' # Puts the build files in the project directory
    FREEZER_REMOVE_EXTRA_FILES = os.environ.get('FREEZER_REMOVE_EXTRA_FILES') or False # Needed so that Flask_Frozen does not self-descruct the source code
    FREEZER_DEFAULT_MIMETYPE = os.environ.get('FREEZER_DEFAULT_MIMETYPE') or 'text/html' # Not reaally sure if needed, but removes some errors when building
