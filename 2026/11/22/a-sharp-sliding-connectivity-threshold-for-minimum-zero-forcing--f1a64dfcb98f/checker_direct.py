"""Standalone original-graph zero-forcing and reconfiguration checker.
Run: python checker_direct.py. No third-party dependencies.
"""
from itertools import combinations
from collections import deque

def zero_forces(initial,n):
    blue=set(initial)
    while True:
        forced=set()
        for u in blue:
            white={v for v in range(n) if v not in blue and abs(u-v)>1}
            if len(white)==1:
                forced.update(white)
        if not forced:
            return len(blue)==n
        blue.update(forced)

def audit(n):
    V=set(range(n))
    assert all(not zero_forces(S,n) for k in range(n-3) for S in combinations(range(n),k))
    triples=[frozenset(W) for W in combinations(range(n),3) if zero_forces(V-set(W),n)]
    expected={frozenset(W) for W in combinations(range(n),3)
              if any(a+2 in W and a+1 not in W for a in W)}
    assert set(triples)==expected
    assert len(triples)==(n-3)**2+1
    T=set(triples)
    jump={w:set() for w in T}; slide={w:set() for w in T}
    for w in T:
        for a in w:
            for b in V-w:
                t=frozenset((w-{a})|{b})
                if t in T:
                    jump[w].add(t)
                    if abs(a-b)>1:
                        slide[w].add(t)
    def components(H):
        rest=set(H); sizes=[]
        while rest:
            start=next(iter(rest)); rest.remove(start); group={start}; q=deque([start])
            while q:
                for x in H[q.popleft()]:
                    if x not in group: group.add(x);rest.remove(x);q.append(x)
            sizes.append(len(group))
        return sorted(sizes)
    J=sum(map(len,jump.values()))//2
    S=sum(map(len,slide.values()))//2
    if n==5:
        assert (len(T),J,S,components(slide))==(5,5,1,[1,1,1,2])
    else:
        assert J==(n**3-3*n*n-32*n+126)//2
        assert S==(n**3-5*n*n-22*n+118)//2
        assert components(slide)==[len(T)]
    print(f'n={n}: states={len(T)}, jumps={J}, slides={S}, slide_components={components(slide)}')

if __name__=='__main__':
    for n in range(5,13):audit(n)
    print('DIRECT CHECKS PASSED')
