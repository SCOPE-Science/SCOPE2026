from fractions import Fraction as F
from itertools import permutations
from math import factorial

def check():
    b={0:F(0),1:F(1)}
    q={0:F(0),1:F(1)}
    count=0
    for n in range(2,101):
        b[n]=sum((b[k] for k in range(1,n-1)),F(0))/F(n-1)
        q[n]=sum((b[k]*b[n-2-k] for k in range(1,n-2)),F(0))/F(n-1)
        assert b[n]==sum((F((-1)**j,factorial(j)) for j in range(n)),F(0))
        count+=1
        if n>=4:
            exact=sum((F(n-3-j,n-1)*F((-2)**j,factorial(j)) for j in range(n-3)),F(0))
            assert q[n]==exact
            count+=1
        if n>=3:
            assert ((-1)**n)*(q[n]-b[n]*b[n])>0
            count+=1
    for n in range(3,10):
        left=both=total=0
        for order in permutations(range(n-1)):
            occupied=[False]*n
            for j in order:
                if not occupied[j] and not occupied[j+1]:
                    occupied[j]=occupied[j+1]=True
            u=not occupied[0]
            v=not occupied[n-1]
            left+=u
            both+=u and v
            total+=1
        assert total==factorial(n-1)
        assert F(left,total)==b[n]
        assert F(both,total)==q[n]
        count+=3
    print('PASS:',count,'exact assertions; priority enumeration through n=9, recurrence and coefficients through n=100')

if __name__=='__main__':
    check()
