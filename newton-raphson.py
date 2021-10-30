from math import e

#mendefinisikan fungsi


def f(x):
    return e*2**x-8*x**2

def Df(x):
    return e*2**x-16*x

# metode newton rapshon
def newtonRapshon(x0, eps):
    step = 0
    print('\n\n*** --Metode Newton Raphson-- ***')
    xn = x0
    for n in range(0,100): # maksimal interasi adalah 100
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn = xn - (fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f ' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak ditemukan')


# sesi input nilai awal yang di konversi ke pecahan
x0 = float(input('x0: '))
eps = float(input('epsilon: '))
newtonRapshon(x0, eps)