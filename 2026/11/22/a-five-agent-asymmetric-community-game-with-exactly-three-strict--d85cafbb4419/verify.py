"""Exact, standard-library checks for the two-community Nash census.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache

def solve(A, b):
    n = len(b)
    aug = [[F(A[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for k in range(n):
        j = next(i for i in range(k, n) if aug[i][k] != 0)
        aug[k],aug[j] = aug[j],aug[k]
        z = aug[k][k]
        aug[k] = [t/z for t in aug[k]]
        for i in range(n):
            if i==k:continue
            z=aug[i][k]
            if z:aug[i]=[a-z*b for a,b in zip(aug[i],aug[k])]
    return [aug[i][-1] for i in range(n)]

def matrix(a, b, within, cross):
    n=a+b
    W=[]
    for i in range(n):
        row=[]
        for j in range(n):
            v=F(0) if i==j else (within if (i<a)==(j<a) else cross)
            row.append(F(v))
        den=sum(row)
        W.append([z/den for z in row])
    return W

@lru_cache(maxsize=None)
def resolvent(a,b,within,cross,q):
    W=matrix(a,b,within,cross);n=a+b
    M=[[int(i==j)-q*W[i][j] for j in range(n)] for i in range(n)]
    cols=[solve(M,[int(i==j) for i in range(n)]) for j in range(n)]
    return W,tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))

def equilibria(a,b,within,cross,q,theta):
    W,inv=resolvent(a,b,within,cross,q);n=a+b
    eq=[]
    for x in product((0,1),repeat=n):
        y=[(1-q)*sum(inv[i][j]*x[j] for j in range(n)) for i in range(n)]
        z=[sum(W[i][j]*y[j] for j in range(n)) for i in range(n)]
        if all(z[i]>theta if x[i]==1 else z[i]<theta for i in range(n)):
            eq.append((x,tuple(y),tuple(z)))
    return eq

def predicted(a,b,within,cross,q,theta):
    pA=F((a-1)*within,(a-1)*within+b*cross)
    pB=F((b-1)*within,(b-1)*within+a*cross)
    den=1-q*(pA+pB-1)
    lA=(1-pB)/den
    uA=(q*(1-pB)+(1-q)*pA)/den
    lB=(1-pA)/den
    uB=(q*(1-pA)+(1-q)*pB)/den
    patterns=[(0,)*(a+b)]
    if theta<1:patterns.append((1,)*(a+b))
    if lA<theta<uA:patterns.append((1,)*a+(0,)*b)
    if lB<theta<uB:patterns.append((0,)*a+(1,)*b)
    return set(patterns), (pA,pB,den,lA,uA,lB,uB)

def main():
    ncheck=0; profiles=0
    for a in range(1,5):
      for b in range(1,5):
       if a+b>7:continue
       for within in (1,2,4,8):
        for cross in (1,2):
         for q in (F(1,3),F(1,2),F(3,4)):
          for theta in (F(1,2)+F(1,64),F(9,16),F(5,8),F(3,4),F(15,16),F(17,16)):
           obs=equilibria(a,b,within,cross,q,theta)
           calc,_=predicted(a,b,within,cross,q,theta)
           assert set(x for x,_,_ in obs)==calc,(a,b,within,cross,q,theta,obs,calc)
           ncheck+=1; profiles+=2**(a+b)
    a,b,within,cross=3,2,4,1
    q,theta=F(1,2),F(5,8)
    eq=equilibria(a,b,within,cross,q,theta)
    assert {x for x,_,_ in eq}=={(0,0,0,0,0),(1,1,1,1,1),(1,1,1,0,0)}
    m=[r for r in eq if r[0]==(1,1,1,0,0)][0]
    assert m[1]==(F(50,57),)*3+(F(5,19),)*2,m
    assert m[2]==(F(43,57),)*3+(F(10,19),)*2,m
    _,(pa,pb,den,lA,uA,lB,uB)=predicted(a,b,within,cross,q,theta)
    assert (pa,pb,den,lA,uA,lB,uB)==(F(4,5),F(4,7),F(57,70),F(10,19),F(43,57),F(14,57),F(9,19))
    print('PASS',ncheck,'parameter cases;',profiles,'enumerated profiles; example: exactly three equilibria')

if __name__=='__main__':main()
