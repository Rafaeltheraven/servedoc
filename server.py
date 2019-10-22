from bottle import route, run, template
import config
import os
import markdown2
import crawler

@route('/')
def root():
	dirmap = crawler.get_directory_map()
	url = config.get_url()
	html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<title> Documentation </title>
			</head>
			<body>
				<ul>
					%for file in dirmap:
						<li>{{file}}</li>
					%end
				</ul>
			</body>
		</html>
	'''
	return template(html, dirmap)

@route('/<file:path>')
def find_file(file):
	root = config.get_root()
	path = os.path.join(root, file)
	with open(path, 'r') as f:
		data = f.read()
	md = markdown2.markdown(data)
	return md

if __name__ == '__main__':
	run(host='localhost', port=8080)