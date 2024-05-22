import inquirer

from utils.text import cstring


def should_delete(output_name) -> bool:
	"""
		Asks the user if they want to delete the file if it already exists
	"""
	return inquirer.prompt([
		inquirer.Confirm('delete', message = cstring(
			f'&cThe file &d{output_name}&c already exists. Do you want to replace it?'
		), default=True) # type: ignore
	])['delete']

def should_continue(input_name, output_name) -> bool:
	"""
		Asks the user if they want to continue with the conversion
	"""
	return inquirer.prompt([
		inquirer.Confirm('confirm', message = cstring(
			f'&eAre you sure you want to convert &d{input_name}&e to &d{output_name}&e?'
		), default=True) # type: ignore
	])['confirm']