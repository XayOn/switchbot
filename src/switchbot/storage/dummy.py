class DummyMeterStorage:
    def __init__(self, storage):
        self.store = storage 

    def append(self, data):
        self.store.append(data)

    def latest(self):
        return self.store[-1]

    def all(self):
        return self.store
