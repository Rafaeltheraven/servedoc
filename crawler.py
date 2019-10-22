
import os
import config

def get_directory_map():
	start = config.get_root()
	result = {}
	for root, dirs, files in os.walk(start):
		for subdir in dirs:
			result[os.path.join(root, subdir)] = []
		result[root] = files
	return result

if __name__ == '__main__':
	print(get_directory_map())