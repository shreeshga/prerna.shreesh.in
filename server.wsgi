import os
import sys
path = '/home/ubuntu/shreesh.in/prerna'
if path not in sys.path:
    sys.path.append(path)
path = '/home/ubuntu/shreesh.in/prerna'
if path not in sys.path:
    sys.path.append(path)

activate_this = '/home/ubuntu/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from wedding import app as application

