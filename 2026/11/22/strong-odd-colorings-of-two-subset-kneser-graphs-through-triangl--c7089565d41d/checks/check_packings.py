"""MILP triangle-packings and direct neighborhood-parity verification."""
import itertools, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def expected(n):
    E=n*(n-1)//2
    residue=n%6
    leave={0:n//2,1:0,2:n//2,3:0,4:n//2+1,5:4}[residue]
    return (E-leave)//3,leave

def pack(n):
    ed=list(itertools.combinations(range(n),2)); em={e:i for i,e in enumerate(ed)}
    tri=list(itertools.combinations(range(n),3))
    A=np.zeros((len(ed),len(tri)))
    for j,t in enumerate(tri):
        for a,b in itertools.combinations(t,2):A[em[a,b],j]=1
    ans=milp(c=-np.ones(len(tri)),integrality=np.ones(len(tri)),bounds=Bounds(0,1),constraints=LinearConstraint(A,0,1),options={'time_limit':20,'mip_rel_gap':0})
    if ans.x is None or ans.status!=0: raise RuntimeError(f'MILP not certified for n={n}: {ans.message}')
    chosen=[tri[j] for j,x in enumerate(ans.x) if x>0.5]
    taken={tuple(e) for t in chosen for e in itertools.combinations(t,2)}
    rest=[e for e in ed if e not in taken]
    assert len(chosen)==expected(n)[0]
    assert len(rest)==expected(n)[1]
    return chosen,rest

def check(n,classes):
    edges=list(itertools.combinations(range(n),2)); sets=[set(e) for e in edges];used=[]
    for c in classes:
        used.extend(c)
    assert len(set(used))==len(edges) and set(used)==set(edges)
    for color in classes:
        for i in range(len(color)):
            for j in range(i+1,len(color)):
                assert set(color[i])&set(color[j])
        for a,b in edges:
            count=sum(not (set(e)&{a,b}) for e in color)
            assert count==0 or count%2==1,(n,color,(a,b),count)

for n in range(5,11):
    tris,rest=pack(n)
    nostar=[[tuple(e) for e in itertools.combinations(t,2)] for t in tris]+[[e] for e in rest]
    check(n,nostar)
    E=n*(n-1)//2
    best_nonstar=E-2*len(tris)
    if n%2==0:
        ts,rs=pack(n-1)
        stars=[tuple(sorted((n-1,i))) for i in range(n-1)]
        starclasses=[stars]+[[tuple(e) for e in itertools.combinations(t,2)] for t in ts]+[[e] for e in rs]
        check(n,starclasses)
        starlen=len(starclasses)
    else:starlen=None
    best=min(best_nonstar,starlen if starlen is not None else best_nonstar)
    print(f'n={n} tmax={len(tris)} leave={len(rest)} no_star={best_nonstar} with_star={starlen} best={best} verified')
