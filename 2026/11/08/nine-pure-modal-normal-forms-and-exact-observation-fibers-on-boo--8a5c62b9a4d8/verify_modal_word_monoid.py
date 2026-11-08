"""Finite checks for a normal-form theorem on Boolean compatibility frames.
Run: python3 verify_modal_word_monoid.py. No external dependencies.
"""
from collections import Counter
from functools import reduce
from itertools import combinations
from math import comb

WORDS = ('', 'B', 'D', 'BB', 'BD', 'DB', 'DD', 'BBD', 'DDB')

def cover_count(n):
    return sum((-1)**j * comb(n, j) * (1 << ((1 << (n-j))-1))
               for j in range(n+1))

def make_frame(n):
    assert n >= 1
    atoms = (1 << n)-1
    world_masks = list(range(1, atoms+1))
    all_events = (1 << len(world_masks))-1
    adjacency = tuple(sum(1 << i for i, v in enumerate(world_masks)
                          if u & v) for u in world_masks)
    return world_masks, adjacency, all_events

def support(family, world_masks):
    return reduce(lambda s, index: s | world_masks[index],
                  (i for i in range(len(world_masks)) if family & (1 << i)), 0)

def mask_d(s, world_masks):
    return sum(1 << i for i, v in enumerate(world_masks) if v & s)

def mask_i(s, world_masks):
    return sum(1 << i for i, v in enumerate(world_masks) if v & ~s == 0)

def apply(word, event, adjacency, all_events):
    val = event
    for symbol in reversed(word):
        if symbol == 'D':
            val = sum(1 << i for i, neigh in enumerate(adjacency) if neigh & val)
        else:
            val = sum(1 << i for i, neigh in enumerate(adjacency)
                      if neigh & (~val & all_events) == 0)
    return val

def closed_form(word, U, world_masks, all_events):
    ground = world_masks[-1]
    S = support(U, world_masks)
    T = ground & ~support(all_events ^ U, world_masks)
    D = mask_d
    I = mask_i
    return {'':U, 'B':I(T,world_masks),'D':D(S,world_masks),
            'BB': all_events if U==all_events else 0,
            'DD': all_events if U else 0,
            'BD':I(S,world_masks),'DB':D(T,world_masks),
            'BBD':all_events if S==ground else 0,
            'DDB':all_events if T else 0}[word]

def verify(n):
    worlds, adjacency, full = make_frame(n)
    ground=worlds[-1]
    signatures = {word:[] for word in WORDS}
    spectrum=Counter()
    for U in range(full+1):
        S=support(U,worlds)
        T=ground & ~support(full ^ U,worlds)
        spectrum[(S,T)]+=1
        for word in WORDS:
            actual=apply(word,U,adjacency,full)
            expected=closed_form(word,U,worlds,full)
            assert actual == expected,(n,U,word,actual,expected)
            signatures[word].append(actual)
    if n==1:
        assert len({tuple(v) for v in signatures.values()})==1
    else:
        assert len({tuple(v) for v in signatures.values()}) == 9
        assert len(spectrum) == (1 << (n+1))-1
        for S in range(ground):
            assert spectrum[(S,0)] == cover_count(S.bit_count())
        for T in range(1,ground+1):
            assert spectrum[(ground,T)] == cover_count(n-T.bit_count())
        leftover=cover_count(n)-sum(comb(n,t)*cover_count(n-t)
                                   for t in range(1,n+1))
        assert spectrum[(ground,0)] == leftover
        assert all(not (S!=ground and T!=0) for S,T in spectrum)
        for word in ('B','D','BD','DB'):
            assert len(set(signatures[word])) == (1<<n)
        for word in ('BB','DD','BBD','DDB'):
            assert len(set(signatures[word])) == 2
    # Closure by prefixing B or D: check the complete operation table.
    table={
        '':('B','D'),'B':('BB','DB'),'D':('BD','DD'),
        'BB':('BB','BB'),'BD':('BBD','D'),'DB':('B','DDB'),
        'DD':('DD','DD'),'BBD':('BBD','BBD'),'DDB':('DDB','DDB')}
    for name,(b,d) in table.items():
        assert tuple(apply('B'+name,u,adjacency,full) for u in range(full+1)) == tuple(signatures[b])
        assert tuple(apply('D'+name,u,adjacency,full) for u in range(full+1)) == tuple(signatures[d])
    return {'n':n, 'events':full+1, 'distinct_words':len({tuple(v) for v in signatures.values()}),
            'joint_profiles':len(spectrum), 'cover_count':cover_count(n),
            'unprotected_full_support':spectrum[(ground,0)]}

if __name__ == '__main__':
    for n in range(1,5):print(verify(n))
    print('PASS: exhaustive event cases, nine normal forms, profile fibers, and prefix table')
