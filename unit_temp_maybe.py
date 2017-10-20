class unit:
  def attack(self,defender):
    toReturn = self.level-defender.level+self.advantageOver(defender)
    #1 is sword, 2 is spear, 3 is axe?
	def advantageOver(self,defender)
    advantage = defender.type-self.type
    if advantage == -2:
      return -1
    elif advantange == -1:
      return 1
    elif advantage == 0:
      return 0
    elif advantage == 1:
      return -1
    elif advantage == 2:
      return 1
