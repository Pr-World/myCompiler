import pygame as pyg
import sys


class pygimg:

	@staticmethod
	def crop(self, image, tocrop, colorkey='black'):
		pys = pyg.Surface((tocrop[2], tocrop[3]))
		pys.blit(image, (0,0), (tocrop[0], tocrop[1], tocrop[2], tocrop[3]))
		pys.set_colorkey(colorkey)
		return pys

	@staticmethod
	def merge(self, image1, image2, tomerge, colorkey='black'):
		pys = pyg.Surface(image1.get_size())
		s = image1.get_size()
		pys.blit(image1, (0,0), (0, 0, s[0], s[1]))
		pys.blit(image2, (tomerge[0], tomerge[1]), (0, 0, tomerge[2], tomerge[3]))
		pys.set_colorkey(colorkey)
		return pys

	@staticmethod
	def resize(self, *args, **kwargs):
		return pyg.transform.scale(*args, **kwargs)

	@staticmethod
	def scale(self, img, scaleFactor):
		x, y = img.get_size()
		return pyg.transform.scale(img, (x * scaleFactor, y * scaleFactor))

	@staticmethod
	def load(self, *args, **kwargs):
		return pyg.image.load(*args, **kwargs)

	@staticmethod
	def rotate(self, *args, **kwargs):
		return pyg.transform.rotate(*args, **kwargs)


class pygwin:
	
	def __init__(self, title="Hello World!", size=(600, 600), fps=60, log=True):
		self.title = title
		self.size = size
		if log:
			print("\nPygwin: Initialized with title='{}', size={}, fps={}".format(title, size, fps))
		self.fps = fps
		self.clock = pyg.time.Clock()
		if log: print("Pygwin: Initializing pygame")
		pyg.init()
		while True:
			try:
				pyg.mixer.init()
				break
			except Exception as e:
				pass
		if log: print("Pygwin: Pygame initialized, applying size and title")
		self.screen = pyg.display.set_mode(self.size)
		pyg.display.set_caption(self.title)
		if log: print("Pygwin: applied size and tite, window initialized\n")

	def blit(self, *args, **kwargs):
		self.screen.blit(*args, **kwargs)

	def handle_event(self, event):
		pass

	def update(self):
		pass


	def run(self):

		while True:
			for event in pyg.event.get():
				self.handle_event(event)
				if event.type == pyg.QUIT:
					pyg.quit()
					sys.exit(1)

			self.update()
			pyg.display.update()
			self.clock.tick(self.fps)

def __loadsound__(*args, **kwargs):
	return pyg.mixer.Sound(*args, **kwargs)

def __loadmusic__(*args, **kwargs):
	return pyg.mixer.music.load(*args, **kwargs)

pyg.loadsound = __loadsound__
pyg.loadmusic = __loadmusic__

class pygsprite:

	def __init__(self):
		self.to_update = True
		self.to_draw = True

	def draw_sprite(self, screen):
		pass

	def update(self):
		pass

	def draw(self, screen):
		if self.to_draw: self.draw_sprite(screen)
		if self.to_update: self.update()

	@staticmethod
	def get_sprite(sheet, col, row, size):
		return pygimg.crop(sheet, (col*size[0], row*size[1], size[0], size[1]), 'black')
