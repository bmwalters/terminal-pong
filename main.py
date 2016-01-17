import random, curses, time

from ball import Ball
from paddle import Paddle
from label import Label

TICKRATE = 20

class Game():
	def __init__(self):
		self.window = curses.initscr()
		self.window.nodelay(True)
		self.window.keypad(True)
		curses.cbreak()

		SCRH, SCRW = self.window.getmaxyx()

		self.ball = Ball(2, 2)
		self.paddle1 = Paddle(0, 0, 5, [curses.KEY_LEFT, curses.KEY_RIGHT])
		self.paddle2 = Paddle(0, SCRH - 1, 5, [97, 100])

		self.scorex = 0
		self.scorey = 0
		self.score = Label(1, 1, "Score: 0:0")

	def loop(self):
		while True:
			key = self.window.getch()

			self.ball.update(self.window, [self.paddle1, self.paddle2])
			self.paddle1.update(self.window, key)
			self.paddle2.update(self.window, key)

			self.window.clear()
			draworder = sorted([self.ball, self.paddle1, self.paddle2, self.score], key=lambda o: o.x)
			for o in draworder:
				o.draw(self.window)
			self.window.refresh()

			curses.flushinp()

			curses.napms(1000 / TICKRATE)

g = Game()
g.loop()
