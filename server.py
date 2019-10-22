from bottle import route, run, template
import config
import os
import markdown2
import crawler

@route('/')
def root():
	dirmap = crawler.get_directory_map()
	html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<title> Documentation </title>
			</head>
			<body>
				<ul>
					%for key, value in dirmap.iteritems():
						<li><a href='{{key + "/" + value}}'>{{value}}</a></li>
					%end
				</ul>
			</body>
		</html>
	'''
	return template(html, dirmap=dirmap)

@route('/<file:path>')
def find_file(file):
	root = config.get_value('root')
	path = os.path.join(root, file)
	with open(path, 'r') as f:
		data = f.read()
	md = markdown2.markdown(data)
	return md

if __name__ == '__main__':
	host = config.get_value('host')
	port = config.get_value('port')
	run(host=host, port=port)