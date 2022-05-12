
class Config:

    def __init__(self, fabricName: str=None, last_run: str=None):
        self.update(fabricName, last_run)

    def update(self, fabricName: str, last_run: str):
        self.fabricName = fabricName
        self.last_run = last_run
