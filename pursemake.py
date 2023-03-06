
class Purse:
    def __init__(self):
        self._num = 0
        self._name = 0
        self._coins = 0
        
    @property
    def num(self):
        return self._num 
    @num.setter
    def num(self,value):
        self._num = value
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    @property
    def coins(self):
        return self._coins
    @coins.setter
    def coins(self,value):
        self._coins = value
