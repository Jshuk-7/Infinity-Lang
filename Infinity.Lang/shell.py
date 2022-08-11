import os
import infinity

class Shell(object):
	def __init__(self) -> None:
		self.print_info(git_bash = False)
		self.execute_code()

	def print_info(self, git_bash):
		if git_bash:
			os.system("clear")
		else:
			os.system("cls")

		print("Infinity Lang 0.1.0, running 64 bit (INTEL64) on platform Win32")
		print("Type 'help', 'credits' or 'license' for more information")

	def execute_code(self):
		while 1:
			text = input('>>> ')

			if text == '':
				continue
			elif text == 'exit':
				quit()

			result, error = infinity.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result:
				print(result)