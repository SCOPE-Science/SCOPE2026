"""Independent finite-field checks for the 5x5 nilpotent cubic word fibers.
Supports prime fields 2,3,5,7 and GF(4)=GF(2)[t]/(t*t+t+1).
"""
from itertools import product
from collections import Counter

def add(x,y,q): return x^y if q==4 else (x+y)%q

def mul(x,y,q):
    if q!=4: return x*y%q
    z=0
    for i in range(2):
        for j in range(2):
            if (x>>i)&1 and (y>>j)&1: z ^= 1<<(i+j)
    if z&4: z^=7
    return z

def matmult(X,Y,q):
    Z=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(i+1,5):
            z=0
            for k in range(i+1,j): z=add(z,mul(X[i][k],Y[k][j],q),q)
            Z[i][j]=z
    return Z

def check(q):
    counts=Counter()
    # all active entries of first two superdiagonals; third/fourth are free
    for a,b,c,d,e,f,g in product(range(q),repeat=7):
        X=[[0]*5 for _ in range(5)]
        for (i,j),v in zip(((0,1),(1,2),(2,3),(3,4),(0,2),(1,3),(2,4)),(a,b,c,d,e,f,g)):
            X[i][j]=v
        XX=matmult(X,X,q)
        XXX=matmult(XX,X,q)
        assert all(XXX[i][j]==0 for i in range(5) for j in range(5) if (i,j) not in {(0,3),(1,4),(0,4)})
        counts[XXX[0][3],XXX[1][4],XXX[0][4]]+=1
    def want(A,B,C):
        if A or B: return q*q*(q-1)**2
        if C: return q*q*(2*q**3-3*q*q+1)
        return q*q*(5*q**3-5*q*q+1)
    for triple in product(range(q),repeat=3): assert counts[triple]==want(*triple),(q,triple,counts[triple],want(*triple))
    assert sum(counts.values())==q**7
    print('PASS q=',q,'targets=',len(counts),'enumerated active=',q**7,
          'zero full fiber=',counts[(0,0,0)]*q**3,
          'central nonzero full fiber=',counts[(0,0,1)]*q**3,
          'noncentral full fiber=',counts[(1,0,0)]*q**3)

if __name__=='__main__':
    for q in (2,3,4,5,7): check(q)
