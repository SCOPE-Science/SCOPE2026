"""Exact rational diagnostics for a three-sheet covering approximation theorem.

The graph-covering arguments are analytical; this finite code checks arithmetic,
integer allocation bounds, and small labelled-atom move paths only.
"""
from fractions import Fraction as Q
from collections import deque


def pos(x):
    return max(Q(0), x)


def eq_target(m):
    rem = m % 3
    return Q(8, 3*m) if rem == 2 else Q(2, m)


def eq_lower(m, r):
    n = m - r
    if not n:
        return Q(4, 3)
    counts = ((n - 1)//2, n//2)
    deficit = pos(Q(1, 3)-Q(r, m))
    deficit += sum(pos(Q(1, 3)-Q(k, m)) for k in counts)
    return 2*deficit


def witness_r(m):
    if m % 3 == 1:
        return m//3
    if m % 3 == 2:
        return m//3 + 1
    return m//3


def stationary_cost(m, r, state, moved):
    n = m-r
    c0 = sum(v == 0 for j,v in enumerate(state) if j != moved)
    c1 = n-1-c0
    return (pos(Q(1,3)-Q(r,m))+
            pos(Q(1,3)-Q(c0,m))+
            pos(Q(1,3)-Q(c1,m)))


def path_exists(m, r):
    n = m-r
    if n == 0:
        return False
    start = tuple([0]*((n+1)//2)+[1]*(n//2))
    goal = tuple(1-v for v in start)
    cutoff = eq_target(m)/2
    visited = {start}
    queue = deque([start])
    while queue:
        s = queue.popleft()
        if s == goal:
            return True
        for j in range(n):
            if stationary_cost(m,r,s,j)>cutoff:
                continue
            t = list(s)
            t[j] ^= 1
            t=tuple(t)
            if t not in visited:
                visited.add(t)
                queue.append(t)
    return False


def main():
    checks=0
    for m in range(1,501):
        lower = min(eq_lower(m,r) for r in range(m+1))
        assert lower == (Q(4,3) if m == 1 else eq_target(m)), (m, lower)
        checks += 1
        if m >= 2:
            r=witness_r(m)
            assert 1<=r<m, (m,r)
            assert eq_lower(m,r)==eq_target(m), (m,r)
            checks += 2
            # Independent reduction of the connected double-cover formula.
            n=m-1
            k, rem=divmod(n-1,2)
            s=2-rem
            connected=Q(2*s,2*(k*s+1))
            assert connected==Q(2,n)
            assert Q(2,3)*connected == Q(4,3*(m-1))
            checks += 2
    for m in range(2,19):
        assert path_exists(m,witness_r(m)), m
        checks+=1
    print('THREE_SHEET_RATIONAL_CHECK_OK', checks)

if __name__=='__main__':
    main()
