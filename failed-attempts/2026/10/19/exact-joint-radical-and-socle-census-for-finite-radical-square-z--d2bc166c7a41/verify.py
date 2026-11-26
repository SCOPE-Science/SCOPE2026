"""Exact finite-prime-field checks of a joint image/kernel distribution for product-zero tuples.
Run: python3 verify.py. Standard library only; independent direct matrix enumeration.
"""
from itertools import product
from math import prod


def rank(rows, q):
    a=[list(r) for r in rows]
    if not a: return 0
    h=len(a); w=len(a[0]); piv=0
    for c in range(w):
        t=next((i for i in range(piv,h) if a[i][c]%q),None)
        if t is None: continue
        a[piv],a[t]=a[t],a[piv]
        z=pow(a[piv][c],-1,q)
        a[piv]=[(v*z)%q for v in a[piv]]
        for j in range(h):
            if j!=piv:
                m=a[j][c]
                if m:
                    a[j]=[(v-m*a[piv][l])%q for l,v in enumerate(a[j])]
        piv+=1
        if piv==h: break
    return piv


def gb(n,r,q):
    if r<0 or r>n: return 0
    num=prod(q**(n-j)-1 for j in range(r))
    den=prod(q**(j+1)-1 for j in range(r))
    return num//den


def F(r,t,k,q):
    ans=0
    for a in range(r+1):
        inject=prod(q**(k*a)-q**j for j in range(t))
        ans+=(-1)**(r-a)*q**((r-a)*(r-a-1)//2)*gb(r,a,q)*inject
    return ans


def predicted(n,k,q):
    return {(r,t):gb(n,r,q)*gb(n-r,t,q)*F(r,t,k,q)
            for r in range(n+1) for t in range(n-r+1)
            if gb(n,r,q)*gb(n-r,t,q)*F(r,t,k,q)}


def mult_is_zero(a,b,n,q):
    for i in range(n):
        for j in range(n):
            if sum(a[i*n+s]*b[s*n+j] for s in range(n))%q:
                return False
    return True


def direct(n,k,q):
    mats=list(product(range(q),repeat=n*n))
    square_zero=[a for a in mats if mult_is_zero(a,a,n,q)]
    ans={}
    for tup in product(square_zero,repeat=k):
        if any(not mult_is_zero(a,b,n,q) for a in tup for b in tup):
            continue
        # Joint image dimension = row rank of horizontal concatenation of matrices.
        horizontal=[[v[i*n+j] for v in tup for j in range(n)] for i in range(n)]
        # Common-kernel codimension = column rank of vertical concatenation.
        vertical=[[a[i*n+j] for j in range(n)] for a in tup for i in range(n)]
        r=rank(horizontal,q); t=rank(vertical,q)
        ans[(r,t)]=ans.get((r,t),0)+1
    return ans


def main():
    cases=[(2,2,2),(2,3,2),(3,2,2),(2,2,3)]  # n,k,q
    for n,k,q in cases:
        got=direct(n,k,q)
        exp=predicted(n,k,q)
        assert got==exp,(n,k,q,got,exp)
        assert all(got.get((r,t),0)==got.get((t,r),0) for r,t in got)
        print(f'PASS n={n} k={k} q={q}: total={sum(got.values())}; strata={sorted(got.items())}')
    for q in [2,3,4,5]:
        for n in range(1,7):
            for k in [2,3,4]:
                p=predicted(n,k,q)
                assert all(v>=0 for v in p.values())
                assert all(p.get((r,t),0)==p.get((t,r),0) for r,t in p)
    print('CHECKER_OK')

if __name__=='__main__': main()
