from currency import Currency
from LightSourceType import LightSourceType
from Rating import Rating
from LustersType import LustersType
from Lamps import Lamps
from TableLampsType import TableLampsType

class TableLamps(Lamps):

    def __init__(self,
                 price=0,
                 height=0,
                 currency=Currency.UAH,
                 lightSourceType=LightSourceType.LED,
                 rating=Rating.EXCELLENT,
                 tableLampsType=TableLampsType.OFFICE,
                 ):
        Lamps.__init__(self, price, height, currency,
                         lightSourceType, rating)
        self.tableLampsType = tableLampsType