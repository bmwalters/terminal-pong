import random, curses, time

from ball import Ball
from paddle import Paddle

TICKRATE = 20

class Game():
	def __init__(self):
		self.window = curses.initscr()
		self.window.nodelay(True)
		self.window.keypad(True)
		curses.cbreak()

		SCRH, SCRW = self.window.getmaxyx()

		self.ball = Ball(0, 0)
		self.paddle = Paddle(0, SCRH - 1, 5)

		self.lasttick = time.time()

	def loop(self):
		while True:
			if time.time() > (self.lasttick + 1.0/TICKRATE):
				self.ball.update(self.window, self.paddle)
				self.paddle.update(self.window)

				self.window.clear()
				if self.paddle.x < self.ball.x:
					self.paddle.draw(self.window)
					self.ball.draw(self.window)
				else:
					self.ball.draw(self.window)
					self.paddle.draw(self.window)
				self.window.refresh()

				curses.flushinp()

				self.lasttick = time.time()

g = Game()
g.loop()
