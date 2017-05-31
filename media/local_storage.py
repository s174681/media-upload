class LocalMediaStorage:
  def __init__(self, path):
    self.path = path

  def store(self, key, media):
    with open(self.get_path(key), 'w+') as output, media as input:
      while True:
        data = input.read(100000)
        if data == '':
          break
        output.write(data)

  def get(self, key):
    return open(self.get_path(key), 'r')

  def get_path(self, key):
    return '%s/%s' % (self.path, key)