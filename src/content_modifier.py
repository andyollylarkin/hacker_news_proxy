from cgitb import text
from bs4 import BeautifulSoup
from bs4.element import PageElement, Tag
import re

class ContentModifier():
	def __init__(self, content: BeautifulSoup) -> None:
		self.content = content
	def modify(self) -> None:
		# parse body
		content = self.content.contents
		for i in content:
			tds = i.find_all_next('td')
			for el in tds:
				a = el.find_next('a')
				if a is not None:
					txt = a.get_text().split(' ')
					for word in range(0, len(txt)):
						if len(txt[word]) >= 6:
							txt[word] = txt[word] + '™'
							a.string = ' '.join(txt)
	def render_content(self):
		return self.content.prettify()