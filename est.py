
#statistical  relationship for residential buildings (CBRI Rookee Building Research notes) for less than 300 sqm Plinth_area

# prepare a class name  Building_materials which cointain the statistical relationship for single storey
class Building_materials:
  def __init__(self,A=0):
      if  A < 300 :
          self.F1 = round(0.153*A + 0.57 ,3)
          self.F2 = round(0.47*A-7 ,3)
          self.F3 = round(21.31*A-314 ,3)
          self.F4 = round(2.26*A+66.8 ,3)
          self.F5 = round(0.113*A-0.83 ,3)
          self.F6 = round(0.176*A-0.21 ,3)
          self.F7 = round(0.145*A+ 1.5 ,3)
          self.F8 = round(1.335*A + 28 ,0)
          self.F9 = round(1.184*A - 9 ,0)
          self.F10 = round(0.19*A ,0)
          self.F11 = round(0.269*A - 4 ,0)
          self.F12 = round(4.769*A+ 32 ,0)
      else:
        return None
  def funtion(self):
        print("MATERIAL")
        print("cement",self.F1,"cum")
        print("sand",self.F2,"cum")
        print("steel",self.F3,"kg")
        print("Bricks",self.F4,"100 nos")
        print("Bricks aggregate",self.F5,"cum")
        print("20 mm and down aggregate",self.F6,"cum")
        print("40 mm and down aggregate",self.F7,"cum")
        print("LABOUR")
        print("Mason", "day", self.F8)
        print("Carpenter", "day", self.F9)
        print("Pinter", "day", self.F10)
        print("Blacksmith", "day", self.F11)
        print("Mazdor", "day", self.F12)

# prepare a class name  Building_materials2 which cointain the statistical relationship for double storey
class Building_materials2 :
  def __init__(self,A=0):
      if A < 300 :
          self.F1 = round(0.145*A+ 0.54 ,3)
          self.F2 = round(.43*A-5.6 ,3)
          self.F3 = round(21.97*A-305 ,3)
          self.F4 = round(2.15*A+63 ,3)
          self.F5 = round(0.056*A-0.42 ,3)
          self.F6 = round(.178*A-.21 ,3)
          self.F7 = round(.075*A-0.78 ,3)
          self.F8 = round(1.355*A +63,0)
          self.F9 = round(1.194*A-9 ,0)
          self.F10 = round(.19*A ,0)
          self.F11 = round(.274*A-1.40 ,0)
          self.F12 = round(4.91*A+ 13 ,0)
      else:
        return None
  def funtion(self):
        print("MATERIAL")
        print("cement",self.F1,"cum")
        print("sand",self.F2,"cum")
        print("steel",self.F3,"kg")
        print("Bricks",self.F4,"100 nos")
        print("Bricks aggregate",self.F5,"cum")
        print("20 mm and down aggregate",self.F6,"cum")
        print("40 mm and down aggregate",self.F7,"cum")
        print("LABOUR")
        print("Mason", "day", self.F8)
        print("Carpenter", "day", self.F9)
        print("Pinter", "day", self.F10)
        print("Blacksmith", "day", self.F11)
        print("Mazdor", "day", self.F12)

# #prepare a class name floor which cointain the two class Building_materials and Building_materials2 to call them accordeingly user input
# of floor and plinth area
class flor():
    def __init__(self,Storey,A=0):
        if Storey == 1: 
            global x
            x = Building_materials(A)
            x.funtion()
        elif Storey == 2:
            global y
            y = Building_materials2(A)
            y.funtion()
x=None
y=None


Storey = int(input("Storey:"))
A = int(input("Plinth_area:"))

z = flor(Storey,A)



