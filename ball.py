from movable import Movable

class Ball(Movable):
	def __init__(self, x, y, velx=1, vely=1):
		super(Ball, self).__init__(x, y, velx, vely)

	def update(self, window, paddle):
		super(Ball, self).update()

		scrh, scrw = window.getmaxyx()

		if self.x >= (scrw - 1) or self.x <= 0:
			self.velx *= -1
		if self.y >= (scrh - 1) or self.y <= 0:
			self.vely *= -1

		if (self.x >= paddle.x and self.x <= (paddle.x + paddle.w)) and self.y == (paddle.y + 1):
			self.vely *= -1

	def draw(self, window):
		window.insch(self.y, self.x, "o")
