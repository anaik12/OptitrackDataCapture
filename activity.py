class Activity:
    
    def __init__(self, sourceId, posx, posy, posz, orw, orx, ory, orz, time):
        self.sourceId = sourceId
        self.posx = posx
        self.posy = posy
        self.posz = posz
        self.orw = orw
        self.orx = orx
        self.ory = ory
        self.orz = orz
        self.time = time
        
        def __repr__(self):
            return "Activity({},{},{},{},{},{},{},{},{})".format(self.sourceId, self.posx, self.posy, self.posz, self.orw, self.orx, self.ory, self.orz, self.time)