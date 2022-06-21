import platform
import os
import getpass

class Info:
    def __init__(self):
        self.platform = platform.system()
        if self.platform == "Linux" or self.platform == "Darwin":
            self.posixSystem()
    def posixSystem(self):
        self.home = os.environ['HOME']
        self.user = getpass.getuser()
        self.release = platform.release()
        self.processor = platform.processor()
    def windows(self):
        return True
    def osx(self):
        # osx specic stuff
        return True
    def linux(_self):
        # linux specific stuff
        return True
