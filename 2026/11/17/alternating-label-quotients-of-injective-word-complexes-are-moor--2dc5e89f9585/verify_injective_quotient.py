"""Independent finite checks of alternating-symmetry orbit CW chains for injective words."""
from itertools import permutations
from math import gcd
from functools import reduce
from sympy import ZZ, Matrix
from sympy.matrices.normalforms import smith_normal_form

def sign(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))) % 2 else 1

def key(word,n,alternating=True):
    k=len(word)
    if (not alternating) or n-k>=2:
        return 0
    rest=tuple(x for x in range(n) if x not in word)
    return sign(tuple(word)+rest)

def chain_data(n,alt=True):
    cells=[]; reps=[]; bdry=[]
    for k in range(1,n+1):
        words=list(permutations(range(n),k))
        keys=sorted(set(key(w,n,alt) for w in words))
        cells.append(keys)
        reps.append([next(w for w in words if key(w,n,alt)==a) for a in keys])
        if k>1:
            B=Matrix.zeros(len(cells[-2]),len(keys))
            for j,w in enumerate(reps[-1]):
                for i in range(len(w)):
                    kw=key(w[:i]+w[i+1:],n,alt)
                    B[cells[-2].index(kw),j]+=(-1)**i
            bdry.append(B)
    for i in range(1,len(bdry)):
        assert bdry[i-1]*bdry[i]==Matrix.zeros(bdry[i-1].rows,bdry[i].cols)
    return cells,bdry

for n in range(3,10):
    cells,B=chain_data(n)
    assert [len(c) for c in cells]==[1]*(n-2)+[2,2]
    for k,mat in enumerate(B,2):
        if k<=n-2:
            val=1 if (k-1)%2==0 else 0
            assert mat==Matrix([[val]])
    top=B[-1]; lower=B[-2]
    if n%2:
        a=(n+1)//2;b=(n-1)//2
        assert sorted(map(abs,list(top)))==sorted([a,a,b,b])
        assert abs(top.det())==n
        assert lower==Matrix.zeros(1,2) if n>=5 else lower==Matrix.zeros(1,2)
        diag=smith_normal_form(top,domain=ZZ)
        assert sorted(abs(diag[i,i]) for i in range(2))==[1,n]
    else:
        m=n//2
        assert sorted(map(abs,list(top)))==[m]*4
        assert top.rank()==1
        assert all(abs(v)==1 for v in list(lower))
        assert (top[0,0]*top[1,1]-top[0,1]*top[1,0])==0
        assert gcd(*list(top))==m
    S_cells,S_B=chain_data(n,False)
    assert all(len(c)==1 for c in S_cells)
    for k,b in enumerate(S_B,2):
        assert b[0,0] == (1 if (k-1)%2==0 else 0)
    print('n=',n,'alt_cell_counts=',[len(c) for c in cells], 'lower=',list(lower),'top=',list(top),'SNFdiag=',[abs(smith_normal_form(top,domain=ZZ)[i,i]) for i in range(2)])
print('INJECTIVE_WORD_ALT_QUOTIENT_ORBIT_CHAIN_PASS n=3..9')
