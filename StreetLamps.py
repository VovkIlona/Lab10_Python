from currency import Currency
from LightSourceType import LightSourceType
from Rating import Rating
from LustersType import LustersType
from Lamps import Lamps
from StreetLampsType import StreetLampsType



class StreetLamps(Lamps):

    def __init__(self,
                 price=0,
                 height=0,
                 currency=Currency.UAH,
                 light_source_type=LightSourceType.LED,
                 rating=Rating.EXCELLENT,
                 streetLampsType=StreetLampsType.EMBEDDED,
                 solarBattery=True

                 ):
        Lamps.__init__(self, price, height, currency,
                         light_source_type, rating)
        self.streetLampsType = streetLampsType
        self.solarBattery = solarBattery