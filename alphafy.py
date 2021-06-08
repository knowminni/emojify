import emoji

def A(text):
   
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 4) and row != 0) or
         ((row == 0 or row == 3) and (col > 1 and col < 5))):    
            res = res + text
         else:
            res = res + '  '
      res = res + '\n'
   return res


def B(text):

   res = ''    
   for row in range(0, 7):
      for col in range(0, 7):
         if (col == 1 or ((row == 0 or row == 3 or row == 6) 
         and (col < 5 and col > 1)) or (col == 5 and
          (row != 0 and row != 3 and row != 6))):
            res = res + text    
         else:      
            res=res + '  '   
      res=res + '\n' 

   return res

def C(text):

   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
         if ((col == 1 and (row != 0 and row != 6)) or 
         ((row == 0 or row == 6) and (col > 1 and col < 5)) or
          (col == 5 and (row == 1 or row == 5))):  
            res = res + text    
         else:      
            res = res + '  '
      res = res + '\n' 

   return res

def D(text):

   res = ''    
   for row in range(0, 7):    
      for column in range(0, 7):     
         if (column == 1 or ((row == 0 or row == 6) and 
         (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'
   
   return res


def E(text):
   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
         if (col == 1 or ((row == 0 or row == 6) and (col > 1 and col < 6)) or 
         (row == 3 and col > 1 and col < 5)):  
            res = res + text   
         else:      
            res = res + '  ' 

      res = res + '\n'    
   
   return res


def F(text):
   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
         if (col == 1 or (row == 0 and col > 1 and col < 6)
          or (row == 3 and col > 1 and col < 5)):  
            res = res + text    
         else:      
            res = res + '  '   
             
      res = res + '\n'
   
   return res


def G(text):
   res = ''   
   for row in range(0,7):    
      for col in range(0,7):     
         if ((col == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) 
         and col > 1 and col < 5) or (row == 3 and col > 2 and col < 6) 
         or (col == 5 and row != 0 and row != 2 and row != 6)):  
            res = res + text    
         else:      
            res = res + '  ' 

      res = res + '\n'
   
   return res


def H(text):
   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
         if ((col == 1 or col == 5) or (row == 3 and col > 1 and col < 6)):  
            res = res + text    
         else:      
            res = res + '  ' 

      res = res + '\n'    
   
   return res


def I(text):
   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
        if (col == 3 or (row == 0 and col > 0 and col < 6) or 
        (row == 6 and col > 0 and col < 6)):  
            res = res + text
        else:      
            res = res + '  '  

      res = res + '\n'

   return res


def J(text):
   res = ''   
   for row in range(0,7):    
      for col in range(0,7):     
        if ((col == 4 and row != 6) or (row == 0 and col > 2 and col < 6)
         or (row == 6 and col == 3) or (row == 5 and col == 2)):  
            res = res + text   
        else:      
            res = res + '  '

      res = res + '\n'
   
   return res


def K(text):
   res = ''
   i, j = 0, 5

   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 1 or ((row == col + 1) and col != 0)):  
            res = res + text    
         elif (row == i and col == j):  
              res = res + text    
              i = i + 1  
              j = j - 1  
         else:      
            res = res + '  ' 

      res = res + '\n'
      
   return res


def L(text):
   res = ''   
   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 1 or (row == 6 and col != 0 and col < 6)):  
            res = res + text    
         else:      
            res = res + '  '   

      res = res + '\n'
   
   return res

def M(text):
   res = ''    
   for row in range(0, 7):    
      for col in range(0, 7):     
         if (col == 1 or col == 5 or (row == 2 and (col == 2 or col == 4))
          or (row == 3 and col == 3)):  
            res = res + text    
         else:      
            res = res + '  '

      res = res + '\n'

   return res


def N(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 1 or col == 5 or (row == col and col != 0 and col != 6)):  
            res = res + text
         else:      
            res = res + '  '    

      res = res + '\n' 

   return res   


def O(text):
   res = ''   
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 5) and row != 0 and row != 6) 
         or ((row == 0 or row == 6) and col > 1 and col < 5)):  
            res = res + text   
         else:      
            res = res + '  '

      res = res + '\n'     

   return res

def P(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 1 or ((row == 0 or row == 3) and col > 0 and col < 5) 
         or ((col == 5 or col == 1) and (row == 1 or row == 2))):  
            res = res + text  
         else:      
            res = res + '  '   

      res = res + '\n'
   
   return res


def Q(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if ((col == 1 and row != 0 and row != 6) or (row == 0 and col > 1 and col < 5) or (col == 5 and row != 0 and row != 5) or (row == 6 and col > 1 and col < 4) or (col == row - 1 and row > 3)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'
    
   return res

      
   return res

def R(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 1 or ((row == 0 or row == 3) and col > 1 and col < 5) or (col == 5 and row != 0 and row < 3) or (col == row - 1 and row > 2)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'    
   
   return res


def S(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if(((row == 0 or row == 3 or row == 6) and col > 1 and col < 5)
          or (col == 1 and (row == 1 or row == 2 or row == 6)) or (col == 5 and (row == 0 or row == 4 or row == 5))):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'   

   return res

def T(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (col == 3 or (row == 0 and col > 0 and col < 6)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n' 

   return res 

def U(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 5) and row != 6) or (row == 6 and col > 1 and col < 5)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'

   return res 

def V(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if(((col == 1 or col == 5) and row < 5) or (row == 6 and col == 3) or
          (row == 5 and (col == 2 or col == 4))):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'    

   return res    

def W(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 5) and row < 6) or ((row == 5 or row == 4) and col == 3)
          or (row == 6 and (col == 2 or col == 4))):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'    

   return res

def X(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 5) and (row > 4 or row < 2)) or row == col and col > 0 and col < 6 or (col == 2 and row == 4) or (col == 4 and row == 2)):  
            res = res + text    
         else:      
            res = res + '  '    
      res = res + '\n'

   return res


def Y(text):
   res = ''
   for row in range(0,7):    
      for col in range(0,7):     
         if (((col == 1 or col == 5) and row < 2) or row == col 
         and col > 0 and col < 4 or (col == 4 and row == 2) or ((col == 3) and row > 3)):  
            res = res + text    
         else:      
            res = res + '  ' 

      res = res + '\n' 

   return res


def Z(text):
   res = ''    
   for row in range(0,7):    
      for col in range(0,7):     
         if (((row == 0 or row == 6) and col >= 0 and col <= 7) or row + col==7):  
            res = res + text   
         else:      
            res = res + '  '    
      res = res + '\n'

   return res 



      
      
