from shutil import copyfile

class Image:
	def __init__(self):
		pass

	def copy(self, src, dst):
		copyfile(src, dst)

_Image = Image()