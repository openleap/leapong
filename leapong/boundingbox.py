
class BoundingBox(object):

    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.width = width
        self.height = height

    def collide(self, bounding_box):
        return not (
            self.x2 < bounding_box.x1 or
            bounding_box.x2 < self.x1 or
            self.y2 < bounding_box.y1 or
            bounding_box.y2 < self.y1
        )

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        self._width = width
        self.x2 = self.x1 + width

    @height.setter
    def height(self, height):
        self._height = height
        self.y2 = self.y1 + height

    def set_position(self, x, y):
        self.x1, self.y1 = x, y
        self.x2, self.y2 = (self.x1 + self._width), (self.y1 + self._height)

    def resize(self, width, height):
        self.width = width
        self.height = height
