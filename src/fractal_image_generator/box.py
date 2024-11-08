class Box:
    def __init__(self, coords, is_alive=False, create_children=False):
        self.coords = coords
        self.children = []
        self.is_alive = is_alive
        if create_children:
            self.make_children()
    
    # create dim^2 children for the node
    def make_children(self):
        if self.children:
            return
        x, y, size = self.coords
        shift = int(size / 2)
        if size <= 1 or shift < 1:
            return []
        self.children = [Box((x + i * shift, y + j * shift, shift)) for i in range(2) for j in range(2)]