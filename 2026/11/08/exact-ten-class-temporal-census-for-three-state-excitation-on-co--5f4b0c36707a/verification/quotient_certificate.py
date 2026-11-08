#!/usr/bin/env python3
"""Exhaustive support certificate for three-state excitation on complete tripartite graphs.

A representative of each initially present color is kept at every shore. Its
future state is tracked individually, not just its support. Consequently a
period-one support sequence that rotates labelled vertices cannot be mistaken
for a fixed state. The 343 cases cover all possible support triples.
"""
from collections import Counter, defaultdict
from itertools import product

SUPPORTS = tuple(product(range(1, 8), repeat=3))

def transition(state):
    live = [any(color == 1 for color in shore) for shore in state]
    result = []
    for i, shore in enumerate(state):
        has_excited_neighbor = any(live[j] for j in range(3) if j != i)
        result.append(tuple((color+1) % 3 if color != 0 else int(has_excited_neighbor)
                            for color in shore))
    return tuple(result)

def classify(supports):
    state = tuple(tuple(c for c in range(3) if (mask >> c) & 1)
                  for mask in supports)
    visited = {}
    while state not in visited:
        visited[state] = len(visited)
        state = transition(state)
    return (visited[state], len(visited)-visited[state])

def surj_coeff(mask):
    out = Counter()
    k = mask.bit_count()
    for sub in range(8):
        if (sub & mask) == sub:
            out[sub.bit_count()] += (-1)**(k-sub.bit_count())
    return out

# Powers for positive shore sizes (zero-power terms are correctly omitted).
# Notation: X=sum_i 2^ni; Y=sum_i 3^ni; P=sum_i<j 2^(ni+nj);
# U=2^(sum ni); Q=sum_i 3^ni 2^(N-ni);
# R=sum_i!=j 3^ni 2^nj; V=3^N; 1 denotes the constant term.
BASIS = {
    '1': {(1,1,1):1},
    'X': {(2,1,1):1,(1,2,1):1,(1,1,2):1},
    'Y': {(3,1,1):1,(1,3,1):1,(1,1,3):1},
    'P': {(2,2,1):1,(2,1,2):1,(1,2,2):1},
    'U': {(2,2,2):1},
    'Q': {(3,2,2):1,(2,3,2):1,(2,2,3):1},
    'R': {(3,2,1):1,(3,1,2):1,(2,3,1):1,(1,3,2):1,(2,1,3):1,(1,2,3):1},
    'V': {(3,3,3):1}
}
# Each (entry time, eventual least period) -> expression in the above basis.
EXPECTED = {
 (0,1): {'1':1},
 (0,3): {'V':1,'Q':-3,'U':15,'P':-3,'Y':3,'X':-6,'1':12},
 (1,1): {'U':1,'1':-1},
 (1,3): {'Q':1,'R':-1,'U':-6,'P':5,'Y':2,'X':-6,'1':6},
 (2,1): {'U':1,'Y':1,'X':-2,'1':2},
 (2,3): {'Q':1,'U':-6,'P':1,'Y':-2,'X':4,'1':-6},
 (3,1): {'U':1,'Y':1,'X':-3,'1':7},
 (3,3): {'Q':1,'U':-6,'P':1,'Y':-2,'X':4,'1':-6},
 (4,1): {'Y':1,'X':-1,'1':-3},
 (4,3): {'R':1,'P':-4,'Y':-4,'X':10,'1':-12}
}

def expected_coefficients():
    result = defaultdict(Counter)
    for key, expr in EXPECTED.items():
        for name, scalar in expr.items():
            for powers, coeff in BASIS[name].items():
                result[key][powers] += scalar*coeff
    return result

def coefficient_table():
    result = defaultdict(Counter)
    state_count = Counter()
    for supports in SUPPORTS:
        cls = classify(supports)
        assert cls[0] <= 4 and cls[1] in (1,3), (supports,cls)
        state_count[cls] += 1
        coeff = [surj_coeff(mask) for mask in supports]
        for three in product(*[sorted(c.items()) for c in coeff]):
            powers = tuple(k for k,v in three)
            if 0 in powers: continue  # all shore sizes are positive
            multiplier = three[0][1]*three[1][1]*three[2][1]
            result[cls][powers] += multiplier
    return result,state_count

def simplify(dic):
    return {k:{powers:value for powers,value in cnt.items() if value}
            for k,cnt in dic.items()}

def main():
    assert len(SUPPORTS) == 343
    actual, state_count = coefficient_table()
    expected=expected_coefficients()
    assert simplify(actual)==simplify(expected), (simplify(actual),simplify(expected))
    assert sum(state_count.values()) == 343
    print('PASS 343/343 exact labelled-representative support histories')
    print('PASS all 10 symmetric-basis coefficient identities')
    print('support orbit class census:',sorted(state_count.items()))
    for sizes in [(1,1,1),(1,1,2),(1,2,2),(2,2,2),(2,2,3),(3,3,3)]:
        a,b,c=sizes
        X=2**a+2**b+2**c
        Y=3**a+3**b+3**c
        P=2**(a+b)+2**(a+c)+2**(b+c)
        U=2**(a+b+c)
        Q=3**a*2**(b+c)+3**b*2**(a+c)+3**c*2**(a+b)
        R=sum(3**sizes[i]*2**sizes[j] for i in range(3) for j in range(3) if i!=j)
        V=3**(a+b+c)
        vals={'1':1,'X':X,'Y':Y,'P':P,'U':U,'Q':Q,'R':R,'V':V}
        numbers={key:sum(coef*vals[name] for name,coef in expr.items()) for key,expr in EXPECTED.items()}
        assert sum(numbers.values())==V and min(numbers.values())>=0
        assert sum(number for (t,p),number in numbers.items() if p==1)==3*(U+Y-2*X+2)
        print('PASS shore sizes',sizes,'total',sum(numbers.values()),'entry3cycle_t2=t3',numbers[2,3])
if __name__=='__main__': main()
