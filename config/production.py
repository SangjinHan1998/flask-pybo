from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xde\xae\x04\xc7\xcc\xa5#U\xad3L\xb1\xd3U\xf6Q'


