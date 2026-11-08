"""Finite checks for sharp obstruction rank with h Horn hypotheses.
Runs independently from external packages; no finite check is offered as a proof.
"""
from itertools import combinations
from math import comb

def is_subset(a,b): return (a & b)==a

def middle_witnesses(h):
    k=h//2
    return tuple(s for s in range(1<<h) if s.bit_count() in {k,k+1})

def extremal(h):
    k=h//2
    return comb(h,k)+(comb(h,k+1) if k+1<=h else 0)

def minima(sets):
    return tuple(s for s in sets if not any(t!=s and is_subset(t,s) for t in sets))

def construct_rules(h, W):
    # Rules have a head ('g' or 'bad') and an exact source guard plus hypothesis mask.
    universe=range(1<<h)
    rules=[]
    for c in W:
        E=set(W)-{c}
        down={s for s in universe if any(is_subset(s,t) for t in E)}
        bad_min=minima(set(universe)-down)
        for a in minima(E): rules.append(('g',c,a))
        for b in bad_min: rules.append(('bad',c,b))
    return tuple(rules)

def closure_valid(rules,c,s):
    got_g=any(head=='g' and context==c and is_subset(body,s) for head,context,body in rules)
    got_bad=any(head=='bad' and context==c and is_subset(body,s) for head,context,body in rules)
    return got_g and not got_bad

def check_witness(h):
    W=middle_witnesses(h)
    assert len(W)==extremal(h)
    # Independent closure evaluation across all Boolean hypothesis sets.
    rules=construct_rules(h,W)
    for c in W:
        expected=set(W)-{c}
        actual={s for s in range(1<<h) if closure_valid(rules,c,s)}
        assert actual==expected, (h,c,actual,expected)
    assert not set.intersection(*(set(W)-{c} for c in W)) if W else True
    for c in W:
        assert c in set.intersection(*(set(W)-{d} for d in W if d!=c)) if len(W)>1 else True
    # Check that each family is order convex by direct interval enumeration.
    for c in W:
        E=set(W)-{c}
        for a in E:
            for b in E:
                if is_subset(a,b):
                    assert all((not(is_subset(a,z) and is_subset(z,b))) or z in E for z in range(1<<h))
    return len(rules)

def check_upper_exhaustive(h):
    N=1<<h
    forbidden=[]
    for a,b,c in combinations(range(N),3):
        if ((is_subset(a,b) and is_subset(b,c)) or
            (is_subset(a,c) and is_subset(c,b)) or
            (is_subset(b,a) and is_subset(a,c)) or
            (is_subset(b,c) and is_subset(c,a)) or
            (is_subset(c,a) and is_subset(a,b)) or
            (is_subset(c,b) and is_subset(b,a))):
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    maximum=0
    for family in range(1<<N):
        if family.bit_count()<=maximum: continue
        if all(family & ban !=ban for ban in forbidden):
            maximum=family.bit_count()
    assert maximum==extremal(h), (h,maximum,extremal(h))
    return maximum

if __name__=='__main__':
    for h in range(5):
        nr=check_witness(h)
        upper=check_upper_exhaustive(h)
        print(f'h={h}: upper={upper}, witness={extremal(h)}, rules={nr}')
    for h in [5,6,7,8]:
        # Higher-h constructive test only, no exhaustive 2-Sperner census.
        nr=check_witness(h)
        print(f'h={h}: witness={extremal(h)}, rules={nr}')
    print('ALL_CHECKS_OK')
