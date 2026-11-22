#!/usr/bin/env python3
"""Independent complete word-enumeration certificate for two 3-state DFA products.
All 729 binary transition tables are represented in base three, with state order 0,1,2.
No external dependencies.
"""
from collections import Counter
from itertools import product, permutations

def table(i):
    return [[(i // 3**(3*c+s)) % 3 for s in range(3)] for c in range(2)]

# masks[i][length] is bitset of the words synchronizing automaton i,
# ordered lexicographically by 0=a,1=b, length in 1..6.
masks = [[0]*7 for _ in range(729)]
for i in range(729):
    d = table(i)
    for length in range(1, 7):
        bits=0
        for wcode in range(1 << length):
            word = [(wcode >> (length-1-j)) & 1 for j in range(length)]
            images=[]
            for s in range(3):
                for c in word:
                    s=d[c][s]
                images.append(s)
            if images[0]==images[1]==images[2]:
                bits |= 1 << wcode
        masks[i][length]=bits

# Every 3-state DFA has a synchronizing word iff one of the words
# of length <=6 resets it: this is independently checked below by
# brute force reachability of every nonempty subset.
def reachability_has_singleton(d):
    seen = {7}
    frontier = [7]
    while frontier:
        x = frontier.pop()
        if x in (1,2,4):
            return True
        for c in range(2):
            nxt=0
            for s in range(3):
                if (x >> s) & 1:
                    nxt |= 1 << d[c][s]
            if nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return False

individual=[]
for i in range(729):
    r = next((length for length in range(1,7) if masks[i][length]), -1)
    assert (r!=-1) == reachability_has_singleton(table(i)), i
    individual.append(r)
counts=Counter(); cross=Counter(); extremals=[]
for i in range(729):
    if individual[i]<0: continue
    for j in range(729):
        if individual[j]<0: continue
        r=next((length for length in range(1,7)
                if masks[i][length] & masks[j][length]), -1)
        assert r>=1, (i,j)
        counts[r]+=1
        cross[(individual[i],individual[j],r)]+=1
        if r==6: extremals.append((i,j))
assert sum(counts.values()) == 549**2
assert counts==Counter({1:13041,2:154008,3:87552,4:37872,5:7488,6:1440})
assert Counter(individual)==Counter({-1:180,1:153,2:324,3:48,4:24})

# Canonicalize the extremal pairs under independent state renamings,
# simultaneous letter interchange, and factor interchange.
perms=list(permutations(range(3)))
def renamed(i,perm,swap):
    tr=table(i); out=[[0]*3 for _ in range(2)]
    for c in range(2):
        for s in range(3):
            out[c][perm[s]]=perm[tr[c^swap][s]]
    return sum(out[c][s]*3**(3*c+s) for c in range(2) for s in range(3))
variants=[[tuple(renamed(i,p,sw) for p in perms) for sw in range(2)]
          for i in range(729)]
def canonical(i,j):
    return min((min(a,b),max(a,b)) for sw in range(2)
               for a in variants[i][sw] for b in variants[j][sw])
classes=Counter(canonical(i,j) for i,j in extremals)
assert len(classes)==11
assert Counter(classes.values()) == Counter({144:9, 72:2})

print('single_histogram', sorted(Counter(individual).items()))
print('product_reset_histogram', sorted(counts.items()))
print('pair_count', sum(counts.values()))
print('length6_count',len(extremals),'orbits',len(classes))
print('orbit_size_distribution',sorted(Counter(classes.values()).items()))
print('slow_pair_conditional', sorted((i,j,k,v) for (i,j,k),v in cross.items() if k==6))
print('example_tables',table(32),table(38))
print('example_reset_word', 'baabab')
print('example_noshorter', all((masks[32][l] & masks[38][l])==0 for l in range(1,6)))
print('example_reset',bool(masks[32][6] & masks[38][6] & (1<<int('100101',2))))
