"""Exact reproducibility checks for the three-agent directed-trust construction."""
from fractions import Fraction as Q
from itertools import permutations

W=((Q(2,3),Q(1,3),Q(0)),
   (Q(0),Q(2,3),Q(1,3)),
   (Q(1,3),Q(0),Q(2,3)))
x0=(Q(0), Q(1,4), Q(3,4))

def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def apply(a,v):
    return tuple(sum(a[i][j]*v[j] for j in range(3)) for i in range(3))

def diffs(v):
    return tuple(v[i]-v[j] for i,j in ((0,1),(0,2),(1,2)))

def mat_power(a,n):
    out=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
    for _ in range(n):out=mul(a,out)
    return out

P=tuple(tuple(Q(1,3) for j in range(3)) for i in range(3))
Id=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
assert mat_power(W,6)==tuple(tuple(P[i][j]-(Id[i][j]-P[i][j])/27 for j in range(3)) for i in range(3))
assert mat_power(W,12)==tuple(tuple(P[i][j]+(Id[i][j]-P[i][j])/729 for j in range(3)) for i in range(3))
x=x0; vals=[]
for t in range(12):
    vals.extend(abs(v) for v in diffs(x))
    x=apply(W,x)
assert min(vals)==Q(1,2916)

# Exact endogenous-confidence iterations for multiple positive reverse thresholds.
for m in range(4):
    delta=Q(1,5832*729**m)
    x=x0
    n_forward=12*m+12
    sign0=tuple(v>0 for v in diffs(x))
    sign_changes=0
    for t in range(n_forward):
        # Never assume the directed cycle: test the actual gates at every step.
        assert all(abs(d)>delta for d in diffs(x)), (m,t,x)
        xnext=[]
        for i in range(3):
            next_idx=(i+1)%3
            opposite=(i+2)%3
            trusted=[j for j in (next_idx,opposite) if abs(x[j]-x[i]) < (Q(1) if j==next_idx else delta)]
            assert trusted==[next_idx], (m,t,i,trusted)
            xnext.append(x[i]+sum((x[j]-x[i])/3 for j in trusted))
        x=tuple(xnext)
        assert x==apply(mat_power(W,t+1),x0)
        if (t+1)%6==0:
            assert tuple(v>0 for v in diffs(x))==tuple(not b for b in sign0)
            sign_changes+=1
            sign0=tuple(v>0 for v in diffs(x))
    assert sign_changes==2*m+2
    assert all(v!=0 for v in diffs(x))
    # Thereafter direct two-threshold dynamics reaches exact consensus.
    reach=False
    for t in range(500):
        if x[0]==x[1]==x[2]:
            reach=True; break
        x=tuple(x[i]+sum((x[j]-x[i])/3 for j in range(3) if j!=i and abs(x[j]-x[i])<(Q(1) if j==(i+1)%3 else delta)) for i in range(3))
    assert reach,(m,'finite convergence failed')
    print('m=',m,'delta=',delta,'full consensus at t=',n_forward+t)

# Every 2-step transition has 3x3 positive entries >=1/9 (all possible gate patterns).
def step_matrix(mask):
    out=[]
    for i in range(3):
        r=[Q(0)]*3
        r[i]+=Q(2,3)
        r[(i+1)%3]+=Q(1,3)
        if (mask>>i)&1:
            r[i]-=Q(1,3)
            r[(i+2)%3]+=Q(1,3)
        out.append(tuple(r))
    return tuple(out)
for mask1 in range(8):
    for mask2 in range(8):
        mat=mul(step_matrix(mask2),step_matrix(mask1))
        assert all(v>=Q(1,9) for row in mat for v in row)
print('PASS: two exact matrix identities, 12 phase gaps, 4 full gated trajectories, 64 scrambling products.')
