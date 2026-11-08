"""Independent finite first-appearance edge-pattern certificate (Python >=3.9)."""
from collections import Counter
from math import comb, factorial

EXPECTED = {
 (4,1):48, (4,2):24,
 (5,1):432, (5,2):240,
 (6,1):504, (6,2):408, (6,3):24,
 (7,1):112, (7,2):264, (7,3):64,
 (8,2):48, (8,3):28, (9,3):4,
}
BINOMIAL_COEFFICIENTS = {4:720, 5:33120, 6:257040,
                         7:655200, 8:624960, 9:181440}

def small_covers(edges, t):
    """Vertex covers of size one or two, vertices confined to used labels."""
    ans=[]
    for x in range(t):
        if all(x in e for e in edges):ans.append((x,))
    for x in range(t):
        for y in range(x+1,t):
            if all(x in e or y in e for e in edges):ans.append((x,y))
    return ans

hist=Counter()
visited=Counter()

def generate(edges, t, pair_births):
    k=len(edges)
    visited[k]+=1
    cv=small_covers(edges,t)
    if k==6:
        # The complete sequence must dominate all two-subsets.
        assert not cv
        hist[(t,pair_births)]+=1
        return
    if k and not cv:
        return
    if not k:
        generate(((0,1),),2,1)
        return
    choices=[(x,y) for x in range(t) for y in range(x+1,t)]
    choices += [(x,t) for x in range(t)]
    choices.append((t,t+1))
    for edge in choices:
        if edge in edges:continue
        if not any(not set(c).intersection(edge) for c in cv):continue
        new_t=max(t,edge[1]+1)
        generate(edges+(edge,),new_t,pair_births+int(new_t==t+2))

generate((),0,0)
assert dict(hist)==EXPECTED, (dict(hist),EXPECTED)
assert visited == {0:1,1:1,2:3,3:19,4:146,5:886,6:2200}, visited
for t in range(4,10):
    value=sum(factorial(t) * v // (2**q) if factorial(t)*v % (2**q)==0
              else None for (u,q),v in hist.items() if u==t)
    assert value==BINOMIAL_COEFFICIENTS[t],(t,value)
assert max(t for t,q in hist)==9
print('PASS canonical complete patterns:', sum(hist.values()))
print('visited levels:', sorted(visited.items()))
print('histogram (support size, pair births, patterns):',sorted((t,q,c) for (t,q),c in hist.items()))
print('binomial coefficients:',sorted(BINOMIAL_COEFFICIENTS.items()))
print('largest support size: 9')
