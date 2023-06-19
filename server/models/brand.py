class Brand:
    
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def serialise(self):
        return {
            "id": self.id,
            "name": self.name
        }