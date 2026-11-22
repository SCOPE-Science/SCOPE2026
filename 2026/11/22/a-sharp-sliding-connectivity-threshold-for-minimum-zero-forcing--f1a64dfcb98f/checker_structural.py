"""Independent triple-criterion and pair-completion checker.
Run: python checker_structural.py. No third-party dependencies.
"""
from itertools import combinations
from collections import deque

def valid(t):
    t=set(t)
    return any(x+2 in t and x+1 not in t for x in t)

def pair_completion(n,a,b):
    d=b-a
    if d==1:
        return {x for x in (a-2,b+2) if 0<=x<n}
    if d==2:
        return set(range(n))-{a,a+1,b}
    return {x for x in (a-2,a+2,b-2,b+2) if 0<=x<n and x not in (a,b)}

def audit(n):
    good={frozenset(t) for t in combinations(range(n),3) if valid(t)}
    J=S=0
    for a,b in combinations(range(n),2):
        K=pair_completion(n,a,b)
        assert K=={c for c in range(n) if c not in (a,b) and valid((a,b,c))}
        J+=len(K)*(len(K)-1)//2
        S+=len(K)*(len(K)-1)//2 -sum(c+1 in K for c in K)
    if n>=6:
        assert J*2==n**3-3*n*n-32*n+126
        assert S*2==n**3-5*n*n-22*n+118
        assert J-S==n*n-5*n+4
        # Structural-fibre connectivity, without zero-forcing simulation.
        # Every vertex is covered by at least one a-fibre.
        fibres=[{frozenset((a,a+2,t)) for t in range(n) if t not in (a,a+1,a+2)} for a in range(n-2)]
        assert set().union(*fibres)==good
        if n>=7:
            for f in fibres:
                rest=set(f); q=[rest.pop()]
                for x in q:
                    for y in tuple(rest):
                        a=next(iter(x-y));b=next(iter(y-x))
                        if abs(a-b)>1:q.append(y);rest.remove(y)
                assert not rest
    else:
        assert n==5 and (J,S)==(5,1)
    print(f'n={n}: {len(good)} states; {J} jumps; {S} slides')

if __name__=='__main__':
    for n in range(5,61): audit(n)
    print('STRUCTURAL CHECKS PASSED')
