"""Exact finite-field validation of the Loewy rank-stratum count.
Run: python3 loewy_rank_verify.py. Requires only Python 3 standard library.
"""
from itertools import product
from math import prod
from collections import Counter


def ops(q):
    if q == 4:
        add = lambda a,b: a ^ b
        mul = lambda a,b: ((a&1)*(b&1)) ^ (((a&1)*(b>>1)) ^ ((a>>1)*(b&1))) * 2 ^ (((a>>1)*(b>>1))*3)
        # Multiplication in F2[x]/(x^2+x+1), representatives 0,1,x,1+x.
    else:
        add = lambda a,b: (a+b)%q
        mul = lambda a,b: (a*b)%q
    neg = (lambda a:a) if q in (2,4) else (lambda a:(-a)%q)
    A=[[add(i,j) for j in range(q)] for i in range(q)]
    M=[[mul(i,j) for j in range(q)] for i in range(q)]
    N=[neg(i) for i in range(q)]
    return A,M,N

def rank(rows,q):
    if not rows:return 0
    A,M,N=ops(q)
    a=[list(x) for x in rows]
    ncol=len(a[0]); pivot=0
    for col in range(ncol):
        k=next((r for r in range(pivot,len(a)) if a[r][col]),None)
        if k is None:continue
        a[pivot],a[k]=a[k],a[pivot]
        value=a[pivot][col]
        inv=next(v for v in range(1,q) if M[value][v]==1)
        a[pivot]=[M[inv][v] for v in a[pivot]]
        for r in range(pivot+1,len(a)):
            z=a[r][col]
            if z:
                a[r]=[A[a[r][c]][N[M[z][a[pivot][c]]]] for c in range(ncol)]
        pivot+=1
        if pivot==len(a):break
    return pivot

def matmul_zero(a,b,n,q):
    A,M,_=ops(q)
    for i in range(n):
      for j in range(n):
        s=0
        for k in range(n):
          s=A[s][M[a[i*n+k]][b[k*n+j]]]
        if s:return False
    return True

def gauss(n,k,q):
    if not 0<=k<=n:return 0
    top=prod(q**(n-i)-1 for i in range(k))
    bot=prod(q**(k-i)-1 for i in range(k))
    return top//bot

def H(ell,a,b,q):
    return sum(gauss(a,i,q)*gauss(b,j,q)*(-1)**(a-i+j)*q**((a-i)*(a-i-1)//2+j*(j-1)//2+ell*i*(b-j)) for i in range(a+1) for j in range(b+1))

def predicted(n,ell,q):
    return Counter({(a,b):gauss(n,a,q)*gauss(n-a,b,q)*H(ell,a,b,q) for a in range(n+1) for b in range(n-a+1) if gauss(n,a,q)*gauss(n-a,b,q)*H(ell,a,b,q)})

def tuple_invariants(mats,n,q):
    image_matrix=[[a[i*n+j] for a in mats for j in range(n)] for i in range(n)]
    common_kernel_matrix=[[a[i*n+j] for j in range(n)] for a in mats for i in range(n)]
    return rank(image_matrix,q),rank(common_kernel_matrix,q)

def exhaustive(n,ell,q):
    squares=[m for m in product(range(q),repeat=n*n) if matmul_zero(m,m,n,q)]
    compat=[[j for j,b in enumerate(squares) if matmul_zero(a,b,n,q) and matmul_zero(b,a,n,q)] for a in squares]
    good=[set(x) for x in compat]
    counts=Counter()
    def walk(ids):
        if len(ids)==ell:
            counts[tuple_invariants([squares[j] for j in ids],n,q)]+=1
            return
        allowed=set(range(len(squares))) if not ids else good[ids[0]].copy()
        for j in ids[1:]:allowed &=good[j]
        for j in sorted(allowed):walk(ids+[j])
    walk([])
    want=predicted(n,ell,q)
    assert counts==want, f"MISMATCH q={q},n={n},ell={ell}: {counts} vs {want}"
    return len(squares),sum(counts.values()),dict(sorted(counts.items()))

def main():
    for n,ell,q in [(2,1,2),(3,1,3),(3,2,2),(3,2,3),(3,3,2),(3,3,3),(3,2,4),(4,2,2)]:
        s,total,counts=exhaustive(n,ell,q)
        print(f'PASS q={q} n={n} loops={ell} squarezero_generators={s} tuples={total} strata={counts}',flush=True)
    print('VERIFY_OK_LOEWY_RANK_STRATA_ALL_CASES')
if __name__=='__main__':main()
