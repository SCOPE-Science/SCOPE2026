"""Independent character-transform check for proper four-colourings of K_{2,n}.
Python 3, standard library only. Run: python verify_fourier.py
"""
from itertools import product

def apply(g,a,b):return (a+b)%4 if g=='C4' else a^b

def char(g,k,x):
    if g=='C4':return (1,1j,-1,-1j)[(k*x)%4]
    return (-1)**(((k&1)*(x&1))+(((k>>1)&1)*((x>>1)&1)))

def DFT(g,n):
    d=n+2; N=4**d
    arr=[]
    for digits in product(range(4),repeat=d):
        a,b=digits[:2]; rest=digits[2:]
        arr.append(complex(1 if all(c not in (a,b) for c in rest) else 0))
    for j in range(d):
        stride=4**(d-j-1); period=4*stride
        for block in range(0,N,period):
            for off in range(stride):
                old=[arr[block+q*stride+off] for q in range(4)]
                new=[sum(char(g,k,q)*old[q] for q in range(4)) for k in range(4)]
                for k in range(4):arr[block+k*stride+off]=new[k]
    assert all(z.real.is_integer() and z.imag.is_integer() for z in arr)
    four=sum((int(z.real)**2+int(z.imag)**2)**2 for z in arr)
    assert four%N==0
    return four//N

def formula(g,n):
    h={'C4':{2:2,4:12,6:30,8:1,10:18,21:1},
       'V4':{4:18,6:24,8:3,10:18,21:1}}[g]
    return 64*sum(a*t**n for t,a in h.items())

for n in range(1,5):
    for g in ('C4','V4'):
        energy=DFT(g,n)
        assert energy==formula(g,n),(n,g,energy,formula(g,n))
        print(n,g,'additive-energy',energy)
print('PASS: independent exact tensor Fourier check for n=1,2,3,4')
