"""Reproduce the exact first-recurrence witness on sunlet rotor walks.

No external packages are required. The mathematical proof is independent of
finite computation; this program checks its explicit flow certificates and
runs a direct finite-state microscopic rotor walk.
"""
from collections import Counter
from itertools import product


def setup(n):
    assert n >= 3
    c = (n + 1) // 2
    adj = [[(i + 1) % n, i + n, (i - 1) % n] for i in range(n)]
    adj += [[i] for i in range(n)]
    rotor = [2 if i > c else 1 if i == c else 0 for i in range(n)]
    if n % 2:
        rotor[0] = 2
    rotor += [0] * n
    return c, adj, rotor


def predicted(n):
    c, adj, initial = setup(n)
    q = [0] * (2*n)
    for i in range(n):
        if i == c:
            continue
        if i == 0 and n % 2:
            d = (n - 1) // 2
            q[i] = 3 * d
            q[n+i] = d
        elif i < c:
            d = c - i
            q[i] = 3*d-1
            q[n+i] = d
        else:
            d = i-c
            q[i] = 3*d
            q[n+i] = d
    return c, adj, initial, q


def rotor_is_unicycle(pos, rot, adj):
    # A state is recurrent iff the arrow graph contains exactly one cycle
    # and the chip is on that cycle.
    size = len(adj)
    for x in range(size):
        visited = set()
        y = x
        while y not in visited and y != pos:
            visited.add(y)
            y = adj[y][rot[y]]
        if y != pos:
            return False
    return True


def step(pos, rot, adj):
    new_rot = list(rot)
    new_rot[pos] = (new_rot[pos]+1) % len(adj[pos])
    return adj[pos][new_rot[pos]], new_rot


def certificate(n):
    c, adj, initial, firings = predicted(n)
    final_rot = initial.copy()
    incoming = [0]*(2*n)
    outgoing = [0]*(2*n)
    for v, count in enumerate(firings):
        deg = len(adj[v])
        for t in range(1, count+1):
            target = adj[v][(initial[v]+t) % deg]
            incoming[target]+=1
        outgoing[v] = count
        final_rot[v] = (initial[v]+count) % deg
    # Conservation with one chip initially at rim zero, one at c at end.
    for i in range(2*n):
        assert int(i==0)+incoming[i]-outgoing[i]==int(i==c), (n, i)
    assert all(final_rot[i]==2 for i in range(n) if i!=c)
    assert final_rot[c]==1 and final_rot[n+c]==0
    assert all(final_rot[n+i]==0 for i in range(n))
    assert rotor_is_unicycle(c,final_rot,adj)
    expected=n*n-(n+1)//2
    assert sum(firings)==expected
    return expected, firings


def direct_witness(n):
    c, adj, rot = setup(n)
    current = 0
    t = 0
    while current != c:
        assert not rotor_is_unicycle(current,rot,adj)
        current, rot = step(current,rot,adj)
        t+=1
        assert t<10*n*n
    assert rotor_is_unicycle(current,rot,adj)
    return t


def exhaustive_max(n):
    c, adj, base = setup(n)
    cnt=Counter()
    for digits in product(range(3),repeat=n):
        current=0
        rotor=list(digits)+[0]*n
        t=0
        while not rotor_is_unicycle(current,rotor,adj):
            current,rotor=step(current,rotor,adj)
            t+=1
            assert t<10*n*n
        cnt[t]+=1
    return max(cnt),cnt[max(cnt)],sum(cnt.values())


def main():
    for n in range(3,501):
        certificate(n)
    print('Conservation, rotor arrows, and time verified for n=3..500')
    for n in range(3,61):
        target,_=certificate(n)
        assert direct_witness(n)==target
    print('Independent direct witness simulation passed for n=3..60')
    for n in range(3,9):
        observed,multiplicity,total=exhaustive_max(n)
        target,_=certificate(n)
        assert observed==target and multiplicity==1
        print('n=%d: observed max=%d, states attaining max=%d, checked=%d' %(n,observed,multiplicity,total))
    print('Finite checks completed; no all-size extremality inferred from finite runs')

if __name__=='__main__':
    main()
