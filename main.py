import perfume

default_perfume = perfume.Perfume()
man_perfume = perfume.Perfume(volume=145,
                              price=199,
                              brand='Dior',
                              type='Floral',
                              collection='Dior Addict collection',
                              fragranceConcentration=30)
woman_perfume = perfume.Perfume(volume=100,
                                price=250,
                                collection='Miss Dior', )
print(default_perfume)
print(man_perfume)
print(woman_perfume)
