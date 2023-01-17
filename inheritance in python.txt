class vehicle:
    def __init__(self,sc):
        self.sc=sc
        self.sc=self.sc*100
    def dis(self):
        print(self.sc)
class Bus(vehicle):
    def __init__(self,sc):
        vehicle.__init__(self,sc)
        self.sc = sc * 100
        total = self.sc * 0.1
        self.sc = self.sc + total
        print(self.sc)


ok=vehicle(123)
ok.dis()
ok2=Bus(100)