#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass
class CreateDataClass:
  name: str
  country:str
  area: float
  description:str
  aka:str
  def __post_init__(self):
    self.name = self.name.upper()
    self.country = self.country.upper()
    self.area = self.area * 2
    self.description = self.description.upper()
    self.aka = self.aka.upper()
    #print(self.name, self.country, self.area, self.description, self.aka)

if __name__ == '__main__':
  c = CreateDataClass('Nigeria', 'Africa', 923768.64, 'Giant of Africa', 'Naija')
  d = CreateDataClass('Ghana', 'Africa', 238768.64, 'Gold Coast', 'Ghana')
  e = CreateDataClass('South Africa', 'Africa', 1223768.64, 'Rainbow Nation', 'SA')
  f = CreateDataClass('Kenya', 'Africa', 423768.64, 'Land of the Maasai', 'Kenya')
  print(c.name)