from tutorial.application_context import AppContext

import sys

if __name__ == '__main__':
	appctxt = AppContext()
	exit_code = appctxt.run()
	sys.exit(exit_code)