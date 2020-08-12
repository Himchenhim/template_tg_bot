class Item:
    def __init__(self, item_id=0, item_name="none", rating=0):
        self.item_id = item_id
        self.item = item_name
        self.rating = rating

    def plus_rating(self):
        self.rating += 1

    def minus_rating(self):
        self.rating -= 1

    def get_item_id(self):
        return self.item_id


mandarin = Item(item_id=100, item_name="mandarin", rating=0)
