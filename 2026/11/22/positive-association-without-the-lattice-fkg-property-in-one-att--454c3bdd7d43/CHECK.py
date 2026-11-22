"""Exact finite-model diagnostics for colored one-shot antagonistic deposition.

Only Python standard-library modules are used.  The universal association
assertion is an analytic theorem and is not inferred from these finite tests.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations, combinations
from math import factorial


def neighbors(n, edges):
    masks = [0] * n
    for i, j in edges:
        masks[i] |= 1 << j
        masks[j] |= 1 << i
    return masks


def exact_law(n, edges, p, t):
    """Exact probabilities for all A-occupation masks at observation time t."""
    ne = neighbors(n, edges)
    q = 1-p
    output = defaultdict(Q)
    for attempted in range(1 << n):
        vertices = [v for v in range(n) if attempted >> v & 1]
        m = len(vertices)
        time_weight = t**m * (1-t)**(n-m) / factorial(m)
        if not time_weight:
            continue
        for order in permutations(vertices):
            for colors in range(1 << m):
                num_a = colors.bit_count()
                w = time_weight * p**num_a * q**(m-num_a)
                if not w:
                    continue
                a = b = 0
                for k, v in enumerate(order):
                    if colors >> k & 1:
                        if not (b & ne[v]):
                            a |= 1 << v
                    else:
                        if not (a & ne[v]):
                            b |= 1 << v
                output[a] += w
    assert sum(output.values()) == 1
    return output


def triangle_closed_form(p, t):
    w0 = (1-p)+p*(1-t)**3
    w1 = p*t*(3 - 3*(p+1)*t + (p*p+p+1)*t*t)/3
    w2 = p*p*t*t*(3 - (2*p+1)*t)/3
    w3 = p*p*p*t*t*t
    det = -p**4*(1-p)*t**5*(3-(p+2)*t)/9
    return w0, w1, w2, w3, det


def time_order_outcome(n, edges, potential_times):
    ne = neighbors(n, edges)
    a = b = 0
    first = []
    for v in range(n):
        ta, tb = potential_times[2*v], potential_times[2*v+1]
        first.append((min(ta,tb), v, ta < tb))
    for _, v, is_a in sorted(first):
        if is_a:
            if not (b & ne[v]):
                a |= 1 << v
        else:
            if not (a & ne[v]):
                b |= 1 << v
    return a,b


def all_graphs(n):
    pairs = list(combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        yield [edge for j,edge in enumerate(pairs) if bits >> j & 1]


def test():
    checks = 0
    for p in (Q(1,3), Q(1,2), Q(4,5)):
        for t in (Q(1,5), Q(1,2), Q(1,1)):
            law = exact_law(3, [(0,1),(0,2),(1,2)], p, t)
            w0,w1,w2,w3,D = triangle_closed_form(p,t)
            assert law[0] == w0
            for a in range(1,8):
                assert law[a] == (w1,w2,w3)[a.bit_count()-1]
                checks+=1
            assert law[1]*law[7]-law[3]*law[5] == D
            assert D < 0
            checks+=3
    for n in range(1,6):
        complete = list(combinations(range(n),2))
        for p in (Q(1,3),Q(1,2),Q(3,4)):
            law=exact_law(n,complete,p,Q(1))
            assert law[0]==1-p
            for mask in range(1,1<<n):
                k=mask.bit_count()
                assert law[mask] == Q(k,n)*p**k*(1-p)**(n-k)
                checks += 1
    for p in (Q(1,3),Q(1,2),Q(3,4)):
        for t in (Q(1,5),Q(1,2),Q(1)):
            for edges in ([],[(0,1)]):
                law=exact_law(2,edges,p,t)
                D=law[0]*law[3]-law[1]*law[2]
                assert D>=0
                if edges:
                    assert D==p*p*(1-p)*t**3*(4-(1-p)*t)/4
                else:
                    assert D==0
                checks+=2
    # All partial-order monotonicity checks on graphs of up to 3 vertices:
    # Advance one A potential clock, or delay one B potential clock.
    trials=0
    for n in (2,3):
        for edges in all_graphs(n):
            for order in permutations(range(2*n)):
                times=[None]*(2*n)
                for rank,token in enumerate(order):
                    times[token]=Q(rank)
                a,b=time_order_outcome(n,edges,times)
                for v in range(n):
                    if times[2*v]>0:
                        changed=times.copy()
                        changed[2*v]-=Q(3,2)
                        ap,bp=time_order_outcome(n,edges,changed)
                        assert (a & ~ap)==0 and (bp & ~b)==0
                        trials+=1
                    if times[2*v+1]<2*n-1:
                        changed=times.copy()
                        changed[2*v+1]+=Q(3,2)
                        ap,bp=time_order_outcome(n,edges,changed)
                        assert (a & ~ap)==0 and (bp & ~b)==0
                        trials+=1
    print('PASS: exact-law assertions',checks,'; monotone one-clock comparisons',trials)
    print('Triangle at p=1/2,t=1: mu(100)=1/24, mu(110)=mu(101)=1/12, mu(111)=1/8')
    print('Exact lattice-minor violation = -1/576.')

if __name__ == '__main__':
    test()
