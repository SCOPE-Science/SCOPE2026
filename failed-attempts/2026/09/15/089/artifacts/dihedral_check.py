"""Bounded recovery test: dihedral-group verification of the two blocking obstructions.

Obstruction A (odd m): in I_2(m) = <s,t | s^2=t^2=(st)^m=1>, s conjugate to t iff m odd.
Obstruction B (finite n): alternating word (st)^k of length 2k is reduced only while
2k <= m (longest element has length m); in particular a periodic 2-letter ray is not an
infinite geodesic when the label is finite. In the duplex with m,n both finite, the
published avoidant pair (alternating b'a'-rays across an n-labelled edge) therefore
fails to be geodesic, and every 2-generator special subgroup is spherical.
"""
from collections import deque


def dihedral(m):
    def prod(e1, e2):
        k1, a = e1
        k2, b = e2
        if k1 == 0 and k2 == 0:
            return (0, (a + b) % m)
        if k1 == 0 and k2 == 1:
            return (1, (b - a) % m)
        if k1 == 1 and k2 == 0:
            return (1, (a + b) % m)
        return (0, (b - a) % m)

    def mul(e, g, t):
        s = (1, 0)
        return prod(e, s if g == 's' else t)

    t = (1, 1)
    dist = {(0, 0): 0}
    q = deque([(0, 0)])
    while q:
        e = q.popleft()
        for g in ('s', 't'):
            f = mul(e, g, t)
            if f not in dist:
                dist[f] = dist[e] + 1
                q.append(f)

    def inv(e):
        k, a = e
        return (0, (-a) % m) if k == 0 else e

    s = (1, 0)
    elems = list(dist)
    conj = {prod(prod(g, s), inv(g)) for g in elems}
    # alternating word lengths vs distance
    r = prod(s, t)
    e = (0, 0)
    alt = []
    for k in range(0, m + 2):
        alt.append((k, e, dist[e], 2 * k, dist[e] == 2 * k))
        e = prod(e, r)
    return len(dist), t in conj, alt


for m in (4, 5):
    order, conj, alt = dihedral(m)
    print(f'm={m} |G|={order} s_conj_t={conj}')
    for k, e, d, wl, red in alt:
        print(f'  (st)^{k}: elem={e} dist={d} wordlen={wl} reduced={red}')
