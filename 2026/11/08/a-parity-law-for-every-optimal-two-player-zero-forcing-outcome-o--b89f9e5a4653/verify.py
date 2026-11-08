#!/usr/bin/env python3
"""Exact certificate for optimal-play outcomes on edge-deleted cliques.

Implements the game's stated colour-change and force-preservation rules;
the finite-state period check supports an induction for every clique size.
No nonstandard modules are required.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path

# 0=white, 1=blue, 2=red for the two nonadjacent exceptional vertices.
# c_blue,c_red flag whether a player owns any universal-clique vertex.
# turn=0 for blue, 1 for red.  Future payoffs count force moves.
@lru_cache(None)
def compressed(w, x, y, c_blue, c_red, turn):
    white = w + (x == 0) + (y == 0)
    if not white:
        return frozenset({(0, 0)})
    own_u = (c_blue, c_red)[turn]
    other_u = (c_blue, c_red)[1-turn]
    own_e = x == turn+1 or y == turn+1
    other_e = x == 2-turn or y == 2-turn
    own_forces = set()
    other_forces = set()
    if w == 1 and own_e:
        own_forces.add('u')
    if w == 1 and other_e:
        other_forces.add('u')
    if white == 1:
        for universal_owner, target_set in (
            (own_u, own_forces), (other_u, other_forces)):
            if universal_owner:
                if w:
                    target_set.add('u')
                if x == 0:
                    target_set.add('x')
                if y == 0:
                    target_set.add('y')
    options = (['u'] if w else []) + (['x'] if x == 0 else []) + (['y'] if y == 0 else [])
    safe_seed = any(s not in own_forces and s not in other_forces for s in options)
    candidates = []
    for target in options:
        is_force = target in own_forces
        # If a nonblocking seed is available, blocking seeds are illegal.
        if not is_force and target in other_forces and safe_seed:
            continue
        state = (
            w-(target=='u'),
            (turn+1 if target=='x' else x),
            (turn+1 if target=='y' else y),
            int(c_blue or (target=='u' and turn==0)),
            int(c_red or (target=='u' and turn==1)),
            1-turn
        )
        for future in compressed(*state):
            pair = list(future)
            if is_force:
                pair[turn] += 1
            candidates.append(tuple(pair))
    best = max(z[turn] for z in candidates)
    return frozenset(z for z in candidates if z[turn] == best)

STATES = list(product(range(3), range(3), range(2), range(2), range(2)))

def table(w):
    return {v:compressed(w, *v) for v in STATES}

def render_outcomes(value):
    return ';'.join(f'{a},{b}' for a,b in sorted(value))

def certificate():
    lines = ['x\ty\tc_blue\tc_red\tturn\tF3\tF5']
    t3,t5=table(3),table(5)
    for state in STATES:
        x,y,ca,cb,p=state
        lines.append('\t'.join(map(str,(x,y,ca,cb,p)))+'\t'+render_outcomes(t3[state])+'\t'+render_outcomes(t5[state]))
    return ('\n'.join(lines)+'\n').encode('utf8')

# Fully distinct, vertex-labelled full game; no twin compression.
def vertex_bruteforce(n):
    universal=set(range(2,n))
    adj=[sum(1<<v for v in range(n) if v!=u and not (u<2 and v<2)) for u in range(n)]
    all_bits=(1<<n)-1
    @lru_cache(None)
    def solve(blue,red):
        white=all_bits ^ (blue|red)
        if white==0:
            return frozenset({(0,0)})
        mover=(blue|red).bit_count()%2
        mine=(blue,red)[mover]
        theirs=(red,blue)[mover]
        def legal_force_targets(owned):
            targets=0
            for i in range(n):
                if owned & (1<<i):
                    avail=adj[i] & white
                    if avail.bit_count()==1:
                        targets|=avail
            return targets
        f=legal_force_targets(mine)
        g=legal_force_targets(theirs)
        remaining=[i for i in range(n) if white & (1<<i)]
        safe=any(not (f&(1<<i)) and not (g&(1<<i)) for i in remaining)
        pairs=[]
        for i in remaining:
            forcing=bool(f&(1<<i))
            if not forcing and safe and (g&(1<<i)):
                continue
            next_blue=blue|(1<<i) if mover==0 else blue
            next_red=red|(1<<i) if mover==1 else red
            for pair in solve(next_blue,next_red):
                new=list(pair)
                if forcing:
                    new[mover]+=1
                pairs.append(tuple(new))
        opt=max(z[mover] for z in pairs)
        return frozenset(z for z in pairs if z[mover]==opt)
    return solve(0,0),solve.cache_info().currsize

def verify():
    # A direct finite enumeration, not an extrapolation: the transition
    # F_w = Phi(F_(w-1)) is independent of w whenever w>=2, because
    # no force can occur with two or more universal vertices still white.
    t3,t5=table(3),table(5)
    assert len(STATES)==72
    assert t3==t5, 'full-state two-step transfer period failed'
    assert certificate()==Path(__file__).with_name('periodicity_certificate.tsv').read_bytes()
    print('FULL_72_STATE_PERIOD_CERTIFICATE_OK F3=F5')
    # Initial state has both exceptional vertices white and no owned
    # universal.  These base cases + the transfer period prove all n>=4.
    assert compressed(1,0,0,0,0,0)==frozenset({(1,0)})
    assert compressed(2,0,0,0,0,0)==frozenset({(1,1)})
    assert compressed(3,0,0,0,0,0)==frozenset({(1,0),(1,1)})
    assert compressed(4,0,0,0,0,0)==frozenset({(1,1)})
    print('ROOT_BASE_CASES_OK')
    for r in range(2,101):
        expected=frozenset({(1,1)}) if r%2==0 else frozenset({(1,0),(1,1)})
        assert compressed(r,0,0,0,0,0)==expected
    print('EXTRA_ROOT_CHECKS_OK r=2..100')
    total=0
    for n in range(3,11):
        direct,states=vertex_bruteforce(n)
        assert direct==compressed(n-2,0,0,0,0,0),(n,direct)
        total+=states
    print('INDEPENDENT_VERTEX_LEVEL_BACKWARD_INDUCTION_OK n=3..10 states',total)
    print('VERIFY_OK')
if __name__=='__main__':
    verify()
