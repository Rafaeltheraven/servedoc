from bottle import route, run, template, HTTPResponse
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
				<title>Documentation</title>
			</head>
			<body>
				<ul>
					%for key, values in dirmap.items():
						<li>{{key}}</li>
						<ul>
						%for value in values:
							<li><a href='{{key + "/" + value}}'>{{value}}</a></li>
						%end
						</ul>
					%end
				</ul>
			</body>
		</html>
	'''
	return template(html, dirmap=dirmap)

def show_dir(path):
	dirmap = crawler.get_directory_map()
	subdir = dirmap[path.rstrip('/')]
	html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<title>Documentation</title>
			</head>
			<body>
				<h3>{{path}}</h3>
				<ul>
					%for value in subdir:
						<li><a href={{path + "/" + value}}>{{value}}</a></li>
					%end
				</ul>
			</body>
		</html>
	'''
	return template(html, path=path, subdir=subdir)

@route('/<file:path>')
def find_file(file):
	path = os.path.join('/', file)
	if os.path.isfile(path):
		with open(path, 'r') as f:
			data = f.read()
		md = markdown2.markdown(data)
		return md
	elif os.path.isdir(path):
		return show_dir(path)
	else:
		return HTTPResponse(status=404)

if __name__ == '__main__':
	host = config.get_value('host')
	port = config.get_value('port')
	run(host='localhost', port=port)