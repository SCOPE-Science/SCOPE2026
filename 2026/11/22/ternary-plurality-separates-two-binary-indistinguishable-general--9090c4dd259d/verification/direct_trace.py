"""Independent tuple-trajectory verifier of the finite three-colour plurality claims.
Python >=3.9; standard library only.
"""
from collections import Counter, defaultdict
from itertools import product

def graph(step):
    A = [set() for _ in range(10)]
    for i in range(5):
        for j in ((i+1)%5, i+5):
            A[i].add(j); A[j].add(i)
        a,b=5+i,5+(i+step)%5
        A[a].add(b); A[b].add(a)
    assert all(len(v)==3 for v in A)
    return tuple(tuple(sorted(v)) for v in A)

def evolve(x, N):
    y=[]
    for i,nbrs in enumerate(N):
        counts=Counter(x[j] for j in nbrs)
        leaders=[a for a,v in counts.items() if v==max(counts.values())]
        y.append(leaders[0] if len(leaders)==1 else x[i])
    return tuple(y)

def check(step):
    N=graph(step)
    states=tuple(product(range(3), repeat=10))
    F={x:evolve(x,N) for x in states}
    assert len(F)==59049
    outcome={};cycles={};first_depth=Counter();first_period=Counter();basins=Counter()
    for x in states:
        seq=[];position={};u=x
        while u not in position and u not in outcome:
            position[u]=len(seq);seq.append(u);u=F[u]
        if u in outcome:
            cyc,base=outcome[u]
            depth=len(seq)+base
            for j,v in enumerate(seq):outcome[v]=(cyc,len(seq)-j+base)
        else:
            start=position[u];cyc=tuple(seq[start:]);p=len(cyc)
            canonical=min(cyc)
            if canonical not in cycles:cycles[canonical]=cyc
            for j,v in enumerate(seq):outcome[v]=(canonical,max(0,start-j))
    for x in states:
        cyc,dep=outcome[x];per=len(cycles[cyc]);first_depth[(dep,per)]+=1;first_period[per]+=1;basins[cyc]+=1
    orbit=Counter(map(len,cycles.values()))
    consensus=[c for c in cycles if len(set(c))==1 and len(cycles[c])==1]
    hist_fixed=Counter(basins[c] for c in cycles if len(cycles[c])==1)
    hist_two=Counter(basins[c] for c in cycles if len(cycles[c])==2)
    print(f'GP(5,{step}): orbit={dict(orbit)} basin={dict(first_period)} max_depth={max(d for d,p in first_depth)} consensus_basin={sum(basins[c] for c in consensus)}')
    print('entry=',sorted(first_depth.items()),'fixed_basin_hist=',sorted(hist_fixed.items()),'two_basin_hist=',sorted(hist_two.items()))
    return dict(orbit),dict(first_period),max(d for d,p in first_depth)

if __name__=='__main__':
    assert check(1)==({1:219,2:1410},{1:17049,2:42000},5)
    assert check(2)==({1:579,2:2175},{1:37899,2:21150},7)
    print('INDEPENDENT_DIRECT_TRAJECTORY_CHECK_PASSED')
    for step in (1,2):
        N=graph(step)
        B=tuple(product((0,1),repeat=10))
        def majority2(x):
            return tuple(int(sum(x[j] for j in N[i])>=2) for i in range(10))
        binary_fixed=sum(majority2(x)==x for x in B)
        binary_two=sum(majority2(x)!=x and majority2(majority2(x))==x for x in B)//2
        assert (binary_fixed,binary_two)==(14,55)
        print(f'GP(5,{step}) binary fixed={binary_fixed} primitive_two_cycles={binary_two}')
    print('BINARY_BASELINE_CHECK_PASSED')
