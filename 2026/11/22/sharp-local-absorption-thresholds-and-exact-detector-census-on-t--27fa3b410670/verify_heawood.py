"""Exact finite verification for coherent trapping on the Heawood incidence graph.

Requires only Python 3 standard library. Outputs the complete six-detector census.
An independent modular elimination cross-check has a rigorous determinant bound.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb, sqrt

N=7
LINES=tuple(frozenset((i+j)%N for j in (0,1,3)) for i in range(N))
B=tuple(tuple(int(i in LINES[j]) for j in range(N)) for i in range(N))
assert all(sum(B[i][k]*B[j][k] for k in range(N))==(3 if i==j else 1) for i in range(N) for j in range(N))
assert all(sum(B[i][j] for i in range(N))==3 for j in range(N))

# Columns: constant vector, seven point indicator vectors, seven line indicators.
C=[tuple([1]*N)]
C += [tuple(int(j==i) for j in range(N)) for i in range(N)]
C += [tuple(B[i][j] for i in range(N)) for j in range(N)]

def rank_fraction(cols):
    a=[[Fraction(col[i]) for col in cols] for i in range(N)]
    rows=N; nn=len(cols); p=0
    for j in range(nn):
        k=next((i for i in range(p,rows) if a[i][j]),None)
        if k is None: continue
        a[p],a[k]=a[k],a[p]
        z=a[p][j]; a[p]=[t/z for t in a[p]]
        for i in range(rows):
            if i!=p:
                z=a[i][j]
                if z: a[i]=[x-z*y for x,y in zip(a[i],a[p])]
        p+=1
        if p==rows:break
    return p

def rank_mod(cols,p=101):
    a=[[col[i]%p for col in cols] for i in range(N)]
    r=0
    for j in range(len(cols)):
        k=next((i for i in range(r,N) if a[i][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(r+1,N):
            factor=a[i][j]
            if factor: a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==N:break
    return r

counts=Counter(); badfive=[]
for S in combinations(range(14),6):
    cols=[C[0]]+[C[i+1] for i in S]
    r=rank_mod(cols)
    assert r==rank_fraction(cols),(S,r)
    k=sum(i<7 for i in S)
    counts[k,r]+=1
    if r==5: badfive.append(S)

expect={
  (0,7):7,
  (1,6):63,(1,7):84,
  (2,6):315,(2,7):420,
  (3,5):21,(3,6):336,(3,7):868,
  (4,6):315,(4,7):420,
  (5,6):63,(5,7):84,
  (6,7):7,
}
assert dict(counts)==expect,(counts,expect)
assert sum(counts.values())==comb(14,6)==3003
assert sum(v for (k,r),v in counts.items() if r==7)==1890
assert sum(v for (k,r),v in counts.items() if r==6)==1092
assert len(badfive)==21

# Each 10-dimensional bright-space configuration is precisely a Fano flag:
# a detected full line of points, and the three lines through one of these points.
def is_flag(S):
    ps=frozenset(x for x in S if x<7)
    ls=frozenset(x-7 for x in S if x>=7)
    if len(ps)!=3 or len(ls)!=3:return False
    return ps in LINES and any(ls==frozenset(j for j,L in enumerate(LINES) if p in L) for p in ps)
assert all(is_flag(s) for s in badfive)
assert sum(is_flag(s) for s in combinations(range(14),6))==21

# For any square minor of the 7x7 test matrix, Hadamard gives
# |det| <= sqrt(7)*sqrt(3)^6 < 72 < 101.
# So ranks over F_101 equal characteristic-zero ranks for these matrices.
assert sqrt(7)*3**3 < 101
print('HEAWOOD_EXACT_CENSUS_PASSED count=3003 full=1890 bright12=1092 bright10=21')
for k in range(7):
    print('points',k,'bright10',counts[k,5],'bright12',counts[k,6],'bright14',counts[k,7])

# The sharp universal threshold, checked independently of the six-set census.
for t,expected in [(7,{6:336,7:3096}),(8,{6:42,7:2961}),(9,{7:2002})]:
    c=Counter(rank_mod([C[0]]+[C[x+1] for x in S]) for S in combinations(range(14),t))
    assert dict(c)==expected,(t,c)
    print('detectors',t,'rank_histogram',sorted(c.items()))

# The 42 exceptional eight-detector sets are precisely the complements
# of 21 point-dipole supports and 21 line-dipole supports.
def dipole_support(a,b):
    assert a!=b
    s={a,b}
    s.update(7+j for j in range(7) if B[a][j]!=B[b][j])
    assert len(s)==6
    return frozenset(s)

def line_dipole_support(a,b):
    assert a!=b
    s={7+a,7+b}
    s.update(i for i in range(7) if B[i][a]!=B[i][b])
    assert len(s)==6
    return frozenset(s)

expected_bad8={frozenset(range(14))-dipole_support(a,b) for a,b in combinations(range(7),2)}
expected_bad8|={frozenset(range(14))-line_dipole_support(a,b) for a,b in combinations(range(7),2)}
actual_bad8={frozenset(S) for S in combinations(range(14),8) if rank_mod([C[0]]+[C[x+1] for x in S])<7}
assert len(expected_bad8)==42 and actual_bad8==expected_bad8
print('HEAWOOD_SHARP_UNIVERSAL_NINE_THRESHOLD_AND_42_DIPOLES_PASSED')
