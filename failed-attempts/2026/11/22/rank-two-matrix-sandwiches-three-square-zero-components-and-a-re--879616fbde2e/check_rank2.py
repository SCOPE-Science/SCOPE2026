"""Direct matrix-product tests for square-zero elements of rank-two sandwich algebras.
Run: python check_rank2.py
"""
from itertools import product
from collections import Counter


def plus(x,y,q):
    return x^y if q==4 else (x+y)%q

def times(x,y,q):
    if q!=4: return x*y%q
    out=0
    while y:
        if y&1: out^=x
        y>>=1; x<<=1
        if x&4: x^=7
    return out

def matmul(A,B,r,s,t,q):
    C=[0]*(r*t)
    for i in range(r):
        for j in range(t):
            z=0
            for h in range(s): z=plus(z,times(A[i*s+h],B[h*t+j],q),q)
            C[i*t+j]=z
    return C

def rank(A,r,s,q):
    M=[list(A[i*s:(i+1)*s]) for i in range(r)]
    piv=0
    for j in range(s):
        p=next((i for i in range(piv,r) if M[i][j]),None)
        if p is None: continue
        M[p],M[piv]=M[piv],M[p]
        pv=M[piv][j]
        # use powers for inverse in small fields
        inv=next(t for t in range(1,q) if times(t,pv,q)==1)
        M[piv]=[times(x,inv,q) for x in M[piv]]
        for i in range(r):
            if i!=piv and M[i][j]:
                c=M[i][j]
                M[i]=[plus(x,times(c,y,q),q) if q==4 else (x-times(c,y,q))%q for x,y in zip(M[i],M[piv])]
        piv+=1
        if piv==r: break
    return piv

def formula(q,a,b):
    F=q**(2*a)+(q+1)*(q**b-1)*q**a+(q**b-1)*(q**b-q)
    return q**(a*b)*(F+(q*q-1)*q**(a+b))

def test(q,a,b):
    m=a+2;n=b+2
    J=[int(i==j and i<2) for i in range(n) for j in range(m)]
    total=0
    classes=Counter()
    for x in product(range(q),repeat=m*n):
        XX=matmul(matmul(x,J,m,n,m,q),x,m,m,n,q)
        if not any(XX):
            total+=1
            P=[x[i*n+j] for i in range(2) for j in range(2)]
            Q=[x[i*n+j] for i in range(2) for j in range(2,n)]
            R=[x[i*n+j] for i in range(2,m) for j in range(2)]
            classes[(rank(P,2,2,q),rank(Q,2,b,q),rank(R,a,2,q))]+=1
    assert total==formula(q,a,b),(q,a,b,total,formula(q,a,b))
    print('PASS', 'q',q,'a',a,'b',b,'square_zero',total,'rank_profile',sorted(classes.items()))

if __name__=='__main__':
    for z in [(2,0,0),(2,1,1),(2,1,2),(2,2,1),(2,2,2),(3,0,1),(3,1,1),(4,0,1)]:
        test(*z)
    print('ALL RANK-TWO CHECKS PASSED')
