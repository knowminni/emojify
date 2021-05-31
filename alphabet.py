import emoji

def A():
   res = ''   
   for row in range(0, 7):    
      for column in range(0, 7):     
         if (((column == 1 or column == 5) and row != 0) 
         or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            res = res + emoji.emojize(':pizza:')    
         else:      
            res = res + ' '    
      res = res + '\n'   

   print(res, sep = ' ')

def B():

   res = ''    
   for row in range(0, 7):
      for col in range(0, 7):
         if (col == 1 or ((row == 0 or row == 3 or row == 6) 
         and (col < 5 and col > 1)) or (col == 5 and (row != 0 and row != 3 and row != 6))):
            res = res + emoji.emojize(':fire:')    
         else:      
            res=res + ' '   
      res=res + '\n' 

   print(res, sep = ' ')

A()
B()