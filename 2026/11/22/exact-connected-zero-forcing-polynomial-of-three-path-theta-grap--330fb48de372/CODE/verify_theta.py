"""Independent exhaustive verification of the three-arm theta connected-forcing enumerator.
Pure Python standard library; run: python CODE/verify_theta.py
All assertions are exact integer checks. Finite checks corroborate the general proof.
"""
from itertools import combinations_with_replacement

def graph(lengths):
    assert len(lengths) == 3 and all(x >= 2 for x in lengths)
    n = 2 + sum(x-1 for x in lengths)
    adj = [0]*n
    p = 2
    for length in lengths:
        path = [0] + list(range(p, p+length-1)) + [1]
        p += length-1
        for u,v in zip(path,path[1:]):
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj

def connected(s, adj):
    if not s: return False
    discovered = s & -s
    frontier = discovered
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        nbr = adj[bit.bit_length()-1] & s & ~discovered
        discovered |= nbr
        frontier |= nbr
    return discovered == s

def forces(s, adj):
    target = (1 << len(adj)) - 1
    while s != target:
        newly = 0
        for v,nbr in enumerate(adj):
            if s & (1 << v):
                missing = nbr & ~s
                if missing and missing & (missing-1) == 0:
                    newly |= missing
        if not newly: return False
        s |= newly
    return True

def census(lengths):
    adj = graph(lengths)
    out = [0]*(len(adj)+1)
    for mask in range(1,1<<len(adj)):
        if connected(mask,adj) and forces(mask,adj):
            out[mask.bit_count()] += 1
    return out

def add(a,b):
    out = [0]*max(len(a),len(b))
    for i,v in enumerate(a): out[i] += v
    for i,v in enumerate(b): out[i] += v
    return out

def neg(a): return [-v for v in a]
def mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out

def product(items):
    out = [1]
    for item in items: out = mul(out,item)
    return out

def formula(lengths):
    r = [a-1 for a in lengths]
    prefixes = [[0]+[1]*k for k in r]
    unions = [[0]+list(range(2,k+1))+[1] if k > 1 else [0,1] for k in r]
    full = [[0]*k+[1] for k in r]
    half = [add(unions[i],neg(full[i])) for i in range(3)]
    one_terminal = product([add([1],x) for x in prefixes])
    one_terminal = add(one_terminal,[-1])
    for x in prefixes: one_terminal = add(one_terminal,neg(x))
    one_terminal = [0]+[2*x for x in one_terminal]
    def full_among(indices):
        return add(product([unions[i] for i in indices]),
                   neg(product([half[i] for i in indices])))
    both = full_among(range(3))
    for omitted in range(3):
        both = add(both,full_among([i for i in range(3) if i!=omitted]))
    out = add(one_terminal,[0,0]+both)
    return out[:2+sum(r)+1]

def verify():
    cases = 0
    raw_states = 0
    repeated_arm_cases = 0
    for lengths in combinations_with_replacement(range(2,9),3):
        if sum(lengths) > 18: continue
        exact = census(lengths)
        proposed = formula(lengths)
        assert exact == proposed, (lengths, exact, proposed)
        assert exact[:3] == [0,0,0] and exact[3] == 6, (lengths,exact)
        assert exact[-1] == 1
        if len(set(lengths)) < 3: repeated_arm_cases += 1
        cases += 1
        raw_states += (1 << len(graph(lengths)))
    print('EXHAUSTIVE_CHECKED_THETA_INSTANCES',cases)
    print('REPEATED_ARM_INSTANCES',repeated_arm_cases)
    print('TOTAL_VERTEX_SUBSETS_INSPECTED',raw_states)
    for lengths in [(2,2,2),(2,2,3),(2,3,4),(3,4,5),(4,4,4)]:
        print('CASE',lengths,'COEFFICIENTS',formula(lengths))
    print('VERIFY_OK')

if __name__ == '__main__': verify()
