import sys
sys.path.insert(0, '../models')
from currency import Currency
from LightSourceType import LightSourceType
from Rating import Rating
from LustersType import LustersType
from Lamps import Lamps
from Lusters import Lusters
from TableLamps import TableLamps
from TableLampsType import TableLampsType
from StreetLamps import StreetLamps
from StreetLampsType import StreetLampsType

class LampsManager:
        def __init__(self, lamps):
            self.lamps = lamps

        @staticmethod
        def sortByPrice(lamps, descending=False):
            return sorted(lamps, key=lambda lamp: lamp.price, reverse=descending)

        @staticmethod
        def sortByHeight(lamps, descending=False):
            return sorted(lamps, key=lambda lamp: lamp.height, reverse=descending)

        @staticmethod
        def filterByType(lightSourceType):
            return list(filter(lambda lamp: lamp.lightSourceType == lightSourceType, self.lamps))

        @staticmethod
        def filterByRating(rating):
            return list(filter(lambda lamp: lamp.rating == rating, self.lamps))

     







def main():
    
    lamps = []
    lamps.append(Lamps(250, 20, Currency.UAH, LightSourceType.ENERGYSAVING, Rating.AVERAGE))
    lamps.append(Lamps(250, 30, Currency.UAH, LightSourceType.ENERGYSAVING, Rating.AVERAGE))
    lamps.append(Lamps(400, 100, Currency.UAH, LightSourceType.LED, Rating.AVERAGE))
    lamps.append(Lamps(440, 10, Currency.UAH, LightSourceType.ENERGYSAVING, Rating.GOOD))
    lamps.append(Lamps(190, 50, Currency.USD, LightSourceType.ENERGYSAVING, Rating.GOOD))

    manager = LampsManager(lamps)

    for i in LampsManager.sortByPrice(lamps):
        print(i)
    print()

    for i in LampsManager.sortByHeight(lamps):
        print(i)
    print()
    

main()