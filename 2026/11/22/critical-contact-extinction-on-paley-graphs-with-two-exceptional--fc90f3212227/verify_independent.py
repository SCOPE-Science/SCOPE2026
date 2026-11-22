#!/usr/bin/env python3
"""Independent exhaustive orbit tracing with lexicographic tuples and phase reconstruction."""
from collections import Counter
from itertools import product,permutations

def neighbors(q):
    if q==5:
        edges={(i,(i+1)%5) for i in range(5)}
    else:
        edges={(3*a+b,3*a+c) for a in range(3) for b in range(3) for c in range(b+1,3)}
        edges.update((3*a+b,3*c+b) for b in range(3) for a in range(3) for c in range(a+1,3))
    return [set(v for u,v in edges if u==i)|set(u for u,v in edges if v==i) for i in range(q)]

def run(q):
    E=neighbors(q);theta=(q-1)//4
    def step(x):
        result=list(x)
        for i in range(q):
            if x[i]:result[i]=(x[i]+1)%3
            else:result[i]=1 if sum(x[j]==1 for j in E[i])>=theta else 0
        return tuple(result)
    basin=Counter();depths=Counter();recur=set();cycles={}
    for x in product(range(3),repeat=q):
        seen={};path=[];z=x
        while z not in seen:
            seen[z]=len(path);path.append(z);z=step(z)
        t=seen[z];p=len(path)-t
        rep=min(path[t:]);basin[(rep,p)]+=1;depths[(t,p)]+=1
        for y in path[t:]:recur.add(y)
        cycles[(rep,p)]=1
    table=Counter(p for _,p in cycles)
    assert table==({1:1,5:2} if q==5 else {1:1,3:4})
    assert sum(basin.values())==3**q
    print('q',q,'cycles',dict(table),'basin_sizes',sorted(basin.values()),
          'depth_period', sorted((a,b,n) for (a,b),n in depths.items()),
          'periodic_states',len(recur))
    if q==9:
        latin={tuple((r*3+c)%3 for r in range(3) for c in range(3))}
        # enumerate all symbol relabelings, row/col shifts and permutations of rows
        latin=set()
        for p in permutations((0,1,2)):
            for s in permutations((0,1,2)):
                for t in permutations((0,1,2)):
                    x=tuple(p[(s[r]+t[c])%3] for r in range(3) for c in range(3))
                    if all(len({x[3*r+c] for c in range(3)})==3 for r in range(3)) and all(len({x[3*r+c] for r in range(3)})==3 for c in range(3)):
                        latin.add(x)
        assert len(latin)==12
        assert recur==latin | {tuple([0]*9)}
        print('latin_squares',len(latin),'periodic_nonzero',len(recur)-1)
    else:
        assert len(recur)==11
    return basin,depths

if __name__=='__main__':
    run(5);run(9)
    print('INDEPENDENT_OK')
