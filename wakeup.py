import subprocess

# 以下にファイル名を記述する
wakeup_applications = [
    r"",
    r"",
    r"",
    r"",
]

[ subprocess.Popen(application) for application in wakeup_applications ]
