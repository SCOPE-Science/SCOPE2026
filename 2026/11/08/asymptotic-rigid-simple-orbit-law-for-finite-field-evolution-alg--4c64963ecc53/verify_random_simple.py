#!/usr/bin/env python3
"""Exact small-field checks for a random evolution-algebra orbit law.

No external libraries. The ambient model is the full finite matrix space and the
natural-basis action is by nonzero column scalings and simultaneous permutations.
"""
import itertools
from math import factorial


def det_nonzero(a, n, p):
    b = [[a[i*n+j] for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k,n) if b[i][k]), None)
        if pivot is None: return False
        b[k],b[pivot] = b[pivot],b[k]
        inv=pow(b[k][k],-1,p)
        for j in range(k,n): b[k][j]=(b[k][j]*inv)%p
        for i in range(k+1,n):
            x=b[i][k]
            if x:
                for j in range(k,n): b[i][j]=(b[i][j]-x*b[k][j])%p
    return True


def strongly_connected(a,n):
    for source in range(n):
        seen={source}
        todo=[source]
        while todo:
            i=todo.pop()
            for j in range(n):
                if a[i*n+j] and j not in seen:
                    seen.add(j);todo.append(j)
        if len(seen)!=n:return False
    return True


def action(a,perm,t,p):
    n=len(perm)
    return tuple((t[i]*t[i]*a[perm[i]*n+perm[j]]*pow(t[j],-1,p))%p
                 for i in range(n) for j in range(n))


def run(p,n):
    group=list(itertools.product(itertools.permutations(range(n)),
                                  itertools.product(range(1,p),repeat=n)))
    assert len(group)==factorial(n)*(p-1)**n
    seen=set()
    simple=0; rigid=0; stabilizer_sum=0; orbits=0
    for a in itertools.product(range(p), repeat=n*n):
        if not det_nonzero(a,n,p) or not strongly_connected(a,n):
            continue
        simple+=1
        # Direct action enumeration independently computes stabilizer and orbit.
        orb={action(a,sigma,t,p) for sigma,t in group}
        stab=sum(action(a,sigma,t,p)==a for sigma,t in group)
        assert len(orb)*stab==len(group)
        assert all(det_nonzero(b,n,p) and strongly_connected(b,n) for b in orb)
        stabilizer_sum+=stab
        rigid+=(stab==1)
        if a not in seen:
            orbits+=1
            assert not (orb & seen)
            seen.update(orb)
    assert len(seen)==simple
    assert stabilizer_sum%len(group)==0
    assert stabilizer_sum//len(group)==orbits
    print(f'p={p} n={n} matrices={p**(n*n)} simple={simple} '
          f'rigid_simple={rigid} classes={orbits} action_size={len(group)} '
          f'burnside_stabilizers={stabilizer_sum}')

if __name__=='__main__':
    for params in [(2,2),(2,3),(3,2),(3,3),(5,2)]: run(*params)
    print('VERIFY_OK exact_orbit_and_burnside_agreement=yes')
