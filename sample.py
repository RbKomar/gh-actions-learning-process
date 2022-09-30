from datetime import datetime

now = datetime.now()
with open("README.md") as f:
    f.write(now.strftime("%Y-%m-%d"))
