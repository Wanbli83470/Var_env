# ajout avec le shell :
export TEST_KEY = "TESTKEY"

import os
test = os.environ.get('TEST_KEY')
print(test)