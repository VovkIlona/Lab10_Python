from currency import Currency
from LightSourceType import LightSourceType
from Rating import Rating


class Lamps:

        def __init__(self,
                     price=0,
                     height=0,
                     currency=Currency.USD,
                     lightSourceType=LightSourceType.ENERGYSAVING,
                     rating=Rating.AVERAGE
                     ):
            self.price = price
            self.height = height
            self.currency = currency
            self.lightSourceType = lightSourceType
            self.rating = rating


        def __str__(self):
            return " price= {}, height={}, currency={}, lightSourceType={}, rating={}" .format(
            self.price,self.height,
            self.currency,self.lightSourceType,self.rating)
