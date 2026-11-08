#!/usr/bin/env python3
"""Independent five-vertex motif enumeration explaining the first kinetic discrepancy."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from functools import lru_cache


def graph_edges(k):
    E=set()
    for i in range(10):
        for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+k)%10)):
            E.add(tuple(sorted((a,b))))
    assert len(E)==30
    return E

def profiles(k):
    E=graph_edges(k); out=Counter(); rep={}; expectations={}
    for verts in combinations(range(20),5):
        ed=[(a,b) for a,b in combinations(verts,2) if (a,b) in E]
        deg={v:0 for v in verts}
        for a,b in ed: deg[a]+=1;deg[b]+=1
        key=(len(ed),tuple(sorted(deg.values())))
        out[key]+=1
        rep[key]=(verts,ed)
        weight=expected_occupied(verts,ed)
        if key in expectations:
            assert expectations[key]==weight, (key, expectations[key], weight)
        else:
            expectations[key]=weight
    assert sum(out.values())==15504
    return out,rep

def expected_occupied(five,edges):
    v_idx={v:i for i,v in enumerate(five)}
    closed=[1<<i for i in range(5)]
    for a,b in edges:
        i,j=v_idx[a],v_idx[b]
        closed[i]|=(1<<j);closed[j]|=(1<<i)
    @lru_cache(None)
    def F(S):
        if not S: return Fraction(0)
        return 1+sum((F(S&~closed[i]) for i in range(5) if S&(1<<i)),Fraction(0))/S.bit_count()
    return F(31)

def main():
    A, RA=profiles(2); B, RB=profiles(3)
    expected={
      (0,(0,0,0,0,0)):12,
      (1,(0,0,0,1,1)):-60,
      (2,(0,0,1,1,2)):60,
      (2,(0,1,1,1,1)):60,
      (3,(0,1,1,2,2)):-60,
      (3,(1,1,1,1,2)):-60,
      (4,(1,1,2,2,2)):60,
      (5,(2,2,2,2,2)):-12
    }
    actual={key:B[key]-A[key] for key in (A.keys()|B.keys()) if B[key]!=A[key]}
    assert actual==expected, (actual,expected)
    total=Fraction(0)
    for sig,diff in sorted(actual.items()):
        five,edges=RA[sig] if sig in RA else RB[sig];w=expected_occupied(five,edges)
        total+=diff*w
        print('edges=%d degrees=%s Desargues_minus_dodeca=%d RSA_expectation=%s'%
              (sig[0],sig[1],diff,w))
    assert total==4
    print('PASS: complete 5-subset motif census; difference of summed RSA means = 4')

if __name__=='__main__':main()
