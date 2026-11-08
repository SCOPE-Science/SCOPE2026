"""Numerical independent checks of the minimal planar vertex-normal cone H-representation.
Requires numpy, scipy. This is a finite sanity check, not a proof of the all-N theorem.
"""
import numpy as np
from scipy.optimize import linprog

TOL=1e-7
count_cases=0
count_lp=0
count_kept=0
count_omitted=0

def verify(angles):
    global count_cases,count_lp,count_kept,count_omitted
    n=len(angles)
    angles=np.asarray(angles,dtype=float)
    assert n>=3 and np.all(np.diff(angles)>1e-8)
    gaps=np.diff(np.r_[angles,angles[0]+2*np.pi])
    directions=np.stack((np.cos(angles),np.sin(angles)),axis=1)
    large=np.where(gaps>=np.pi-1e-9)[0]
    # At most one gap of length pi or more, since every other gap is positive.
    assert len(large)<=1
    excluded=int(large[0]) if len(large) else -1
    pairs=[];rows=[]
    for i in range(n):
        for j in range(n):
            if j==i:continue
            r=np.zeros((n,2),dtype=float)
            r[i]=directions[i];r[j]=-directions[i]
            rows.append(r.flatten());pairs.append((i,j))
    rows=np.array(rows)
    kept=[]
    for pos,(i,j) in enumerate(pairs):
        if (j-i)%n not in (1,n-1):continue
        if excluded>=0 and {i,j}=={excluded,(excluded+1)%n}:continue
        kept.append(pos)
    assert len(kept)==(2*n if excluded<0 else 2*(n-1))
    for pos,pair in enumerate(pairs):
        # Omitted constraints must follow *simultaneously* from the reduced system.
        # Kept constraints must be irredundant even with all other kept ones.
        if pos in kept:
            other=[j for j in kept if j!=pos]
        else:
            other=kept
        res=linprog(rows[pos],A_ub=-rows[other],b_ub=np.zeros(len(other)),
                    bounds=[(-1,1)]*(2*n),method='highs')
        assert res.success,res.message
        if pos in kept:
            assert res.fun < -TOL,(angles.tolist(),pair,res.fun,'required')
            count_kept+=1
        else:
            assert res.fun >= -TOL,(angles.tolist(),pair,res.fun,'implied')
            count_omitted+=1
        count_lp+=1
    count_cases+=1

for n in range(3,13):
    verify(np.arange(n)*2*np.pi/n)
for values in ([0,30,70,110], [0,30,60,90,120,150], [0,45,90,135,180],
               [0,60,120,180], [0,20,45,90,140,180], [0,30,100,160,230,300],
               [0,89,91,180,269,271], [0,1,2,120,240]):
    verify(np.deg2rad(values))
rng=np.random.default_rng(20261107)
for n in range(3,11):
    for t in range(45):
        angles=np.sort(rng.uniform(0,2*np.pi,n))
        verify(angles)
print('PASS:',count_cases,'normal configurations;',count_lp,'independent bounded LPs;',
      count_kept,'nonredundancy witnesses;',count_omitted,'simultaneous implication checks')
