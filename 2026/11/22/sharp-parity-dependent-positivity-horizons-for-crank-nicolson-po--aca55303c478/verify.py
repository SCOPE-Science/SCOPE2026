#!/usr/bin/env python3
"""Exact-rational checks for Crank--Nicolson powers on unit stars."""
from fractions import Fraction as F

def mul(A,B):
    n=len(A)
    return [[sum((A[i][t]*B[t][j] for t in range(n)), F(0)) for j in range(n)] for i in range(n)]

def inv(A):
    n=len(A)
    B=[list(A[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        p=next(i for i in range(col,n) if B[i][col])
        B[col],B[p]=B[p],B[col]
        d=B[col][col]
        B[col]=[v/d for v in B[col]]
        for i in range(n):
            if i != col:
                z=B[i][col]
                B[i]=[B[i][j]-z*B[col][j] for j in range(2*n)]
    return [r[n:] for r in B]

def check():
    assertions=0
    hs=[F(1,100),F(1,2),F(1),F(3),F(10),F(30),F(100)]
    for m in range(2,9):
        n=m+1
        L=[[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(1,n):
            L[0][0]+=1;L[i][i]+=1;L[i][0]-=1;L[0][i]-=1
        for h in hs:
            B=[[F(int(i==j))+h*L[i][j]/2 for j in range(n)] for i in range(n)]
            D=[[F(int(i==j))-h*L[i][j]/2 for j in range(n)] for i in range(n)]
            C=mul(inv(B),D)
            a=(2-h)/(2+h)
            b=(2-(m+1)*h)/(2+(m+1)*h)
            T=[[F(int(i==j)) for j in range(n)] for i in range(n)]
            for k in range(1,10):
                T=mul(T,C)
                hd=(1+m*b**k)/F(m+1)
                hl=(1-b**k)/F(m+1)
                ld=(m+(m*m-1)*a**k+b**k)/F(m*(m+1))
                lo=(m-(m+1)*a**k+b**k)/F(m*(m+1))
                for i in range(n):
                    for j in range(n):
                        e=hd if (i==0 and j==0) else hl if (i==0 or j==0) else ld if i==j else lo
                        assert T[i][j]==e
                        assertions+=1
                        if i!=j:
                            assert e>0
                            assertions+=1
                assert all(sum(T[i])==1 for i in range(n));assertions+=1
                assert hl>0 and lo>0;assertions+=1
                if k%2==0:
                    assert hd>0 and ld>0
                else:
                    q=F(m)**F(-1,k) if False else m**(-1/k)
                    threshold=(2/(m+1))*(1+q)/(1-q)
                    assert (float(h)<threshold)==(hd>0) or abs(float(h)-threshold)<1e-12
                    assert ld>hd
                assertions+=1
    # A four-vertex path is an exact counterexample to the star-specific even-power property.
    L=[[F(0) for j in range(4)] for i in range(4)]
    for i,j in [(0,1),(1,2),(2,3)]:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    h=F(30)
    C=mul(inv([[F(int(i==j))+h*L[i][j]/2 for j in range(4)] for i in range(4)]),
          [[F(int(i==j))-h*L[i][j]/2 for j in range(4)] for i in range(4)])
    assert mul(C,C)[0][1] == F(-5111040,250937281)
    assertions+=1
    print('VERIFY_OK',assertions)

if __name__=='__main__':check()
