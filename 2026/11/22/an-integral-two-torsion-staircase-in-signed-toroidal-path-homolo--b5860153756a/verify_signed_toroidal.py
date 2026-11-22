"""Standalone integer checks for path-chain orientation and toroidal signed local systems."""
from itertools import combinations
from math import comb
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def signed_cycle_incidence(m):
    # Anti-invariant basis v_i-v_(i+m), e_i-e_(i+m), for a 2m-cycle
    out=Matrix.zeros(m,m)
    for i in range(m):
        out[i,i]-=1
        if i<m-1:out[i+1,i]+=1
        else:out[0,i]-=1
    return out

def tensor_model(r):
    # k-cells indexed by subsets of {0,...,r-1}; only first direction twisted.
    bases=[[s for s in combinations(range(r),k)] for k in range(r+1)]
    mats=[]
    for k in range(1,r+1):
        d=Matrix.zeros(len(bases[k-1]),len(bases[k]))
        for j,s in enumerate(bases[k]):
            if 0 in s:
                s2=tuple(x for x in s if x!=0)
                d[bases[k-1].index(s2),j]=-2
        mats.append(d)
    return bases,mats

def snf_rank_torsion(m):
    d=smith_normal_form(m,domain=ZZ)
    v=[abs(int(d[i,i])) for i in range(min(d.rows,d.cols)) if d[i,i]]
    return len(v),[x for x in v if x!=1]

for m in (5,6,8):
    d=signed_cycle_incidence(m)
    rank,tor=snf_rank_torsion(d)
    assert rank==m and tor==[2],(m,rank,tor)
    print('twisted cycle m=',m,'invariant first-boundary SNF:',[1]*(m-1)+[2])

for r in range(2,7):
    b,ds=tensor_model(r)
    for k in range(r):
        dprev=ds[k-1] if k>=1 else Matrix.zeros(0,len(b[k]))
        dnext=ds[k] if k<r else Matrix.zeros(len(b[k]),0)
        if 1<=k<=r-1:assert dprev*dnext==Matrix.zeros(dprev.rows,dnext.cols)
        # Due to sparse tensor model, homology in degree k is Z/2 for each
        # subset of {1,...,r-1} of cardinality k.
        assert sum(0 not in s for s in b[k])==comb(r-1,k)
        assert sum(0 in s for s in b[k+1])==comb(r-1,k) if k<r else True
        if k<r:
            rank,tors=snf_rank_torsion(dnext)
            assert rank==comb(r-1,k) and tors==[2]*rank
    print('r=',r,'predicted H_q torsion ranks=',[comb(r-1,q) for q in range(r)],'all integer boundaries checked')
print('PASS')

# Independently derive Omega_p for a bidirected cycle by eliminating forbidden faces.
def omega_dim_mod2(circ,p):
    paths=[(i,) for i in range(circ)]
    for _ in range(p):
        paths=[z+(j,) for z in paths for j in ((z[-1]-1)%circ,(z[-1]+1)%circ)]
    # each forbidden (p-1)-path gives a row with a bit for each allowable p-path
    rows={}
    for j,path in enumerate(paths):
        for i in range(1,p):
            reduced=path[:i]+path[i+1:]
            if reduced[i-1]==reduced[i]: continue # nonregular, vanishes
            if (reduced[i]-reduced[i-1])%circ not in (1,circ-1):
                rows[reduced]=rows.get(reduced,0)^(1<<j)
    pivots={}
    for row in rows.values():
        while row:
            bit=row.bit_length()-1
            if bit in pivots:row^=pivots[bit]
            else:
                pivots[bit]=row;break
    return len(paths)-len(pivots)

for circumference in (10,12):
    for p in range(2,7):
        actual=omega_dim_mod2(circumference,p)
        assert actual==2*circumference,(circumference,p,actual)
        print('C',circumference,'p',p,'exact mod-2 Omega dimension',actual)
print('DIRECT_PATH_CHECK_PASS')
