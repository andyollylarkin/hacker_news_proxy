from flask import Flask
from dotenv import dotenv_values
from content_loader import ContentLoader
from content_modifier import ContentModifier
from urllib.parse import urlparse


config = dotenv_values('../.env')
app = Flask(__name__)


@app.route('/<path:path>')
@app.route('/', defaults={'path': ''})
def home(path):
	url_parts = urlparse(path)
	content_loader = ContentLoader(config['HN_BASEURL'], url_parts.path)
	content_modifier = ContentModifier(content_loader.get_parsed_data())
	content_modifier.modify()
	return content_modifier.render_content()