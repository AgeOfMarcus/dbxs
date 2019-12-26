import dropbox, requests

class DBXServer(object):
	def __init__(self, db, fn):
		self.db = db
		self.fn = fn
		self._connect()
	def _connect(self):
		

class Dropbox(object):
	def __init__(self, api_key, path="/"):
		self.db = dropbox.Dropbox(api_key)
		self.path = path
	def Server(self, connection_id):
		return DBXServer(db, self.path+connection_id)
	def Client(self, connection_id):
		return DBXClient(db, self.path+connection_id)