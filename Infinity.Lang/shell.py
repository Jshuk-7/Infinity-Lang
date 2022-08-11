import os
import infinity

class Shell(object):
	def __init__(self) -> None:
		self.using_git_bash = True
		self.using_platform_windows = False
		self.print_info()
		self.execute_code()

	def print_info(self):
		if self.using_git_bash:
			os.system("clear")
		else:
			os.system("cls")

		if self.using_platform_windows:
			print(f"Infinity Lang {infinity.version()}, running MSVC 64 bit (INTEL64) on platform Win32")
		else:
			print(f"Infinity Lang {infinity.version()}, running Clang 64 bit (INTEL64) on platform Darwin")
		print("Type 'help', 'credits' or 'license' for more information")

	def execute_code(self):
		while 1:
			text = input('>>> ')

			if text == '':
				continue
			elif text == 'clear()':
				os.system("clear")
				continue
			elif text == "std::version()":
				print(f'Infinity Lang: {infinity.version()}')
				continue
			elif text == 'exit()':
				quit()

			result, error = infinity.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result:
				print(result)