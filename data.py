from model import Creature

_creater:list[Creature] = [
  Creature(name="lion", country="kenya", area="savannah", description="king of the jungle", aka="simba"),
  Creature(name="tiger", country="india", area="jungle", description="king of the jungle", aka="simba"),
  Creature(name="elephant", country="tanzania", area="savannah", description="king of the jungle", aka="simba"),
  Creature(name="rhino", country="tanzania", area="savannah", description="king of the jungle", aka="simba"),
  Creature(name="giraffe", country="south Africa", area="*", description="king of the jungle", aka="simba"),
  Creature(name="Red fox", country="ethiopia", area="savannah", description="king of the jungle", aka="simba"),
]

def get_creature()-> dict:
    return _creater