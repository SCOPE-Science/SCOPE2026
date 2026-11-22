#!/usr/bin/env python3
"""Exact independent verification of path-incidence metric enumerators.
No external datasets or dependencies are required.
"""
from collections import Counter

STATES=((0,0),(0,1),(1,0),(1,1))
INDEX={s:i for i,s in enumerate(STATES)}

def transfers(final=False):
    out={}
    for j,(a,b) in enumerate(STATES):
        choices_a=([None] if not a else ([1] if final else [1,2]))
        choices_b=([None] if not b else ([1] if final else [1,2]))
        for la in choices_a:
            for lb in choices_b:
                k=INDEX[(1 if la in (None,1) else 0,1 if lb in (None,1) else 0)]
                cost=(int(a)+int(b)-2*int(a and b and la==lb))
                out[(j,k,cost)]=out.get((j,k,cost),0)+1
    return out

def distribution(n):
    cur={(3,0):1}
    for t in range(n):
        nxt={}
        for (state,weight),m in cur.items():
            for (j,k,c),v in transfers(final=(t==n-1)).items():
                if j==state:
                    nxt[(k,weight+c)]=nxt.get((k,weight+c),0)+m*v
        cur=nxt
    return Counter({w:count for (k,w),count in cur.items() if k==3})

def path_sets(n):
    if n==0: return [frozenset()]
    ans=[]
    for length in (1,2):
        if length>n:continue
        for rest in path_sets(n-length):
            ans.append(frozenset({(0,length)}|{(i+length,j+length) for i,j in rest}))
    return ans

def run():
    F=[0,1]
    for j in range(2,16):F.append(F[-1]+F[-2])
    for n in range(1,13):
        paths=path_sets(n)
        direct=Counter(len(x.symmetric_difference(y)) for x in paths for y in paths)
        from_matrix=distribution(n)
        assert direct==from_matrix,(n,direct,from_matrix)
        assert sum(from_matrix.values())==len(paths)**2
        assert len(paths)==F[n+1]
    def shift(p,k=0,scale=1):
        return Counter({d+k:scale*a for d,a in p.items() if a})
    def add(*polys):
        out=Counter()
        for p in polys:
            for d,a in p.items():out[d]+=a
        return Counter({d:a for d,a in out.items() if a})
    h={n:distribution(n) for n in range(1,41)}
    assert h[1]==Counter({0:1})
    assert h[2]==Counter({0:2,3:2})
    assert h[3]==Counter({0:3,3:4,4:2})
    for n in range(4,41):
        expected=add(h[n-1],shift(h[n-1],1),h[n-2],shift(h[n-2],1,-1),
                     shift(h[n-2],3,2),shift(h[n-3],1,-1))
        assert h[n]==expected,(n,'rational generating function recurrence')
    print('ZIGZAG_FLOW_DISTANCE_EXACT_PASS n=1..12; RATIONAL_GF_PASS n<=40')
if __name__=='__main__':run()
