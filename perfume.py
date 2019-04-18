class Perfume:
    number_of_perfumes = 0

    def __init__(self,
                 volume=0,
                 price=0,
                 brand=None,
                 type=None,
                 collection=None,
                 fragranceConcentration=0):
        self.volume = volume
        self.price = price
        self.brand = brand
        self.type = type
        self.collection = collection
        self.fragranceConcentration = fragranceConcentration

    def __del__(self):
        print('Perfume {} was deleted'.format(self.volume))

    def __str__(self):
        return ('volume = {} ml, price = {} €, brand = {}, type = {},collection = {}, ' +
                'fragranceConcentration = {} % ').format(self.volume, self.price, self.brand,
                                                         self.type, self.collection, self.fragranceConcentration)

    @staticmethod
    def get_number_of_perfumes():
        return Perfume.number_of_perfumes
