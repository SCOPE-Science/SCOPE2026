"""Separate labeled-subset Bellman value iteration (floating point only)."""
from itertools import product
import numpy as np

def value_iteration(sizes=(1,2,6),max_iter=5000,tol=1e-13):
    N=sum(sizes); groups=[]
    for i,n in enumerate(sizes):groups.extend([i]*n)
    neighbors=[[j for j in range(N) if groups[j]!=groups[i]] for i in range(N)]
    states=range(1<<N); full=(1<<N)-1
    val=np.zeros((1<<N,N));
    for t in range(max_iter):
        new=np.zeros_like(val)
        for S in states:
            if S==full:continue
            for v in range(N):
                if not (S>>v)&1:continue
                arr=np.array([val[S|(1<<w),w] for w in neighbors[v]])
                # Each proposed neighbor uniformly and independently with replacement
                new[S,v]=1+np.minimum(arr[:,None],arr[None,:]).mean()
        diff=np.max(abs(new-val))
        val=new
        if diff<tol:
            return val,t+1,diff
    raise RuntimeError('No convergence')

if __name__=='__main__':
    val,t,diff=value_iteration()
    from choice_multipartite_exact import solve_sizes
    from fractions import Fraction as F
    bad,n,it,dp=solve_sizes((1,2,6))
    S=(1<<1)|(1<<2)|(1<<3)|(1<<4) # both size-two, and two of size-six visited
    assert S.bit_count()==4
    # Index 0 singleton unseen. Index 1 visited in size 2. Index 3 in large part currently.
    q_new=val[S|1,0]
    q_vis=val[S,1]
    print('Iterations',t,'delta',diff,'labeled observed values',q_new,q_vis,'gap',q_new-q_vis)
    w=next(x for x in bad if x['x']==(0,2,2))
    print('exact values',float(F(w['unvisited_value'])),float(F(w['visited_value'])),'gap',float(F(w['gap'])))
    assert abs(q_new-float(F(w['unvisited_value'])))<1e-9
    assert abs(q_vis-float(F(w['visited_value'])))<1e-9
    assert q_new>q_vis
    print('Independent labeled-state check PASS')
