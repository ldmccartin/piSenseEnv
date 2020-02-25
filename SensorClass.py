from getEnvSenseData import grab_data

class EnvSenseData:
  def __init__(self):
    self.myList = []

  def store_data(self):
    self.myList.append(grab_data())

  def get_data(self):
    return self.myList

  def print_data(self):
    print(self.myList)

#Consider changing all this to:
#handle the fetch from sensor -> upload to dynamo in one function?
