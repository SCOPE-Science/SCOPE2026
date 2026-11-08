"""Self-contained exact finite-field direct verification for square-zero matrices over dual numbers."""
from itertools import product
from collections import Counter
from math import prod

def ops(q):
    if q==4:
        def add(a,b):return a^b
        def mul(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):z ^= 1<<(i+j)
            if z&8:z ^= 0b1100
            if z&4:z ^= 0b111
            return z
    else:
        def add(a,b):return (a+b)%q
        def mul(a,b):return (a*b)%q
    return add,mul

def rank(M, q, add,mul):
    a=[list(row) for row in M]; rows=len(a); cols=len(a[0]) if rows else 0; k=0
    for j in range(cols):
        pivot=next((i for i in range(k,rows) if a[i][j]),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=next(t for t in range(1,q) if mul(a[k][j],t)==1)
        a[k]=[mul(x,inv) for x in a[k]]
        for i in range(rows):
            if i!=k and a[i][j]:
                z=a[i][j]
                a[i]=[add(x, -mul(z,y)%q) if q!=4 else add(x,mul(z,y)) for x,y in zip(a[i],a[k])]
        k+=1
        if k==rows:break
    return k

def matmul(A,B,n,add,mul):
    return [sum(((mul(A[i*n+k],B[k*n+j]) for k in range(n))),0)%997 for i in range(n) for j in range(n)] if False else [ _sum([mul(A[i*n+k],B[k*n+j]) for k in range(n)],add) for i in range(n) for j in range(n)]

def _sum(vals,add):
    z=0
    for v in vals:z=add(z,v)
    return z

def theoretical(n,q):
    def gaussian(n,r):
        t=1
        for j in range(r):t=t*(q**(n-j)-1)//(q**(r-j)-1) if False else t
        num=prod(q**(n-j)-1 for j in range(r));den=prod(q**(r-j)-1 for j in range(r))
        return num//den
    def gl(r):return prod(q**r-q**i for i in range(r))
    counts=Counter()
    for r in range(n//2+1):
        h=n-2*r
        choices=gaussian(n,r)*gaussian(n-r,r)*gl(r)*q**(2*r*r+2*r*h)
        for s in range(h+1):
            bcount=gaussian(h,s)*prod(q**h-q**i for i in range(s))
            counts[2*r+s]+=choices*bcount
    return counts

def brute(n,q):
    add,mul=ops(q); counters=Counter(); zmat=[0]*(n*n)
    for A in product(range(q),repeat=n*n):
        if matmul(A,A,n,add,mul)!=zmat: continue
        for B in product(range(q),repeat=n*n):
            ab=matmul(A,B,n,add,mul);ba=matmul(B,A,n,add,mul)
            if any(add(x,y)!=0 for x,y in zip(ab,ba)):continue
            M=[]
            for i in range(n):M.append([A[i*n+j] for j in range(n)]+[0]*n)
            for i in range(n):M.append([B[i*n+j] for j in range(n)]+[A[i*n+j] for j in range(n)])
            counters[rank(M,q,add,mul)]+=1
    return counters

def main():
    for n,q in [(1,2),(1,3),(2,2),(2,3),(2,4),(3,2)]:
        obs=brute(n,q); exp=theoretical(n,q)
        assert obs==exp,(n,q,obs,exp)
        print('DIRECT_SQUARE_ZERO_RANK_MATCH',n,q,sorted(obs.items()),'total',sum(obs.values()))
    for n in range(1,9):
        for q in (2,3,4,5):
            p=theoretical(n,q)
            assert sum(p.values())>0 and max(p)<=n
            acyclic=p[n]
            formula=0
            for r in range(n//2+1):
                h=n-2*r
                a=prod(q**(n-j)-1 for j in range(r))//prod(q**(r-j)-1 for j in range(r))
                b=prod(q**(n-r-j)-1 for j in range(r))//prod(q**(r-j)-1 for j in range(r))
                GL=prod(q**r-q**i for i in range(r));GLh=prod(q**h-q**i for i in range(h))
                formula+=a*b*GL*q**(2*r*r+2*r*h)*GLh
            assert acyclic==formula,(n,q,acyclic,formula)
    print('ACYCLIC_FORMULAS_OK')
    print('DUAL_NUMBER_DIFFERENTIAL_RANK_CENSUS_OK')
if __name__=='__main__':main()
