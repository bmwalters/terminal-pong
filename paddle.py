import curses

from movable import Movable

class Paddle(Movable):
	def __init__(self, x, y, w):
		super(Paddle, self).__init__(x, y)
		self.w = w

	def update(self, window):
		super(Paddle, self).update()

		scrh, scrw = window.getmaxyx()

		key = window.getch()

		if key == curses.KEY_LEFT:
			self.x = max(self.x - 1, 0)
		elif key == curses.KEY_RIGHT:
			self.x = min(self.x + 1, scrw - self.w)

	def draw(self, window):
		window.insstr(self.y, self.x, "[" + ("=" * (self.w - 2)) + "]")
