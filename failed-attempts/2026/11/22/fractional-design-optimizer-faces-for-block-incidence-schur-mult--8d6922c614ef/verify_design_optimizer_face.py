"""Finite exact checks for the fractional-design optimizer-face theorem.

Uses only the Python standard library. These computations supplement an infinite
family argument and do not replace the analytic proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, sqrt

checks = 0

def check(ok, message):
    global checks
    assert ok, message
    checks += 1

def matrix_rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    n, m = len(a), len(a[0]) if a else 0
    i = 0
    pivots = []
    for j in range(m):
        t = next((q for q in range(i, n) if a[q][j]), None)
        if t is None:
            continue
        a[i], a[t] = a[t], a[i]
        c = a[i][j]
        a[i] = [z/c for z in a[i]]
        for q in range(n):
            if q != i and a[q][j]:
                c = a[q][j]
                a[q] = [x-c*y for x,y in zip(a[q],a[i])]
        pivots.append(j)
        i += 1
        if i==n:
            break
    return i,pivots,a

def run(v,k):
    blocks = list(combinations(range(v),k))
    b = len(blocks)
    pairs = list(combinations(range(v),2))
    A = [[int(i in S and j in S) for S in blocks] for i,j in pairs]
    rank,piv,R = matrix_rank(A)
    expected = comb(v,2) if k <= v-2 else v
    check(rank==expected,(v,k,'rank',rank,expected))
    check(sum(row[0] for row in A) == comb(k,2),(v,k,'column pair total'))
    target = Fraction(comb(v-2,k-2),b)
    for row in A:
        check(Fraction(sum(row),b)==target,(v,k,'uniform pair'))
    # All k-subsets have identical fixed-size columns; two-design Gram is uniform.
    reps=comb(v-1,k-1)
    lam=comb(v-2,k-2)
    for i in range(v):
        for j in range(v):
            tally=sum((i in S and j in S) for S in blocks)
            check(tally == (reps if i==j else lam),(v,k,i,j))
    # A kernel direction can be used to construct a continuum of exact optimizer weights.
    if b>rank:
        f=next(j for j in range(b) if j not in piv)
        c=[Fraction(0) for _ in range(b)]
        c[f]=1
        for i,j in enumerate(piv):
            c[j]=-R[i][f]
        for row in A:
            check(sum(x*y for x,y in zip(row,c))==0,(v,k,'kernel'))
        check(sum(c)==0,(v,k,'normalization'))
        z=[Fraction(1,b)+Fraction(1,100*b)*ci for ci in c]
        if min(z)<=0:
            z=[Fraction(1,b)+ci/(b*(1+sum(abs(x) for x in c))) for ci in c]
        check(min(z)>0,(v,k,'positivity'))
        check(sum(z)==1,(v,k,'probability'))
        for row in A:
            check(sum(w*x for w,x in zip(row,z))==target,(v,k,'fractional design'))
    # Known Schur norm attained at uniform weights, as an external comparison.
    val=(k+sqrt((v-1)*k*(v-k)))/v
    check(val>1,(v,k,'noncontractive'))
    check(val<=(1+sqrt(v))/2+1e-12,(v,k,'sharp envelope'))
    return b,rank,b-rank

for v,k in [(4,2),(4,3),(5,2),(5,3),(5,4),(6,2),(6,3),(6,4),(6,5),(7,2),(7,3),(7,4),(7,5),(7,6),(8,3),(8,4),(9,3),(9,4)]:
    b,r,d=run(v,k)
    print(f'v={v} k={k} blocks={b} pair-incidence-rank={r} optimizer-face-dim={d}')
print(f'DESIGN_OPTIMIZER_FACE_CHECK_OK {checks}')
