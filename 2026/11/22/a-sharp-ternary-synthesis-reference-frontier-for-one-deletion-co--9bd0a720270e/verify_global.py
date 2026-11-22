"""Exact ternary three-letter deletion-code and reference enumeration.
Run: python verify_global.py
"""
from itertools import product, combinations
from collections import Counter

Q=range(3)
words=tuple(product(Q, repeat=3))
shadows=[{x[:i]+x[i+1:] for i in range(3)} for x in words]
independent={i:[] for i in range(1,6)}
# Incrementally construct all codes; note that each subsequent index is larger.
independent[1]=[(i,) for i in range(27)]
for k in range(2,6):
    for c in independent[k-1]:
        for j in range(c[-1]+1,27):
            if all(shadows[j].isdisjoint(shadows[i]) for i in c):
                independent[k].append(c+(j,))
assert len(independent[5]) == 3
assert not any(all(shadows[i].isdisjoint(shadows[j]) for i in c)
               for c in independent[5] for j in range(c[-1]+1,27))
print('global: number_of_maximal_five_word_codebooks',len(independent[5]))

def is_subsequence(x,s):
    pos=0
    for v in s:
        if pos<len(x) and x[pos]==v:
            pos+=1
    return pos==len(x)

def compute(s):
    support=set(i for i,w in enumerate(words) if is_subsequence(w,s))
    for k in (5,4,3,2,1):
        matches=[c for c in independent[k] if all(i in support for i in c)]
        if matches:
            return k,len(matches)
    return 0,0

for t in range(3,10):
    hist=Counter()
    best=[]
    for s in product(Q,repeat=t):
        k,co=compute(s)
        hist[k]+=1
        if t==6 and k==4:
            best.append((''.join(map(str,s)),co))
    cyc=tuple(i%3 for i in range(t))
    print('length',t,'histogram',sorted(hist.items()),'cyclic_best',compute(cyc)[0])
    if t==6:
        assert len(best)==12 and {x[1] for x in best}=={1}
        originals={x[0] for x in best}
        seed=(0,1,2,0,2,1)
        orbit=set()
        for p in product(Q,repeat=3):
            if len(set(p))==3:
                s=tuple(p[v] for v in seed)
                orbit.add(''.join(map(str,s)))
                orbit.add(''.join(map(str,reversed(s))))
        assert originals == orbit
        print('six_cycle_optimizers',sorted(originals))
assert compute((0,1,2,0,2,1))[0]==4
print('RESULT: exact enumeration and symmetry assertions PASS')
