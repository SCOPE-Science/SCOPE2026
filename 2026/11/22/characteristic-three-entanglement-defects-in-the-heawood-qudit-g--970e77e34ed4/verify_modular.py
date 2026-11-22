"""Independent finite-field verification using F_2^3 projective incidence.
Only Python standard library. Run: python verify_modular.py
"""
from collections import Counter
from itertools import combinations

V = list(range(1,8))
def parity(x): return x.bit_count() & 1
# Every nonzero vector v is a distinct projective point over F_2;
# every nonzero linear form a determines a distinct line a.v = 0.
N = [[int(parity(a & v)==0) for a in V] for v in V]
assert all(sum(row)==3 for row in N)
assert all(sum(row[j] for row in N)==3 for j in range(7))
assert all(sum(N[i][j]*N[k][j] for j in range(7))==1
           for i in range(7) for k in range(i+1,7))


def field_rank(A, p):
    if not A: return 0
    M=[[int(z)%p for z in row] for row in A]
    rows,cols=len(M),len(M[0]);r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if M[i][j]),None)
        if pivot is None: continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][j], -1, p)
        M[r]=[(v*inv)%p for v in M[r]]
        for i in range(rows):
            if i!=r and M[i][j]:
                c=M[i][j];M[i]=[(M[i][k]-c*M[r][k])%p for k in range(cols)]
        r+=1
        if r==rows: break
    return r

hist={p:Counter() for p in (2,3,5,101)}
defects=set()
for S in combinations(range(14),7):
    if 0 not in S: continue
    s=set(S)
    X=[i for i in range(7) if i in s]
    Y=[j for j in range(7) if j+7 not in s]
    XC=[i for i in range(7) if i not in s]
    YC=[j for j in range(7) if j+7 in s]
    assert len(X)==len(Y) and len(XC)==len(YC)
    M1=[[N[i][j] for j in Y] for i in X]
    M2=[[N[i][j] for j in YC] for i in XC]
    # Empty blocks have rank zero.
    ranks={p:field_rank(M1,p)+field_rank(M2,p) for p in hist}
    for p in hist: hist[p][ranks[p]]+=1
    if ranks[3]<ranks[101]: defects.add(frozenset(S))

expected={2:{4:50,5:490,6:840,7:336},
          3:{4:21,5:273,6:729,7:693},
          5:{4:21,5:273,6:700,7:722},
          101:{4:21,5:273,6:700,7:722}}
for p in hist: assert dict(hist[p])==expected[p],(p,hist[p])

# Identify characteristic-three exceptional cuts without Smith reduction:
# each noncollinear point triangle selects its complement and its three side lines.
lines=[frozenset(i for i in range(7) if N[i][j]) for j in range(7)]
triangles=set()
for T in combinations(range(7),3):
    t=set(T)
    if any(t <= L for L in lines):continue
    side={j+7 for j,L in enumerate(lines) if len(t & L)==2}
    assert len(side)==3
    S=frozenset((set(range(7))-t) | side)
    if 0 not in S:S=frozenset(set(range(14))-S)
    triangles.add(S)
assert len(triangles)==28
assert defects == triangles | {frozenset(range(7))}
print('PASS: second incidence model, split-block rank algorithm, 1716 cuts')
print('Field-rank histograms:',{p:dict(sorted(hist[p].items())) for p in hist})
print('Exceptional geometric description:',len(defects),'= 28 triangles + 1 point-line cut')
