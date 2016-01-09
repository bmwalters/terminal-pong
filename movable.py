class Movable(object):
	def __init__(self, x, y, velx=0, vely=0):
		self.x = x
		self.y = y
		self.velx = velx
		self.vely = vely

	def update(self):
		self.x += self.velx
		self.y += self.vely

	def draw(self, window):
		window.insch(self.y, self.x, "@")
