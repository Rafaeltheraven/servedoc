
import configparser
import os

def create_config(path='config.ini'):
	parser = get_parser()
	parser['DEFAULT'] = {
		'root': './',
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

def get_root():
	parser = get_parser()
	return parser['CONFIG']['root']

def get_url():
	parser = get_parser()
	return parser['CONFIG']['url']