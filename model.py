
from pydantic import BaseModel,constr,Field

class Creature(BaseModel):
  name:str = Field(...,min_length=3,max_length=50)
  country:str
  area:str
  description:str
  aka:str

  def __post_init__(self)->None:
    self.name = self.name.upper()
    self.country = self.country.upper()
    self.area = self.area * 2
    self.description = self.description.upper()
    self.aka = self.aka.upper()
    #print(self.name, self.country, self.area, self.description, self.aka)

