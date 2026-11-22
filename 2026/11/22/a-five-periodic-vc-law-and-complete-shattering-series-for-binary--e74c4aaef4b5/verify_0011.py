#!/usr/bin/env python3
"""Exact, dependency-free verification of the 0011-free coordinate-shattering theorem.
Run with: python3 verify_0011.py
"""
from itertools import combinations, product
from collections import defaultdict

PATTERN = '0011'
# Canonical seven accepting states, plus rejecting state 7.
QUOTIENT = [(0, 1), (0, 4), (0, 5), (0, 6), (2, 6), (1, 7), (3, 7), (7, 7)]
CLASS = [0, 0, 1, 0, 1, 0, 4, 0, 1, 0, 4, 0, 1, 2, 6, 0, 5, 3, 1, 0, 6, 0, 4, 3, 2, 6, 7]

def forbidden_automaton():
    result = []
    for state in range(len(PATTERN)):
        new = []
        for bit in '01':
            word = PATTERN[:state] + bit
            if PATTERN in word:
                new.append(-1)
            else:
                new.append(max(k for k in range(len(PATTERN)) if word.endswith(PATTERN[:k])))
        result.append(tuple(new))
    return result

def subset_transition(state_mask, bit, transitions):
    result = 0
    for state in range(4):
        if state_mask & (1 << state):
            next_state = transitions[state][bit]
            if next_state >= 0:
                result |= 1 << next_state
    return result

def family_step(family, is_query, transitions):
    result = set()
    for subset in family:
        if is_query:
            result.add(subset_transition(subset, 0, transitions))
            result.add(subset_transition(subset, 1, transitions))
        else:
            result.add(subset_transition(subset, 0, transitions) | subset_transition(subset, 1, transitions))
    if 0 in result:
        return None
    return tuple(sorted(result))

def verify_quotient():
    trans = forbidden_automaton()
    assert trans == [(1, 0), (2, 0), (2, 3), (1, -1)], trans
    states = [(1,)]
    ids = {states[0]: 0}
    arrows = []
    for state in states:
        row = []
        for q in (0, 1):
            target = family_step(state, q, trans)
            if target is None:
                row.append(26)
            else:
                if target not in ids:
                    ids[target] = len(states)
                    states.append(target)
                row.append(ids[target])
        arrows.append(tuple(row))
    assert len(states) == 26 and len(arrows) == 26
    assert len(CLASS) == 27
    for i, row in enumerate(arrows):
        assert (CLASS[row[0]], CLASS[row[1]]) == QUOTIENT[CLASS[i]], (i, row)
    # Minimize independently by repeated partition refinement on all states.
    all_arrows = arrows + [(26, 26)]
    partition = [0] * 26 + [1]
    while True:
        signatures = [(partition[i], partition[a], partition[b]) for i, (a, b) in enumerate(all_arrows)]
        label = {key: i for i, key in enumerate(sorted(set(signatures)))}
        new = [label[key] for key in signatures]
        if len(set(new)) == len(set(partition)):
            break
        partition = new
    assert len(set(partition)) == 8
    for i in range(27):
        for j in range(27):
            assert (partition[i] == partition[j]) == (CLASS[i] == CLASS[j])
    return states, arrows

# Polynomials in t,z, represented by dict (degree_t,degree_z) -> integer coefficient.
def poly(terms):
    return {x: v for x, v in terms if v}
def add(*args):
    result = defaultdict(int)
    for p in args:
        for k, v in p.items():
            result[k] += v
    return {k: v for k, v in result.items() if v}
def mul(p, q):
    result = defaultdict(int)
    for (a,b),u in p.items():
        for (c,d),v in q.items():
            result[(a+c,b+d)] += u*v
    return {k:v for k,v in result.items() if v}
def neg(p):
    return {k:-v for k,v in p.items()}
ONE={(0,0):1}; T={(1,0):1}; TZ={(1,1):1}
DEN = poly([((0,0),1),((1,0),-1),((2,1),-2),((3,1),1),((4,2),-1),((5,2),1),((5,3),-1),((6,3),2),((7,3),-1)])
NUMS = [
  poly([((0,0),1),((1,1),1),((2,1),-1),((2,2),1),((3,3),1),((4,2),-1),((4,3),1),((5,3),-1),((6,3),1),((6,4),-1)]),
  poly([((0,0),1),((1,1),1),((2,1),-1),((2,2),1),((4,2),-1),((5,3),-1),((6,3),1)]),
  poly([((0,0),1),((1,1),1),((2,1),-1),((4,2),-1),((4,3),2),((5,3),-1),((6,3),1),((6,4),-1)]),
  poly([((0,0),1),((1,1),1),((2,1),-1),((4,2),-1),((4,3),1),((5,3),-1),((6,3),1)]),
  poly([((0,0),1),((1,1),1),((2,1),-1),((3,2),-1),((4,2),-1),((6,3),1)]),
  poly([((0,0),1),((2,1),-1),((3,2),1),((4,2),-1),((5,3),-1),((6,3),1)]),
  poly([((0,0),1),((2,1),-1),((4,2),-1),((6,3),1)])
]

def verify_rational_identity():
    # H_i = 1 + t H_{delta(i,0)} + tz H_{delta(i,1)}.
    # NUMS[i]/DEN is its unique formal power-series solution.
    for i, (j, k) in enumerate(QUOTIENT[:7]):
        rhs = add(DEN, mul(T, NUMS[j]), mul(TZ, NUMS[k]) if k < 7 else {})
        assert NUMS[i] == rhs, (i, add(NUMS[i],neg(rhs)))
    # For each n, polynomial coefficient extraction from rational function equals DFA counts.
    count = [[0] * 7 for _ in range(41)]
    count[0][0] = 1
    face_coeff = [{0: 1}]
    counts = [{(0,0):1}]
    for n in range(1, 41):
        p = defaultdict(int)
        for (i,k),v in counts[-1].items():
            for bit, dest in enumerate(QUOTIENT[i]):
                if dest < 7:
                    p[(dest,k+bit)] += v
        counts.append(dict(p))
        d = defaultdict(int)
        for (s,k),v in p.items():
            d[k] += v
        face_coeff.append(dict(d))
    # Cross-multiplication coefficientwise D F = NUM0 to 40 in t.
    f={(n,k):v for n, coeff in enumerate(face_coeff) for k,v in coeff.items()}
    left=mul(DEN,f)
    for (nt,nz),v in left.items():
        if nt<=40:
            assert v == NUMS[0].get((nt,nz),0), (nt,nz,v)
    for (nt,nz),v in NUMS[0].items():
        assert left[(nt,nz)]==v
    return face_coeff

def maxplus(X,Y):
    Z=[[None]*7 for _ in range(7)]
    for i in range(7):
        for j in range(7):
            candidates=[X[i][k]+Y[k][j] for k in range(7)
                        if X[i][k] is not None and Y[k][j] is not None]
            if candidates:
                Z[i][j]=max(candidates)
    return Z

def verify_rank():
    A=[[None]*7 for _ in range(7)]
    for i,(a,b) in enumerate(QUOTIENT[:7]):
        A[i][a]=0
        if b<7:
            A[i][b]=1
    powers=[[[0 if i==j else None for j in range(7)] for i in range(7)]]
    for n in range(11):
        powers.append(maxplus(powers[-1], A))
    assert all((None if x is None else x+3)==y
               for row, other in zip(powers[6],powers[11])
               for x,y in zip(row,other))
    assert powers[6]==[
        [3,4,3,4,4,4,4], [3,3,3,3,4,3,4],
        [3,3,3,3,3,3,4], [3,3,3,3,3,3,4],
        [2,3,3,3,3,3,4], [2,3,2,3,3,3,3],
        [2,2,2,3,3,3,3]]
    for n in range(1,11):
        assert max(x for x in powers[n][0] if x is not None) == (3*n+6)//5, n

def brute(n):
    words=[''.join(w) for w in product('01',repeat=n) if PATTERN not in ''.join(w)]
    coeff=defaultdict(int)
    count=0
    for k in range(n+1):
        for sites in combinations(range(n), k):
            traces={tuple(word[i] for i in sites) for word in words}
            accepted = len(traces)==(1<<k)
            state=0
            sites_set=set(sites)
            for i in range(n):
                state=QUOTIENT[state][int(i in sites_set)]
            assert accepted == (state<7), (n,sites,accepted,state)
            if accepted:
                coeff[k]+=1
            count+=1
    return dict(coeff), count

def main():
    states, arrows=verify_quotient()
    faces=verify_rational_identity()
    verify_rank()
    decisions=0
    for n in range(0,13):
        res,num=brute(n)
        assert res==faces[n],(n,res,faces[n])
        decisions+=num
    print('PASS: 26-state closure; seven accepting quotient states; full equivalence checks')
    print('PASS: exact rational polynomial identity in all seven states')
    print('PASS: exact A^11 = 3 + A^6 max-plus matrix identity and base cases')
    print('PASS: independent brute-force check of',decisions,'support decisions, n=0..12')
    for n in (8,10,12):
        print('n=',n,'coefficients=',[faces[n].get(j,0) for j in range(n+1)])
    print('Sample state 0 transition:',QUOTIENT[0]); print('Total original family states:',len(states))

if __name__=='__main__':
    main()
