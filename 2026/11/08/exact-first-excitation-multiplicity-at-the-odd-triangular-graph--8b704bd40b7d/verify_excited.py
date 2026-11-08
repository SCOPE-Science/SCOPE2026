"""Exact independent finite checks for the Ising three-defect shell."""
from math import comb, factorial

def double_factorial(k):
    p = 1
    for j in range(k, 0, -2):
        p *= j
    return p

def formulas(n):
    assert n >= 5 and n % 2 == 1
    m = (n - 3) // 2
    d0 = n*(n+1)//2*double_factorial(n-2)
    numerator = factorial(n)//factorial(n-3) * double_factorial(n-4) * (m**3+6*m*m+8*m+2)
    assert numerator % 6 == 0
    return d0, numerator//6

def structural(n):
    p=n-3
    m=p//2
    pref=factorial(n)//factorial(p)*double_factorial(p-1)
    s=0
    for t in range(4):
        numer=factorial(t)*comb(t+m-1,m-1)+(1 if t==3 else 0)
        s += pref * numer // (factorial(t)*factorial(3-t))
    return s

def exhaustive(n):
    edges=[(a,b) for a in range(n) for b in range(a+1,n)]
    c0=c1=0
    for mask in range(1<<len(edges)):
        ds=[0]*n
        for k,(a,b) in enumerate(edges):
            if (mask>>k)&1:
                ds[a]+=1;ds[b]+=1
        defect=sum((d-1)**2 for d in ds)
        assert defect%2==1
        if defect==1:c0+=1
        if defect==3:c1+=1
    return c0,c1

if __name__=='__main__':
    for n in range(5,36,2):
        assert formulas(n)[1] == structural(n),n
    for n in [5,7]:
        assert exhaustive(n) == formulas(n), (n,exhaustive(n),formulas(n))
    assert formulas(5)==(45,170)
    assert formulas(7)==(420,5250)
    assert formulas(9)==(4725,134820)
    print('PASS: exact structural sums, finite exhaustive edge configurations, and integer formula checks')
