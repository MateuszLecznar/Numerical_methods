import main

import numpy as np
import scipy
import matplotlib.pyplot as plt
import math



def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r<0:
        return math.nan
    if h<0:
        return math.nan
    else:
        return 2*r*r*math.pi+2*math.pi*r*h

    

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if isinstance(n, int) and n>0:


        result = [1,1]
        if n==1:
            return result[0]

        for i in range(n-2):
            result.append(result[i]+ result[(i + 1)])
    
        return np.array([result])

    else:
         return None

    
    

    

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    
    b=np.array(([a,1,-a],[0,1,1],[-a,a,1]))
    if np.linalg.det(b)!=0:
        Minv=np.linalg.inv(b)
        Mt=np.transpose(b)
        Mdet=np.linalg.det(b)
        return (Minv,Mt,Mdet)
    else :
        Minv=math.nan
        Mt=np.transpose(b)
        Mdet=np.linalg.det(b)
        return (Minv,Mt,Mdet)

   

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if isinstance(m,int) and isinstance(n,int) and n>0 and m>0:
        M=np.ones((m,n))
        
        j = 0
        for i in range(m):
            if i>j:
                M[i,j]=i
            if i<=j:
                    M[i,j]=j
            for j in range(n):
                if i<=j:
                    M[i,j]=j
                if i>j:
                    M[i,j]=i
        return M
    else:       
        return None
print(custom_matrix(5,6))