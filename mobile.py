class mobile:
    def __init__(self,num):
        self.number=str(num)
    
    def turn_on(self):
        return 'Mobile phone {0} is turned on'. format(self.number)
        
    
    def turn_off(self):
        return 'Mobile phone is turned off'
        
    def call(self):
        return 'Calling {}'.format(self.number)
    

m1=mobile('716-990-4010')
m2=mobile('207-330-8530')
print(m1.turn_on())
print(m2.turn_on())
print(m1.call())
print(m1.turn_off())
print(m2.turn_off())        