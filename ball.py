import wave, threading

useaudio = True
try:
	import pyaudio
except ImportError:
	useaudio = False

from movable import Movable

def play_blip():
	chunk = 1024
	wf = wave.open("blip.wav", "rb")
	p = pyaudio.PyAudio()

	stream = p.open(
		format = p.get_format_from_width(wf.getsampwidth()),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output = True
	)

	data = wf.readframes(chunk)

	while data != "":
		stream.write(data)
		data = wf.readframes(chunk)

	stream.stop_stream()
	stream.close()
	p.terminate()

def blip():
	if useaudio:
		t = threading.Thread(target=play_blip)
		t.start()

class Ball(Movable):
	def __init__(self, x, y, velx=1, vely=1):
		super(Ball, self).__init__(x, y, velx, vely)

	def update(self, window, obstacles):
		super(Ball, self).update()

		scrh, scrw = window.getmaxyx()

		if self.x == (scrw - 1) or self.x == 0:
			self.velx *= -1
			blip()
		if self.y == (scrh - 1) or self.y == 0:
			self.vely *= -1
			blip()

		for obstacle in obstacles:
			if (self.x >= obstacle.x and self.x <= (obstacle.x + obstacle.w + 1)) and ((self.vely == 1 and self.y == (obstacle.y - 1)) or (self.vely == -1 and self.y == (obstacle.y + 1))):
				self.vely *= -1
				blip()

	def draw(self, window):
		window.insch(self.y, self.x, "o")
