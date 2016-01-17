import curses

from movable import Movable

class Paddle(Movable):
	def __init__(self, x, y, w, keys):
		super(Paddle, self).__init__(x, y)
		self.w = w
		self.k_l = keys[0]
		self.k_r = keys[1]

	def update(self, window):
		super(Paddle, self).update()

		scrh, scrw = window.getmaxyx()

		key = window.getch()

		if key == self.k_l:
			self.x = max(self.x - 1, 0)
		elif key == self.k_r:
			self.x = min(self.x + 1, scrw - self.w)

	def draw(self, window):
		window.insstr(self.y, self.x, "[" + ("=" * (self.w - 2)) + "]")
