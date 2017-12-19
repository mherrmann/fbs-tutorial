from fbs_runtime.application_context import ApplicationContext, \
	cached_property
from PyQt5.QtWidgets import QApplication, QWidget

import sys

class AppContext(ApplicationContext):
	def run(self):
		self.main_window.show()
		return self.app.exec_()
	@cached_property
	def main_window(self):
		result = QWidget()
		result.setWindowTitle('Hello World!')
		result.resize(250, 150)
		result.move(300, 300)
		return result

if __name__ == '__main__':
	appctxt = AppContext()
	exit_code = appctxt.run()
	sys.exit(exit_code)