#!/usr/bin/env python3
"""Independent word census and signed-flow generating-series check (stdlib)."""
from itertools import product
from math import comb

def series_by_flow(max_m):
    # Enumerate imbalances as signed flows on the three edges of K3.
    flow=[0]*(max_m+1)
    for p in range(-max_m,max_m+1):
        for shift,weight in ((3*abs(p),1),(abs(p)+2*abs(p-1),6)):
            for k in range(shift,max_m+1,2):
                flow[k]+=weight*comb((k-shift)//2+2,2)
    flow[0]-=1   # all-zero off-diagonal contribution: disjoint loops treated separately
    def trio(t):return comb(t+2,2) if t>=0 else 0
    counts=[]
    for m in range(max_m+1):
        a=sum(flow[j]*trio(m-j) for j in range(m+1))
        a+=(1 if m==0 else 3) # zero off-diagonal edges, at most one active loop
        a-=sum((6*trio(m-2-2*j)+3*trio(m-3-2*j)) for j in range(m//2+1))
        counts.append(a)
    return counts

def main():
    counts=series_by_flow(18)
    for length in range(1,13):
        spectra=set()
        for word in product(range(3), repeat=length):
            m=[0]*9
            for a,b in zip(word,word[1:]):m[3*a+b]+=1
            spectra.add(tuple(m))
        assert len(spectra)==counts[length-1],(length,len(spectra),counts[length-1])
    print('DIRECT_WORD_ENUM_OK',counts[:12])
    assert counts[:12]==[1,9,24,65,156,342,683,1272,2226,3708,5919,9120]
    print('SIGNED_FLOW_SERIES_OK',counts)
if __name__=='__main__':main()
