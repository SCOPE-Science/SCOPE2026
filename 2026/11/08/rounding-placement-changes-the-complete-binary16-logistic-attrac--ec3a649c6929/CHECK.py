#!/usr/bin/env python3
"""Exact finite-state certificate for two binary16 logistic-map evaluation semantics.
Uses only integer arithmetic and the Python standard library; no floating-point
operations occur in the construction of either transition graph.
"""
from bisect import bisect_left
from collections import Counter
from hashlib import sha256
from struct import pack

Q=1<<24
LAST=0x3c00
N=LAST+1

def half_scaled(bits):
    assert 0 <= bits <= LAST
    e=(bits>>10)&31
    f=bits&1023
    return f if e==0 else (1024+f) << (e-1)

GRID=[half_scaled(i) for i in range(N)]
assert GRID[0]==0 and GRID[-1]==Q and all(GRID[i]<GRID[i+1] for i in range(N-1))

def nearest_index(num,den=1):
    """Round rational num/(den*2**24) to nearest binary16 in [0,1], ties to even."""
    assert 0<=num<=Q*den + Q*den//2048
    if num>=Q*den:return LAST
    j=bisect_left(GRID,num//den)
    # Find first grid point >= num/den exactly (floor-based bisect may undershoot).
    while j<N and GRID[j]*den < num:
        j+=1
    if j==0:return 0
    if j==N:return N-1
    low=j-1
    lo_gap=num-GRID[low]*den
    hi_gap=GRID[j]*den-num
    if lo_gap<hi_gap:return low
    if lo_gap>hi_gap:return j
    return low if low%2==0 else j

def maps():
    staged=[];single=[];reassociated=[]
    for x in GRID:
        u=GRID[nearest_index(Q-x)]  # fl16(1 - x), exact integer source
        staged.append(nearest_index(4*x*u,Q)) # fl16( (4*x) * fl16(1-x) )
        single.append(nearest_index(4*x*(Q-x),Q)) # fl16(4*x*(1-x)), one rounding
        product=GRID[nearest_index(x*u,Q)] # fl16(x*fl16(1-x))
        reassociated.append(nearest_index(4*product))
    assert staged==reassociated  # power-of-two scaling commutes with rounding here
    return staged,single

def census(succ):
    state=bytearray(N)
    cycle_of=[-1]*N;pre=[-1]*N
    cycles=[]
    for root in range(N):
        if state[root]:continue
        path=[];index={};t=root
        while not state[t] and t not in index:
            index[t]=len(path);path.append(t);t=succ[t]
        if t in index:
            core=path[index[t]:]
            label=len(cycles);cycles.append(core)
            for v in core:cycle_of[v]=label;pre[v]=0
        for v in reversed(path):
            if cycle_of[v]==-1:
                cycle_of[v]=cycle_of[succ[v]]
                pre[v]=1+pre[succ[v]]
            state[v]=1
    assert all(state) and all(p>=0 for p in pre)
    assert all(succ[v]>=0 and succ[v]<N for v in range(N))
    stats=[]
    for c,cyc in enumerate(cycles):
        lengths=[pre[k] for k in range(N) if cycle_of[k]==c]
        stats.append((len(cyc),len(lengths),max(lengths),min(cyc)))
    return sorted(stats),max(pre),max(pre[v]+len(cycles[cycle_of[v]]) for v in range(N)),cycles,cycle_of,pre

def digest(succ):
    return sha256(b''.join(pack('<H',v) for v in succ)).hexdigest()

def main():
    staged,single=maps()
    assert len(staged)==len(single)==N
    print('DOMAIN',N,'float16 states [0,1], signed zero identified')
    for tag,seq in [('staged',staged),('single_round',single)]:
        stats,mx,mr,cy,co,pre=census(seq)
        print(tag,'cycle tuple (period, basin, maximum preperiod, smallest cycle-bit-pattern)',stats)
        print(tag,'max_preperiod',mx,'max_first_repeat',mr,'sha256_le_uint16',digest(seq))
        print(tag,'distinct cycle periods',sorted(Counter(len(c) for c in cy).items()))
    print('different one-step transitions',sum(a!=b for a,b in zip(staged,single)))
    assert sorted(census(staged)[0])==[(1,2,1,0x3a00),(1,5092,55,0),(40,10267,83,7678)]
    assert sorted(census(single)[0])==[(1,8,7,0x3a00),(1,15236,109,0),(5,117,14,11709)]
    assert sum(a!=b for a,b in zip(staged,single))==2774
    print('VERIFY_OK exact_integer_full_graphs=2 states_each=15361 edge_comparisons=15361')

if __name__=='__main__':main()
