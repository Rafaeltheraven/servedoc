from bottle import route, run, template, HTTPResponse, default_app
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
					%for key, values in sorted(dirmap.items()):
						<li>{{key}}</li>
						<ul>
						%for value in sorted(values):
							<li><a href='{{key + "/" + value}}'>{{value}}</a></li>
						%end
						</ul>
					%end
				</ul>
			</body>
		</html>
	'''
	return template(html, dirmap=dirmap)

def create_html(body):
	title = config.get_value('title')
	css = config.get_value('css')
	html = '''
		<!DOCTYPE html>
		<html>
			<head>
				<title>''' + title + '''</title>
	'''
	if css:
		html += '''
			<link rel='stylesheet' type='text/css' href="''' + css + '''"
		'''
	html ++ '''
			</head>
			<body>
	'''
	html += body
	html += '''
			</body>
		</html>
	'''
	return html

def show_dir(path):
	dirmap = crawler.get_directory_map()
	try:
		subdir = dirmap[path.rstrip('/')]
	except:
		subdir = dirmap[path] # Why is this not consitent
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
	root = config.get_value('root')
	path = os.path.join(root, file)
	if os.path.isfile(path):
		with open(path, 'r') as f:
			data = f.read()
		md = markdown2.markdown(data)
		return md
	elif os.path.isdir(path):
		return show_dir(file)
	else:
		return HTTPResponse(status=404)

if __name__ == '__main__':
	port = config.get_value('port')
	run(host='localhost', port=port)
else:
	app = application = default_app()