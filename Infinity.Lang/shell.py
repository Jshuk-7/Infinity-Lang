import os
import infinity

class Shell(object):
	def __init__(self) -> None:
		self.using_platform_windows = True
		self.using_git_bash = True
		self.print_info()
		self.execute_program()

	def print_info(self):
		os.system("cls" if os.name == 'nt' else 'clear')

		if os.name == 'nt':
			print(f"Infinity Lang {infinity.version()}, running G++ 64 bit (INTEL64) on platform win32")
		else:
			print(f"Infinity Lang {infinity.version()}, running Clang 64 bit (INTEL64) on platform darwin")
		print("Type 'help', 'credits' or 'license' for more information")

	def execute_program(self):
		while 1:
			text = input('>>> ')

			if text == '': continue
			elif text == 'exit()': quit()

			result, error = infinity.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result:
				print(result)