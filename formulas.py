Escala_Socaya = {"1":407,"2":440,"3":466,"4":480,"5":499,"6":519,"7":537,"8":556}

def Normales(Categoria, Hs_Normales):
  global Total_Normales
  Valor = Escala_Socaya[Categoria]
  Total_Normales = Valor * Hs_Normales
  
def Extras50(Categoria, Hs_50):
  global Total_50
  Valor = Escala_Socaya[Categoria]
  Total_50 = (Valor * 1.50) * Hs_50

def Extras100(Categoria, Hs_100):
  global Total_100
  Valor = Escala_Socaya[Categoria]
  Total_100 = (Valor * 2) * Hs_100
  