#!/usr/bin/env python3
"""Small-field direct verification of idempotent derivation rank spectra.

Enumerates the complete derivation normal form, tests its ORIGINAL
Leibniz identity and idempotence, and counts ranks. No counting formula
is used by the enumerator. Works over GF(2), GF(3), and GF(4).
"""
from itertools import product
from collections import Counter
from math import prod


def field(q):
    if q == 4:
        return lambda a,b: a^b, lambda a,b: (((a&1)*(b&1)) ^ ((a>>1)*(b>>1))) | (((((a&1)*(b>>1)) ^ ((a>>1)*(b&1)) ^ ((a>>1)*(b>>1))) & 1) << 1)
    return lambda a,b: (a+b)%q, lambda a,b: (a*b)%q


def matmul(A,B,q,add,mul):
    return [[sum_field((mul(A[i][h],B[h][j]) for h in range(len(B))), add) for j in range(len(B[0]))] for i in range(len(A))]


def sum_field(vals,add):
    r=0
    for v in vals:r=add(r,v)
    return r


def rank(A,q,add,mul):
    a=[row[:] for row in A];m=len(a);n=len(a[0]);r=0
    for j in range(n):
        p=next((i for i in range(r,m) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        inv=next(v for v in range(1,q) if mul(v,a[r][j])==1)
        for k in range(j,n):a[r][k]=mul(inv,a[r][k])
        for i in range(m):
            if i==r or a[i][j]==0:continue
            fac=a[i][j]
            for k in range(j,n):a[i][k]=add(a[i][k],neg(mul(fac,a[r][k]),q))
        r+=1
        if r==m:return r
    return r


def neg(a,q):
    return a if q%2==0 else (-a)%q


def predicted(n,q):
    def sp(k):return q**(k*k)*prod(q**(2*i)-1 for i in range(1,k+1))
    def gl(k):return prod(q**k-q**i for i in range(k))
    out=Counter()
    if q%2:
        out[0]=1
    else:
        for r in range(n+1):
            out[2*r]+=q**(2*r)*sp(n)//(sp(r)*sp(n-r))
    out[n+1]+=q**n*sp(n)//gl(n)
    return dict(sorted(out.items()))


def direct(n,q):
    add,mul=field(q)
    d=2*n; z=d; N=d+1
    # standard symplectic structure with paired indices (0,1),(2,3),...
    J=[[0]*d for _ in range(d)]
    for i in range(n):J[2*i][2*i+1]=1;J[2*i+1][2*i]=neg(1,q)
    def bracket(x,y):
        return sum_field((mul(x[i],mul(J[i][j],y[j])) for i in range(d) for j in range(d)),add)
    eye=[[int(i==j) for j in range(d)] for i in range(d)]
    got=Counter(); candidates=0; tested=0
    for entries in product(range(q),repeat=d*d):
        T=[list(entries[i*d:(i+1)*d]) for i in range(d)]
        if matmul(T,T,q,add,mul)!=T:continue
        # Derivation constraints projected to V, independently checked on generators.
        possible_a=[]
        for a in (0,1):
            ok=True
            for i in range(d):
                for j in range(d):
                    val=sum_field((mul(T[k][i],J[k][j]) for k in range(d)),add)
                    val=add(val,sum_field((mul(J[i][k],T[k][j]) for k in range(d)),add))
                    if val!=mul(a,J[i][j]):ok=False;break
                if not ok:break
            if ok:possible_a.append(a)
        for a in possible_a:
            candidates+=1
            for fs in product(range(q),repeat=d):
                P=[[0]*N for _ in range(N)]
                for i in range(d):
                    for j in range(d):P[i][j]=T[i][j]
                    P[z][i]=fs[i]
                P[z][z]=a
                if matmul(P,P,q,add,mul)!=P:continue
                # Check original Leibniz identity on every ordered pair of basis vectors.
                valid=True
                for i in range(N):
                    for j in range(N):
                        # [e_i,e_j] is J[i,j]*z; central with the generator z.
                        lhs=mul((J[i][j] if i<d and j<d else 0),a)
                        rhs=bracket([P[h][i] for h in range(d)], [int(h==j) for h in range(d)])
                        rhs=add(rhs,bracket([int(h==i) for h in range(d)], [P[h][j] for h in range(d)]))
                        if lhs!=rhs:valid=False;break
                    if not valid:break
                if not valid:continue
                tested+=1
                got[rank(P,q,add,mul)]+=1
    return dict(sorted(got.items())),candidates,tested


def main():
    for n,q in [(1,2),(1,3),(1,4),(1,5),(2,2)]:
        # GF(5) is prime; at dimension 3 we enumerate 5^4 candidate T matrices.
        actual,candidates,tested=direct(n,q)
        expect=predicted(n,q)
        assert actual==expect,(n,q,actual,expect)
        print(f'n={n} q={q} ranks={actual} total={sum(actual.values())} T_a_pairs={candidates} PASS')
    print('HEISENBERG_IDEMPOTENT_DERIVATION_ORIGINAL_LEIBNIZ_AND_RANK_OK')

if __name__=='__main__':main()
