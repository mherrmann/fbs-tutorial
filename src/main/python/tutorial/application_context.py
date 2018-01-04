from fbs_runtime.application_context import ApplicationContext, \
    cached_property
from PyQt5.QtWidgets import QApplication, QMainWindow

class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()
    @cached_property
    def main_window(self):
        result = QMainWindow()
        result.setWindowTitle('Hello World!')
        result.resize(250, 150)
        return result