class A:
    def __init__(self, a):
      self.a = A
    def __lt__(self, other):
       if(self.a<other.a):
          return"ob1 is less than ob2"
       else:
          return"on2 is less than ob1"
       def __eq__(self, other):
          if(self.a == other.a):
             return"both are equal"
          else:
             return"not equal"
ob1 = A(2)
ob2 = A(3)
print("passed values :", ob1.a, ob2.a)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print("passed values :", ob3.a, ob4.a)
print( ob3 == ob4)
class flashcard:
   def __init__(self, word, meaning):
      self.word = word
      self.meaning = meaning
   def __str__(self):
      return self.word+' ('+self.meaning+' )'
flash = []
print("welcome to flashcard application")
while(True):
   word = input("enter the name you want to add to flashcard : ")
   meaning = input("enter the meanign of the word : ")
   flash.append(flashcard(word, meaning))
   option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 :"))
   if(option):
      break