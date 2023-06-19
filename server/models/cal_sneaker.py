class CalSneaker:

    def __init__(self, brand, model, date, image_url, id = None):
        self.brand = brand
        self.model = model
        self.date = date
        self.image_url = image_url
        self.id = id

    def serialise(self):
        return {
            "id": self.id,
            "brand": self.brand.serialise(),
            "model": self.model,
            "date": self.date,
            "image_url": self.image_url
        }