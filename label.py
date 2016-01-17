class Label(object):
	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw(self, window):
		window.insstr(self.y, self.x, self.text)
