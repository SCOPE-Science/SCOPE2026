"""Reproduce finite-field nullity counts for bordered-diagonal symmetric ensembles.
No external dependencies; supports prime fields and the four-element field.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, prod


def arith(q):
    if q == 4:
        def add(a,b): return a ^ b
        def mul(a,b):
            r=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):r^=1<<(i+j)
            if r&8:r^=0b1110 # X^3=X^2+X
            if r&4:r^=0b111 # X^2=X+1
            return r
        return add,mul
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q


def rank(A,q,add,mul):
    A=[row[:] for row in A]
    n=len(A);r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if A[i][j]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=next(t for t in range(1,q) if mul(A[r][j],t)==1)
        for x in range(j,n):A[r][x]=mul(A[r][x],inv)
        for i in range(r+1,n):
            v=A[i][j]
            if v:
                # subtraction equals addition in characteristic two
                neg = v if q in (2,4) else (-v)%q
                for x in range(j,n):A[i][x]=add(A[i][x],mul(neg,A[r][x]))
        r+=1
    return r


def qbinom(n,k,q):
    if k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k)) if k else 1


def full_sym_count(d,q):
    # Known classical count; verified independently by enumeration below.
    # Rational-exact alternate computation below avoids intermediate rounding.
    v=Fraction(q**(d*(d+1)//2))
    for i in range(1,d+1,2):v*=Fraction(q**i-1,q**i)
    assert v.denominator==1
    return int(v)


def sym_ranks(d,q):
    return [qbinom(d,r,q)*full_sym_count(r,q) for r in range(d+1)]


def rectangular_ranks(k,s,q):
    ans=[]
    for t in range(min(k,s)+1):
        v=Fraction(1)
        for i in range(t):
            v*=Fraction((q**k-q**i)*(q**s-q**i),q**t-q**i)
        assert v.denominator==1
        ans.append(int(v))
    return ans


def predicted(k,m,q):
    out=Counter()
    for s in range(m+1):
        # Number of leaf diagonals with exactly s zeros; all other
        # m-s leaf couplings are arbitrary and do not affect rank.
        factor=comb(m,s)*(q-1)**(m-s)*q**(k*(m-s))
        for t,ct in enumerate(rectangular_ranks(k,s,q)):
            d=k-t
            for r,cr in enumerate(sym_ranks(d,q)):
                nullity=(s-t)+(d-r)
                out[nullity]+=factor*ct*cr*q**(k*(k+1)//2-d*(d+1)//2)
    assert sum(out.values())==q**(k*(k+1)//2 + k*m + m)
    return out


def enumerated(k,m,q):
    add,mul=arith(q)
    cells=[(i,j) for i in range(k) for j in range(i,k)]
    cells += [(i,k+j) for i in range(k) for j in range(m)]
    cells += [(k+j,k+j) for j in range(m)]
    result=Counter();n=k+m
    for vals in product(range(q),repeat=len(cells)):
        A=[[0]*n for _ in range(n)]
        for (i,j),v in zip(cells,vals):A[i][j]=A[j][i]=v
        result[n-rank(A,q,add,mul)]+=1
    return result


def main():
    cases=[(q,k,m) for q,k,m in [
        (2,1,1),(2,1,3),(2,2,2),(2,3,1),
        (3,1,2),(3,2,1),(3,2,2),
        (4,1,2),(4,2,1),(5,1,2),(5,2,1)]]
    for q,k,m in cases:
        observed=enumerated(k,m,q)
        expected=predicted(k,m,q)
        assert observed==expected, (q,k,m,observed,expected)
        print('PASS q=%s hubs=%s leaves=%s total=%s nullities=%s'%(q,k,m,sum(observed.values()),sorted(observed.items())))
    for q in (2,3,4,5):
        add,mul=arith(q)
        for d in (0,1,2,3):
            if q**(d*(d+1)//2)>60000:continue
            cells=[(i,j) for i in range(d) for j in range(i,d)]
            nfull=0
            for vals in product(range(q),repeat=len(cells)):
                A=[[0]*d for _ in range(d)]
                for (i,j),v in zip(cells,vals):A[i][j]=A[j][i]=v
                nfull+=(rank(A,q,add,mul)==d)
            assert nfull==full_sym_count(d,q),(q,d,nfull,full_sym_count(d,q))
            print('PASS symmetric q=%s dimension=%s invertible=%s'%(q,d,nfull))
    print('ALL CHECKS PASSED')

if __name__=='__main__':main()
