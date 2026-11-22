"""Independent walk-predecessor enumeration for the late survival polynomials.
Run: python check_walk.py
"""

def inspect(a):
    n, E = 2*a, a*(a+1)
    preds = [[] for _ in range(n)]
    # Two cycles share only the zero vertex.
    for L, start in ((a,1),(a+1,a)):
        nodes = [0] + list(range(start, start+L-1))
        for i in range(L):
            u,v = nodes[i], nodes[(i+1)%L]
            preds[v].append(u)
    # At time t, reach[v] is the set of original sites that can reach v in t steps.
    reach = [1 << v for v in range(n)]
    full = (1 << n)-1
    empirical = {}
    for t in range(E+1):
        if t >= E-a:
            survival = set()
            for sources in reach:
                missing = full ^ sources
                sub = missing
                while sub:
                    survival.add(sub)
                    sub = (sub-1) & missing
            empirical[t] = (len(survival),
                            sum(1 for z in survival if z.bit_count()==1),
                            sum(1 for z in survival if z.bit_count()==2),
                            max((z.bit_count() for z in survival),default=0))
        reach = [sum_mask(reach[u] for u in predecessors) for predecessors in preds]
    for k in range(1,a+1):
        expected = (3*k-2,2*k-1,k-1, 2 if k>1 else 1)
        assert empirical[E-k] == expected, (a,k,empirical[E-k],expected)
    assert empirical[E] == (0,0,0,0)
    return a,E


def sum_mask(masks):
    out = 0
    for mask in masks:
        out |= mask
    return out

if __name__ == '__main__':
    for a in range(2, 41):
        print('PASS', inspect(a))
