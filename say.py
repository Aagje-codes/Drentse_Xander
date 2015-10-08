""" can I use a bash command in Python?"""

import os

sent = "Hello World"
bash_command = "say -v Karen {0}".format(sent)

os.system(bash_command)


# It works!! How cool is that?! 