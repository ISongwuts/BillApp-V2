import subprocess
from PyQt6.QtCore import QTimer, QThread, pyqtSignal

class PingThread(QThread):
    connection_status = pyqtSignal(bool)
    def run(self):
        while True:
            try:
                subprocess.check_output("ping -c 1 google.com", shell=True, stderr=subprocess.STDOUT)
                self.connection_status.emit(True)
            except subprocess.CalledProcessError:
                self.connection_status.emit(False)
            self.sleep(5)