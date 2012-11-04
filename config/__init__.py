import os

DB_CONFIG = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'matresponsible',
  'charset': 'utf8',
  'collation': 'utf8_general_ci'
}

if os.environ.has_key("DOCUMENT_ROOT"):
    DOCUMENT_ROOT = os.environ["DOCUMENT_ROOT"]+"/"
else:
    DOCUMENT_ROOT = ""
    os.chdir(__path__[0])
    os.chdir("..")