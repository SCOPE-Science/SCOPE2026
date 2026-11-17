#!/usr/bin/env python3
"""Finite checks for clique complexes of half-cube graphs after deleting one edge."""
from collections import defaultdict
from itertools import combinations
from math import comb

def vertices(n): return [x for x in range(1<<n) if x.bit_count()%2==0]
def hdist(a,b):return (a^b).bit_count()
def faces(n, deleted=False):
    verts=vertices(n)
    adj={x:{y for y in verts if y!=x and hdist(x,y)==2 and (not deleted or frozenset((x,y))!=frozenset((0,3)))} for x in verts}
    result=defaultdict(list)
    def grow(clq, candidates):
        for idx,x in enumerate(candidates):
            t=clq+(x,)
            result[len(t)-1].append(t)
            grow(t,[y for y in candidates[idx+1:] if y in adj[x]])
    grow((),verts)
    return dict(result)
def rank_mod2(cols):
    pivots={}
    for v in cols:
        while v:
            pivot=v.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=v;break
            v ^= pivots[pivot]
    return len(pivots)
def betti(f):
    counts=[len(f.get(i,[])) for i in range(max(f)+1)]
    ranks=[0]*(len(counts)+1)
    for k in range(1,len(counts)):
        sub={s:j for j,s in enumerate(f[k-1])}
        cols=[]
        for s in f[k]:
            v=0
            for q in range(len(s)):
                v ^= 1<<sub[s[:q]+s[q+1:]]
            cols.append(v)
        ranks[k]=rank_mod2(cols)
    return [counts[i]-ranks[i]-ranks[i+1] for i in range(len(counts))],counts,ranks

def bn(n):return sum((-1)**(i-4)*2**(n-i)*comb(n,i) for i in range(4,n+1))

def main():
    for n in range(4,7):
        f=faces(n,False)
        b,counts,r=betti(f)
        d=faces(n,True)
        bd,dc,rd=betti(d)
        want=bn(n)-(n-3)
        print('n',n,'full counts',counts,'Betti',b,'deleted counts',dc,'deleted Betti',bd,'expected',want,flush=True)
        assert b==[1,0,0,bn(n)]+[0]*(len(b)-4)
        assert bd==[1,0,0,want]+[0]*(len(bd)-4)
        link=[x for x in vertices(n) if hdist(x,0)==2 and hdist(x,3)==2]
        a=[(1<<0)|(1<<j) for j in range(2,n)]
        c=[(1<<1)|(1<<j) for j in range(2,n)]
        assert set(link)==set(a+c)
        assert all(hdist(a[i],a[j])==2 for i in range(n-2) for j in range(i+1,n-2))
        assert all(hdist(c[i],c[j])==2 for i in range(n-2) for j in range(i+1,n-2))
        assert all((hdist(a[i],c[j])==2)==(i==j) for i in range(n-2) for j in range(n-2))
    print('HALFCUBE_SINGLE_EDGE_HOMOTOPY_CHECK_PASS')
if __name__=='__main__':main()
