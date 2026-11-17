"""Finite exact proof certificate for two coupled eight-bit majority maps.
All loops are over explicitly bounded finite domains. Python 3 standard library only.
"""
from collections import Counter
from itertools import combinations

N = 8
MASK = 255

def bit(s, j):
    return (s >> (j % N)) & 1

def maj(a, b, c):
    return (a & b) | (a & c) | (b & c)

def f(s):  # even shore B -> odd shore A
    return sum(maj(bit(s, j-2),bit(s,j),bit(s,j+1)) << j for j in range(N))

def g(s):  # odd shore A -> even shore B
    return sum(maj(bit(s, j-1),bit(s,j),bit(s,j+2)) << j for j in range(N))

fa = [f(s) for s in range(256)]
gb = [g(s) for s in range(256)]
h = [fa[gb[s]] for s in range(256)]
k = [gb[fa[s]] for s in range(256)]
h2 = [h[h[s]] for s in range(256)]
k2 = [k[k[s]] for s in range(256)]

# F^3 is periodic: F^5=F^3, universally for all 2^16 inputs.
assert all(fa[k2[s]] == fa[k[s]] for s in range(256))
assert all(gb[h2[s]] == gb[h[s]] for s in range(256))
assert all(h[h2[s]] == h2[s] and k[k2[s]] == k2[s] for s in range(256))

SA = {s for s in range(256) if h[s]==s}
SB = {s for s in range(256) if k[s]==s}
assert len(SA)==len(SB)==72
assert {gb[s] for s in SA}==SB
assert all(fa[gb[s]]==s for s in SA)

# Complete 256-element fibers of the finite retractions h^2 and k^2.
weightsA = Counter(h2)
weightsB = Counter(k2)
assert set(weightsA)==SA and set(weightsB)==SB
assert all(weightsB[gb[s]]==weightsA[s] for s in SA)
assert Counter((s.bit_count(),weightsA[s]) for s in SA)=={
    (0,69):1,(3,2):24,(4,1):22,(5,2):24,(8,69):1
}

# A compact cyclic-necklace witness table for all 72 distinct stable eight-words.
def rotate(s,r):
    r %= 8
    return ((s << r) | (s >> (8-r))) & MASK if r else s
reps = {}
for s in SA:
    rep = min(rotate(s,r) for r in range(8))
    reps.setdefault(rep,set()).add(s)
expected = {(0,1,69),(7,8,2),(13,8,2),(37,8,2),
            (15,8,1),(45,8,1),(51,4,1),(85,2,1),
            (31,8,2),(47,8,2),(91,8,2),(255,1,69)}
assert {(rep,len(orbit),weightsA[rep]) for rep,orbit in reps.items()}==expected
assert all(orbit=={rotate(rep,r) for r in range(8)} for rep,orbit in reps.items())

# The condition that F^t(x) is recurrent factors over two shores.
c0 = len(SA)
c1A = sum(gb[s] in SB for s in range(256))
c1B = sum(fa[s] in SA for s in range(256))
c2A = sum(h[s] in SA for s in range(256))
c2B = sum(k[s] in SB for s in range(256))
assert (c0,c1A,c1B,c2A,c2B)==(72,144,144,208,208)
entry = [72**2,144**2-72**2,208**2-144**2,256**2-208**2]
assert entry == [5184,15552,22528,22272]

# Identifying a state (s,g(t)) with (s,t), F swaps the symbols.
# Each basin is the union of one or two preimages under F^4.
fixed_basins = Counter(weightsA[s]**2 for s in SA)
two_basins = Counter(2*weightsA[s]*weightsA[t] for s,t in combinations(sorted(SA),2))
assert fixed_basins=={1:22,4:48,4761:2}
assert two_basins=={2:231,4:1056,8:1128,138:44,276:96,9522:1}
assert sum(b*n for b,n in fixed_basins.items())==9736
assert sum(b*n for b,n in two_basins.items())==55800
assert len(SA)+2*sum(two_basins.values())==5184
assert sum(entry)==65536

print('CERTIFICATE_OK')
print('graph=Moebius-Kantor_GP8_3 8+8 shore vertices')
print('local_maps=f(B),g(A), h=f(g),k=g(f)')
print('h_first_image,h_second_image',len(set(h)),len(set(h2)))
print('stable_symbols',len(SA),'necklace_representatives',len(reps))
for rep in sorted(reps, key=lambda s:(s.bit_count(),s)):
    print('NECKLACE',format(rep,'08b')[::-1],len(reps[rep]),weightsA[rep])
print('entry_counts_0_1_2_3',*entry)
print('fixed_points',len(SA),'two_cycles',sum(two_basins.values()))
print('fixed_basins',sorted(fixed_basins.items()))
print('two_cycle_basins',sorted(two_basins.items()))
print('eventual_fixed_states',sum(b*n for b,n in fixed_basins.items()))
print('eventual_two_cycle_states',sum(b*n for b,n in two_basins.items()))
print('exact F^5=F^3 YES')
