"""Reproduce exact finite probability law and maximal-matching comparison for C20.
Standard-library Python 3.10+; run `python verify_dodeca.py`."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache

EDGES = tuple(sorted(tuple(sorted(e)) for i in range(10) for e in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10))))
N=20; FULL=(1<<N)-1
ADJ=[0]*N
for a,b in EDGES:
    ADJ[a]|=1<<b; ADJ[b]|=1<<a
assert len(EDGES)==30 and all(x.bit_count()==3 for x in ADJ)

@lru_cache(None)
def avail(mask):
    return tuple((j,mask & ~(1<<a) & ~(1<<b)) for j,(a,b) in enumerate(EDGES) if mask>>a&1 and mask>>b&1)

# Independent method I: dynamic program on remaining free vertex sets.
@lru_cache(None)
def remaining_law(mask):
    options=avail(mask)
    if not options: return (Q(1),)
    out=Counter()
    for _, nxt in options:
        for k,p in enumerate(remaining_law(nxt)):
            out[k+1]+=p/len(options)
    return tuple(out.get(k,Q(0)) for k in range(max(out)+1))

# Independent method II: enumerate all undirected matchings, filter maximal,
# and sum exact probabilities of all possible orders of chosen edges.
@lru_cache(None)
def prefix_probability(matching):
    if not matching:return Q(1)
    total=Q(0)
    all_mask=0
    for i in matching:
        a,b=EDGES[i]; all_mask|=(1<<a)|(1<<b)
    for i in matching:
        a,b=EDGES[i]
        before=all_mask & ~((1<<a)|(1<<b))
        prior=tuple(j for j in matching if j!=i)
        total+=prefix_probability(prior)/len(avail(FULL & ~before))
    return total

def maximal_matchings():
    # Every vertex either unmatched or paired with a larger unassigned neighbor.
    def walk(unassigned, singletons, picked):
        if not unassigned:
            if all(not (ADJ[v]&singletons) for v in range(N) if singletons>>v&1):
                yield tuple(sorted(picked))
            return
        u=(unassigned&-unassigned).bit_length()-1
        bit=1<<u
        yield from walk(unassigned & ~bit, singletons|bit, picked)
        for j,(a,b) in enumerate(EDGES):
            if a==u and unassigned>>b&1:
                yield from walk(unassigned & ~bit & ~(1<<b), singletons, picked+(j,))
            elif b==u and unassigned>>a&1:
                yield from walk(unassigned & ~bit & ~(1<<a), singletons, picked+(j,))
    yield from walk(FULL,0,())

def main():
    raw=remaining_law(FULL)
    law={i:p for i,p in enumerate(raw) if p}
    counts=Counter(); prob=Counter()
    ms=list(maximal_matchings())
    assert len(ms)==len(set(ms))
    for m in ms:
        counts[len(m)]+=1
        prob[len(m)]+=prefix_probability(m)
    assert dict(prob)==law, (prob,law)
    assert sum(counts.values())==3781
    assert counts==Counter({6:5,7:420,8:2280,9:1040,10:36})
    expected={
     6:Q(1,3125),
     7:Q(91294494167,2756754000000),
     8:Q(1796566904214749,4862914056000000),
     9:Q(2544405065946811,4862914056000000),
     10:Q(123231298227,1667666000000)}
    assert law==expected
    assert sum(prob.values())==1
    denom=sum(counts.values())
    for k in (6,7,8,9):
        assert sum(law[i] for i in law if i<=k) < Q(sum(counts[i] for i in counts if i<=k),denom)
    print('PASS: graph 20 vertices 30 edges, 3-regular')
    print('PASS: independent exact output-size recurrences agree')
    print('PASS: 3781 distinct maximal matchings')
    print('PASS: strict stochastic dominance at all four nontrivial thresholds')
    print('DP states',remaining_law.cache_info().currsize)
    print('matching prefixes',prefix_probability.cache_info().currsize)
    for k in sorted(law):
        print('size',k,'maximal_matchings',counts[k],'greedy_probability',law[k],
              'uniform_probability',Q(counts[k],denom))
    print('greedy E',sum(i*p for i,p in law.items()))
    print('uniform E',Q(sum(i*c for i,c in counts.items()),denom))
    print('perfect bias ratio',law[10]/Q(counts[10],denom))

if __name__=='__main__': main()
