import platform
import os
import getpass

class Info:
    def __init__(self):
        self.platform = platform.system()
        self.processList = {}
        if self.platform == "Linux" or self.platform == "Darwin":
            self.posixSystem()
        if self.platform == "Linux":
            self.linux()
    def getProcess(self):
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        processList = []
        for pid in pids:
            _proInfo = {}
            pro = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            pro = pro.decode("utf-8").split("\x00")[0]
            _proInfo["pid"] = pid
            _proInfo["process"] = pro
            processList.append(_proInfo)
        return processList
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
    def linux(self):
        self.processList = self.getProcess()
        # linux specific stuff
        return True
