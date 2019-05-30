from currency import Currency
from LightSourceType import LightSourceType
from Rating import Rating
from LustersType import LustersType
from Lamps import Lamps


class Lusters(Lamps):

    def __init__(self,
                 price=0,
                 height=0,
                 currency=Currency.UAH,
                 lightSourceType=LightSourceType.LED,
                 rating=Rating.GOOD,
                 lustersType=LustersType.CRYSTAL,
                 abatjour=True
                 ):
        Lamps.__init__(self, price, height, currency,
                         lightSourceType, rating)
        self.lustersType = lustersType
        self.abatjour = abatjour