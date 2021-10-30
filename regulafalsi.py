import numpy as np
import matplotlib.pyplot as plt
from math import e

#mendefinisikan fungsi


def f(x):
    return e*2**x-8*x**2


# sesi input nilai awal yang di konversi ke pecahan
x0 = float(input('x0: '))
x1 = float(input('x1: '))
eps = float(input('epsilon: '))

# metode regulafalse
def regulafalse(x0, x1, eps):
    step = 1
    print('\n\n*** --Metode Regulafalse-- ***')
    condition = True
    while condition:
        x2 = x1-(f(x1)*(x1-x0)/(f(x1)-f(x0)))
        print('Iterasi-%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > eps

    print('\n Akar persamaan tersebut : %0.8f' % x2)


# pengecekan nilai awal
if f(x0) * f(x1) > 0.0:
    print('Nilai yang di prediksi tidak mengurung akar')
    print('Silahkan mencoba ulang prediksi nilai baru')
else:
    regulafalse(x0, x1, eps)

#  menggambar fungsi
rr = np.linspace(0, 2, 100)  # masukkan nilai tebakan awal
plt.plot(rr, f(rr))
plt.show()
plt.savefig("fungsi.png")  # untuk menyimpan gambar fungsi
