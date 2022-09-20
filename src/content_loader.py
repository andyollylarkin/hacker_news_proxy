import base64
from importlib.resources import contents
import urllib.request
import bs4


class ContentLoader:
	def __init__(self, base_url: str, path: str) -> None:
		self.__url = base_url
		self.__path = path
		self.__raw_content = self.__load_content()

	def __load_content(self):
		""" Load content from given url """
		opener = urllib.request.FancyURLopener({})
		opener.addheader = [(
			 "User-Agent",
        	 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
		)]
		with opener.open(self.__url + self.__path) as f:
			content = f.read()
		return content

	def get_raw_data(self) -> str:
		return self.__raw_content

	def get_parsed_data(self):
		soup = bs4.BeautifulSoup(self.__raw_content, 'html.parser', from_encoding='ascii')
		return soup
