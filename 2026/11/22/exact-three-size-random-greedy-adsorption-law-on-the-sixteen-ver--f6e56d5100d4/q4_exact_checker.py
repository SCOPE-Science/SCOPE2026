"""Independent exact finite certificates for greedy jamming on the four-cube."""
from fractions import Fraction
from collections import defaultdict,Counter
from functools import lru_cache
from itertools import permutations
from math import factorial

def cube(d):
    N=1<<d
    closed=[(1<<v)|sum(1<<(v^(1<<i)) for i in range(d)) for v in range(N)]
    full=(1<<N)-1
    # Independent full-mask enumeration, independent of the probabilistic recursion.
    families=defaultdict(list)
    for mask in range(1,1<<N):
        if any((mask&closed[v]).bit_count()>1 for v in range(N) if mask>>v&1):continue
        if any((mask&closed[v])==0 for v in range(N)):continue
        families[mask.bit_count()].append(mask)
    @lru_cache(None)
    def distrib(s):
        if not s:return (Fraction(1),)
        ans=[Fraction(0)]*(N+1)
        for v in range(N):
            if s>>v&1:
                for k,p in enumerate(distrib(s&~closed[v])):
                    if p:ans[k+1]+=p/s.bit_count()
        return tuple(ans)
    result=distrib(full)
    assert sum(result)==1
    # Separate direct target-probability recursion, tracks individual selected masks.
    @lru_cache(None)
    def target(s,t):
        if not s:return Fraction(int(t==0))
        if t==0:return Fraction(0)
        return sum((target(s&~closed[v],t^(1<<v)) for v in range(N) if s>>v&1 and t>>v&1),Fraction())/s.bit_count()
    point_probs={m:target(full,m) for group in families.values() for m in group}
    assert sum(point_probs.values())==1
    assert {k:sum((point_probs[m] for m in group),Fraction()) for k,group in families.items()} == {i:p for i,p in enumerate(result) if p}
    print('Q',d,'MIS', {k:len(g) for k,g in families.items()},'p',[(i,str(p)) for i,p in enumerate(result) if p], 'states',distrib.cache_info().currsize, 'point_states',target.cache_info().currsize)
    return families,point_probs

for d in (1,2,3,4):
    families,prob=cube(d)
    if d==1:assert {k:len(v) for k,v in families.items()}=={1:2}
    if d==2:assert {k:len(v) for k,v in families.items()}=={2:2}
    if d==3:assert {k:len(v) for k,v in families.items()}=={2:4,4:2}
    if d==4:
        assert {k:len(v) for k,v in families.items()}=={4:24,5:16,8:2}
        assert {k:sum((prob[m] for m in g),Fraction()) for k,g in families.items()} == {4:Fraction(1,6),5:Fraction(64,165),8:Fraction(49,110)}
        expected={4:Fraction(1,144),5:Fraction(4,165),8:Fraction(49,220)}
        for k,group in families.items():
            for mask in group:assert prob[mask]==expected[k]
        # An automorphism is a coordinate permutation followed by a bitwise translation.
        auto=[]
        for prm in permutations(range(4)):
            for t in range(16):
                auto.append([sum(((v>>i)&1)<<prm[i] for i in range(4))^t for v in range(16)])
        assert len(auto)==384
        for k,group in families.items():
            orbit={sum(1<<per[v] for v in range(16) if group[0]>>v&1) for per in auto}
            assert orbit==set(group),(k,len(orbit),len(group))
        # Full exact first-order stochastic dominance versus uniform among all MIS.
        total=sum(map(len,families.values()))
        p=Fraction(0);q=Fraction(0)
        for k in sorted(families):
            p+=sum((prob[m] for m in families[k]),Fraction())
            q+=Fraction(len(families[k]),total)
            assert p<=q
            if k<8:assert p<q
        assert total==42
        assert Fraction(49,110)>Fraction(2,42)
        print('PASS: Q4 complete orbit/pointwise-jamming law and stochastic dominance')
