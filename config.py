
import configparser


def get_parser(config='config.ini'):
	parser = configparser.ConfigParser()
	parser.read(config)
	return parser

def get_root():
	parser = get_parser()
	return parser['CONFIG']['root']

def get_url():
	parser = get_parser()
	return parser['CONFIG']['url']