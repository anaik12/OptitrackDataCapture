class Activity:
    
    def __init__(self, date, sourceId, posx, posy, posz, orx, ory, orz):
        self.date = date
        self.sourceId = sourceId
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.orx = orx
        self.ory = ory
        self.orz = orz
        
        def __repr__(self):
            return "Activity('{}',{},{},{},{},{},{},{})".format(self.date, self.sourceId, self.posx, self.posy, self.posz, self.orx, self.ory, self.orz)