"""Finite reproducibility checks for valuation-controlled automatic words.
Run: python3 verify.py. Uses Python standard library only.
"""
from collections import deque
from itertools import product


def tail_value(prefix, a, p, j):
    return prefix[j if j < a + p else a + (j - a) % p]


def intrinsic(a, p, prefix, base):
    f = lambda j: tail_value(prefix, a, p, j)
    reps = {}
    signatures = {}
    for i in range(a + p):
        sig = tuple(f(i+t) for t in range(3*(a+p)+3))
        if sig not in signatures:
            signatures[sig] = i
        reps[i] = signatures[sig]
    states = sorted(set(reps.values()))
    transitions = {
        s: tuple(reps[s+1 if s+1 < a+p else a] if d == base-1 else reps[0]
                 for d in range(base))
        for s in states
    }
    return reps[0], states, transitions, reps


def first_inhomogeneous(start, states, transitions, base, bound):
    ids = {s:i for i,s in enumerate(states)}
    masks0 = (0,)*len(states)
    todo = deque([(start, masks0, 0)])
    seen = {(start, masks0)}
    while todo:
        state, masks, length = todo.popleft()
        if length >= bound:
            continue
        for digit in range(base):
            target = transitions[state][digit]
            newmasks = list(masks)
            newmasks[ids[target]] |= 1 << digit
            value = newmasks[ids[target]]
            if value.bit_count() > 1:
                return length+1
            item = (target, tuple(newmasks))
            if item not in seen:
                seen.add(item)
                todo.append((target, tuple(newmasks), length+1))
    return None


def exact_a_p(prefix, a, p):
    f = lambda j: tail_value(prefix,a,p,j)
    actual_period = next(d for d in range(1,p+1) if all(f(j)==f(j+d) for j in range(a,a+5*p)))
    actual_start = next(j for j in range(a+1) if all(f(i)==f(i+actual_period) for i in range(j,a+5*p)))
    return actual_start == a and actual_period == p


def direct_word(base, n):
    if n == 0:
        return ()
    digits=[]
    while n:
        digits.append(n%base)
        n//=base
    return tuple(reversed(digits))


def valuation(base, n):
    n += 1
    t=0
    while n % base == 0:
        n//=base
        t+=1
    return t


def run():
    configurations = 0
    evaluations = 0
    for a in range(4):
        for p in range(1,7):
            for prefix in product(range(2), repeat=a+p):
                if not exact_a_p(prefix, a, p):
                    continue
                for base in (2,3,4,5):
                    start, states, trans, reps = intrinsic(a,p,prefix,base)
                    assert len(states)==a+p, (a,p,prefix,base,states)
                    actual = first_inhomogeneous(start,states,trans,base,p+4)
                    expected = p+1 if (base==2 and a==0) else (None if base==2 else 2)
                    assert actual==expected,(base,a,p,prefix,actual,expected)
                    for n in range(70):
                        state=start
                        for d in direct_word(base,n):
                            state=trans[state][d]
                        target=tail_value(prefix,a,p,valuation(base,n))
                        assert prefix[state]==target,(a,p,base,n,prefix,state,target)
                        evaluations+=1
                    configurations+=1
    # Additional three-symbol examples include genuine transients and pure periods.
    for a,p in [(0,2),(0,4),(1,2),(2,3)]:
        for prefix in product(range(3),repeat=a+p):
            if not exact_a_p(prefix,a,p):
                continue
            for base in (2,3,7):
                s,states,T,_=intrinsic(a,p,prefix,base)
                assert len(states)==a+p
                actual=first_inhomogeneous(s,states,T,base,p+4)
                assert actual == (p+1 if base==2 and a==0 else (None if base==2 else 2))
                configurations+=1
    print(f'VERIFY_OK configurations={configurations} digit_evaluations={evaluations}')

if __name__=='__main__':
    run()
