"""Vectorized cross-check of synchronous open-neighborhood NOR on GP(10,k)."""
import numpy as np
import sys,collections

def neighbor_masks(k):
    adj=[set() for _ in range(20)]
    def e(a,b): adj[a].add(b);adj[b].add(a)
    for i in range(10):
        e(i,(i+1)%10)
        e(i,i+10)
        e(i+10,(i+k)%10+10)
    assert all(len(s)==3 for s in adj)
    assert sum(map(len,adj))==60
    return np.array([sum(1<<j for j in s) for s in adj],dtype=np.uint32)

def main(k):
    adj=neighbor_masks(k)
    total=1<<20
    xs=np.arange(total,dtype=np.uint32)
    def update(a):
        out=np.zeros_like(a)
        for i,m in enumerate(adj):out |= (((a & m)==0).astype(np.uint32)<<i)
        return out
    fx=update(xs)
    ffx=update(fx)
    fffx=update(ffx)
    assert np.array_equal(fffx,fx)
    fixed=np.flatnonzero(fx==xs)
    rec=np.flatnonzero(ffx==xs)
    cycs=(len(rec)-len(fixed))//2
    periodic_targets=fx
    kind=(ffx==fx) # since y=F(x), F(y)=ffx, equality tests y fixed
    fixed_basin=np.count_nonzero(kind)
    assert np.count_nonzero(ffx==fx)==fixed_basin
    assert len(fixed)+2*cycs==len(rec)
    # Independent formulation of fixed point set via maximal independent sets:
    is_fix_by_sets=np.ones(total,dtype=bool)
    for i,m in enumerate(adj):
        occupied=(xs & (1<<i))!=0
        no_occupied_neighbor=(xs&m)==0
        is_fix_by_sets &= (occupied==no_occupied_neighbor)
    assert np.array_equal(np.flatnonzero(is_fix_by_sets),fixed)
    # Basin of all-zero/all-one two-cycle: x=0 OR x a total dominating set.
    is_totdom=np.ones(total,dtype=bool)
    for m in adj:is_totdom &= ((xs&m)!=0)
    dominant_size=np.count_nonzero(is_totdom)+1
    assert fx[0]==total-1 and fx[total-1]==0
    # invariant orbit representative min(y,F(y)), basin sizes through bincount.
    reps=np.minimum(fx,ffx)
    sizes=np.bincount(reps,minlength=total)
    nonzero=sizes[sizes!=0]
    basins_of_fixed=sizes[fixed]
    periodic_nonfixed=np.flatnonzero((ffx==xs)&(fx!=xs)&(xs<fx))
    bs_2=sizes[periodic_nonfixed]
    assert len(nonzero)==len(fixed)+len(periodic_nonfixed)
    assert sizes[0]==dominant_size
    print('k',k,'total',total,'fixed',len(fixed),'two_cycles',cycs,'fixed_basin',fixed_basin,'two_basin',total-fixed_basin,'dominant',dominant_size)
    print('fixed_basin_spectrum',dict(sorted(collections.Counter(map(int,basins_of_fixed)).items())))
    print('2cycle_basin_spectrum',dict(sorted(collections.Counter(map(int,bs_2)).items())))
    print('fixed_basin_total_from_sums',int(basins_of_fixed.sum()),'period2_basin_total_from_sums',int(bs_2.sum()))
    assert sum(basins_of_fixed)+sum(bs_2)==total
if __name__=='__main__':
    for k in (2,3):main(k)
