from fractions import Fraction as F
from itertools import product
from math import comb

def critical(n):
    return F(n-2,2*n) if n%2==0 else F((n-1)**2,2*n*n)

def expected(n,k):
    af=-F(n-1)+k*n
    bal=F(n%2,n)-1-k*n
    if k<critical(n): return af,'AF'
    if k>critical(n): return bal,'BAL'
    return af,'TIE'

def tests():
    checks=0
    for n in range(3,9):
        ks=(F(0),critical(n)-F(1,10*n*n),critical(n),critical(n)+F(1,10*n*n),F(3,4),F(10))
        for k in ks:
            p,q=k.numerator,k.denominator
            best=None; states=[]
            spins=list(product((-1,1),repeat=n))
            for a in spins:
                ma=sum(a)
                for b in spins:
                    ab=sum(x*y for x,y in zip(a,b))
                    e=ma*sum(b)*q-(q+n*p)*ab
                    if best is None or e<best: best=e; states=[(a,b)]
                    elif e==best:states.append((a,b))
            ex,phase=expected(n,k)
            assert F(best,n*q)==ex,(n,k,best,ex)
            if phase=='AF': assert len(states)==2 and all(all(x==a[0] and y==-a[0] for x,y in zip(a,b)) for a,b in states)
            elif phase=='BAL':
                g=comb(n,n//2) if n%2==0 else 2*comb(n,(n+1)//2)
                assert len(states)==g and all(a==b and abs(sum(a))==n%2 for a,b in states)
            else:
                g=comb(n,n//2) if n%2==0 else 2*comb(n,(n+1)//2)
                assert len(states)==2+g
            checks+=1
    print('PASS exact brute-force all spins n=3..8:',checks,'parameter tests',flush=True)
    count=0
    for n in range(9,61):
        for k in (F(0),critical(n),F(1),F(10)):
            p,q=k.numerator,k.denominator
            best=None
            for ap in range(n+1):
                ma=2*ap-n
                for bp in range(n+1):
                    mb=2*bp-n
                    for pp in range(max(0,ap+bp-n),min(ap,bp)+1):
                        ab=n-2*(ap+bp-2*pp)
                        e=ma*mb*q-(q+n*p)*ab
                        if best is None or e<best:best=e
            ex,phase=expected(n,k)
            assert F(best,n*q)==ex,(n,k,phase,F(best,n*q),ex)
            count+=1
    print('PASS independent four-state pair-composition optimization n=9..60:',count,'parameter tests')
if __name__=='__main__':tests()
