from datetime import datetime
import os

now = datetime.now()
with open("README.md", 'w+') as f:
    f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
    f.write(os.environ["TEST_ENV"])
