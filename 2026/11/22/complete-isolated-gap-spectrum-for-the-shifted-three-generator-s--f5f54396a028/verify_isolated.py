"""Exact checks for an isolated-gap theorem in three-generator numerical semigroups.

No third-party dependencies. Run: python3 verify_isolated.py
"""
from heapq import heappush, heappop


def predicted(a):
    if a < 6:
        raise ValueError('the theorem assumes a >= 6')
    result = [t*a+5 for t in range(2,a//4+3)]
    if a % 4 == 2:
        result.append(((a+2)//4)*a-1)
    if a % 4 == 3:
        result.append(((a+5)//4)*a+2)
    return sorted(result)


def apery_bound(a):
    # Independent shortest-path calculation on the a residue classes.
    distant = 10**50
    dist = [distant]*a
    dist[0] = 0
    heap = [(0,0)]
    while heap:
        value, residue = heappop(heap)
        if value != dist[residue]:
            continue
        for c in (a+3,a+4):
            other = (residue+c)%a
            candidate = value+c
            if candidate < dist[other]:
                dist[other] = candidate
                heappush(heap,(candidate,other))
    assert max(dist)<distant
    return max(dist)-a


def enumerate_membership(a, upper):
    # Independent unbounded coin-addition dynamic program to finite cutoff.
    member = bytearray(upper+2)
    member[0]=1
    for n in range(upper+2):
        if member[n]:
            for c in (a,a+3,a+4):
                if n+c<=upper+1:
                    member[n+c]=1
    return member


def check_offsets():
    # Independently enumerate the possible offsets using exactly t coins.
    for t in range(2,101):
        offsets = {3*y+4*z for y in range(t+1)
                   for z in range(t-y+1)}
        expected = {0,3,4}|set(range(6,4*t+1))
        assert offsets==expected,(t,offsets^expected)
    return 99


def check_all():
    total_gaps = 0
    total_isolated = 0
    cases = 0
    for a in range(6,211):
        frob = apery_bound(a)
        upper = frob + 3
        member = enumerate_membership(a, upper)
        assert all(member[n] for n in range(frob+1,upper+2))
        actual = [n for n in range(1,upper+1)
                  if not member[n] and member[n-1] and member[n+1]]
        expected = predicted(a)
        assert actual==expected,(a,actual,expected)
        assert len(expected)==(a+2)//4+1
        assert len(expected)==len(set(expected))
        total_gaps+=sum(1 for n in range(1,frob+1) if not member[n])
        total_isolated+=len(actual)
        cases+=1
    return cases,total_gaps,total_isolated

if __name__=='__main__':
    print('offset tests:',check_offsets())
    print('semigroup checks (a, gap states, isolated gaps):', check_all())
    print('PASS')
