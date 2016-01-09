import random, curses, time

TICKRATE = 20

stdscr = curses.initscr()
stdscr.nodelay(True)
stdscr.keypad(True)
curses.cbreak()

SCRH, SCRW = stdscr.getmaxyx()

ball = {"x": 0, "y": 0, "velx": 1, "vely": 1}
paddle = {"x": 0, "y": SCRH - 1, "w": 5}

lasttick = time.time()

while True:
	if time.time() > (lasttick + 1.0/TICKRATE):
		key = stdscr.getch()

		ball["x"] += ball["velx"]
		ball["y"] += ball["vely"]

		if ball["x"] >= (SCRW - 1) or ball["x"] <= 0:
			ball["velx"] *= -1
		if ball["y"] >= (SCRH - 1) or ball["y"] <= 0:
			ball["vely"] *= -1

		if (ball["x"] >= paddle["x"] and ball["x"] <= (paddle["x"] + paddle["w"])) and ball["y"] == paddle["y"]:
			ball["vely"] *= -1

		if key == curses.KEY_LEFT:
			paddle["x"] = max(paddle["x"] - 1, 0)
		elif key == curses.KEY_RIGHT:
			paddle["x"] = min(paddle["x"] + 1, SCRW - paddle["w"])

		stdscr.clear()
		if paddle["x"] < ball["x"]:
			stdscr.insstr(paddle["y"], paddle["x"], "[" + ("=" * (paddle["w"] - 2)) + "]")
			stdscr.insch(ball["y"], ball["x"], "o")
		else:
			stdscr.insch(ball["y"], ball["x"], "o")
			stdscr.insstr(paddle["y"], paddle["x"], "[" + ("=" * (paddle["w"] - 2)) + "]")
		stdscr.refresh()

		curses.flushinp()

		lasttick = time.time()
