import os

class Config(object):
    FREEZER_DESTINATION = os.environ.get('FREEZER_DESTINATION') or 'build' # Puts the build files in the project directory
    FREEZER_DEFAULT_MIMETYPE = os.environ.get('FREEZER_DEFAULT_MIMETYPE') or 'text/html' # Not reaally sure if needed, but removes some errors when building
