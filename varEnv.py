# ajout avec le shell :

export TEST_KEY = "TESTKEY"

# Accès avec le module os

import os
test = os.environ.get('TEST_KEY')
print(test)
