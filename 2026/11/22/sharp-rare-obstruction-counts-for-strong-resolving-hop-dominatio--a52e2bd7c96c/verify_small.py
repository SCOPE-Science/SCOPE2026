"""Independent exact enumeration for strong-resolving hop bases on small cubes.
No third-party dependencies. Run: python verify_small.py
"""
from itertools import combinations
from collections import Counter

def masks_for_bases(d):
    v=1<<d; full=v-1
    pairs=[(x,x^full) for x in range(v) if x < (x^full)]
    for code in range(1<<len(pairs)):
        mask=0
        for i,(a,b) in enumerate(pairs):
            mask |= 1<<(b if code>>i &1 else a)
        yield mask

def strong_resolves(d,S):
    v=1<<d
    for a in range(v):
        for b in range(a+1,v):
            ab=(a^b).bit_count()
            if not any((a^w).bit_count()==ab+(b^w).bit_count() or
                       (b^w).bit_count()==ab+(a^w).bit_count() for w in S):
                return False
    return True

def hop_dominates(d,S):
    verts=range(1<<d)
    return all(v in S or any((u^v).bit_count()==2 for u in S) for v in verts)

def enumerate_full(d):
    count=0; count_strong=0
    for mask in masks_for_bases(d):
        S=[u for u in range(1<<d) if mask>>u&1]
        assert strong_resolves(d,S)
        count_strong+=1
        count+=hop_dominates(d,S)
    return count_strong,count

for d,expected in [(2,4),(3,14),(4,256)]:
    total,good=enumerate_full(d)
    assert good==expected, (d,total,good)
    print(f'd={d}: all {total} antipodal bases strongly resolve; {good} hop-dominate')

# A separately implemented bit-vector census at d=5 (not using masks_for_bases).
d=5; allmask=(1<<(1<<d))-1; ant=(1<<d)-1
pairs=[x for x in range(1<<d) if x< (x^ant)]
needs=[sum(1<<(v^(1<<i)^(1<<j)) for i,j in combinations(range(d),2))
       for v in range(1<<d)]
counts=Counter()
for bits in range(1<<len(pairs)):
    omitted=0
    for i,r in enumerate(pairs):
        omitted |= 1<<(r if bits & (1<<i) else r^ant)
    bad=sum(bool((omitted>>v)&1) and (omitted & needs[v])==needs[v]
            for v in range(1<<d))
    counts[bad]+=1
assert counts=={0:64830,1:512,2:160,5:32,16:2},counts
print('d=5: bad-center histogram',sorted(counts.items()))

# d=6: because antipodes retain parity, the two halves split independently.
d=6; full=(1<<d)-1
side=[u for u in range(1<<d) if u.bit_count()%2==0]
rep=[u for u in side if u < (u^full)]
needed={u:{u^(1<<i)^(1<<j) for i,j in combinations(range(d),2)} for u in side}
counts=Counter()
for bits in range(1<<len(rep)):
    outside={r if bits>>i&1 else (r^full) for i,r in enumerate(rep)}
    bad=sum(all(w in outside for w in needed[u]) for u in outside)
    counts[bad]+=1
assert counts=={0:65504,1:32},counts
print('d=6: one-parity histogram',sorted(counts.items()))
print('d=6: full good-basis count',counts[0]**2)
assert counts[0]**2==4290774016
