# servedoc
A python webserver to serve markdown documentation as simple html pages. You can traverse the website
like you would a (unix) filesystem.

This is mostly for personal use, but if you were to want to use it, feel free.

## Dependencies

* `bottle`
* `markdown2`

Install them through pip either manually or using `pip install -r requirements.txt` it doesn't really matter.

## How to run

It might be useful to first create the config file by running `python config.py`. You can then edit the config file as needed.
You can start the server by running `python server.py` which will also create the config file if non exists.

## Explanation of config

The config file has the following sections:

* root - The root directory for all your documentation files (default /doc/).
* port - The port the webserver should run on (default 8080)
* title - The html title tag (default Documentation)
* css - A link to a css file (default None)

### Possible future features

* Optional authentication
* Support for multiple root folders/more modular creation of dirtrees
* Optional RSS Feed support
