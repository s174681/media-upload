import unittest
import os

from media.local_storage import LocalMediaStorage

class TestLocalMediaStorage(unittest.TestCase):
  def setUp(self):
    files = [
      self.get_full_path('storage/upl_name.txt'),
    ]

    for tmp_file in files:
      if os.path.isfile(tmp_file):
        os.remove(tmp_file)

  def get_full_path(self, file_name):
    path = os.path.join(
      os.path.dirname(__file__),
      file_name
    )
    return path

  def test_upload_file(self):
    to_upld_path = os.path.join(os.path.dirname(__file__), 'test.txt')
    to_upl_file = open(to_upld_path, 'rb')

    workspace_dir = os.path.join(os.path.dirname(__file__), 'storage')
    media_storage = LocalMediaStorage(path=workspace_dir)
    media_storage.store(key='upl_name.txt', media=to_upl_file)

    assert os.path.isfile(self.get_full_path('storage/upl_name.txt')), 'file should exists'

  def test_download_file(self):
    workspace_dir = os.path.join(os.path.dirname(__file__), 'storage')
    media_storage = LocalMediaStorage(path=workspace_dir)

    file_link = media_storage.get('uploaded.txt')

    content = file_link.read(1000)
    assert content == 'that file was uploaded'

if __name__ == '__main__':
  unittest.main()
