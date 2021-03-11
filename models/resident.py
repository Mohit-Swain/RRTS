class Resident():
    def __init__(self,residentId,name,idNo,address,phoneNo):
        self.residentId = residentId
        self.name = name
        self.idNo = idNo
        self.address = address
        self.phoneNo = phoneNo


    @classmethod
    def initialize_tuple(cls,t):
        instance = cls(*t)
        return instance

    def raiseRequest(self):
        pass
