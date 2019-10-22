
import configparser
import os

def create_config(path='config.ini'):
	parser = configparser.ConfigParser()
	parser['DEFAULT'] = {
		'root': './',
		'host': 'locahost',
		'port': 8080
	}
	parser['CONFIG'] = {}
	with open(path, 'w') as file:
		parser.write(file)

def get_parser(config='config.ini'):
	if not os.path.isfile(config):
		create_config(config)
	parser = configparser.ConfigParser()
	parser.read(config)
	return parser

def get_value(value):
	parser = get_parser()
	try:
		return parser['CONFIG'][value]
	except:
		return parser['DEFAULT'][value]