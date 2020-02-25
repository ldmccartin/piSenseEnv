from getEnvSenseData import grab_data

class EnvSenseData:
  def __init__(self):
    self.myList = []

  def store_data(self):
    self.myList.append(grab_data())

  def get_data(self):
      return self.myList

