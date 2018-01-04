from fbs_runtime.application_context import ApplicationContext, \
    cached_property
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()
    @cached_property
    def main_window(self):
        result = QMainWindow()
        image_container = QLabel()
        image_container.setPixmap(self.image)
        result.setCentralWidget(image_container)
        return result
    @cached_property
    def image(self):
        return QPixmap(self.get_resource('success.jpg'))