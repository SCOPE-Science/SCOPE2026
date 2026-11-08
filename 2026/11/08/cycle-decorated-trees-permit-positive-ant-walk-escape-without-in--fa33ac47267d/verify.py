"""Finite, exact independent checks for a monotone event in a directed-edge reinforced walk.

The proof of the infinite product and its convergence is mathematical, not numerical.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product
from collections import defaultdict


def gate(path):
    return (tuple(path), 'gate')


def build(level_branching, cycle_lengths=None):
    adj = defaultdict(set)
    if cycle_lengths is None:
        cycle_lengths = (3,) * (len(level_branching) + 1)
    assert len(cycle_lengths) == len(level_branching) + 1
    assert all(x>=3 for x in cycle_lengths)
    def add_cycle(path, length):
        vertices=[gate(path)] + [(path, "cycle", k) for k in range(1,length)]
        for k in range(length):
            u, v = vertices[k], vertices[(k+1)%length]
            adj[u].add(v)
            adj[v].add(u)
    paths = [()]
    for depth, count in enumerate(level_branching):
        next_paths = []
        for path in paths:
            g=gate(path)
            add_cycle(path, cycle_lengths[depth])
            for j in range(count):
                child = path + (j,)
                gc = gate(child)
                adj[g].add(gc)
                adj[gc].add(g)
                next_paths.append(child)
        paths = next_paths
    # Install cycles at the last frontier too.
    for path in paths:
        add_cycle(path, cycle_lengths[-1])
    return adj


def exact_next(adj, visited_path, lam):
    """lam=exp(-beta); for integer crossing counts weights are lam**(-count)."""
    current = visited_path[-1]
    directed = defaultdict(int)
    for u, v in zip(visited_path, visited_path[1:]):
        directed[(u,v)] += 1
        directed[(v,u)] -= 1
    weights = {v: lam ** (-directed[(current, v)]) for v in adj[current]}
    total = sum(weights.values(), Fraction(0))
    return {v: w / total for v,w in weights.items()}


def explicit_test(branching, lam, lengths=None):
    adj=build(branching, lengths)
    for u in adj:
        assert len(adj[u]) > 0
        assert sum(1 for a in adj[u] if a[0] == u[0]) == 2, u
    root=gate(())
    correct=Fraction(branching[0],branching[0]+2)
    for b in branching[1:]:
        correct *= Fraction(b, 1) / (b + 2 + lam)
    total=Fraction(0)
    checks=0
    for choices in product(*(range(b) for b in branching)):
        path=[root]
        factor=Fraction(1)
        prev=()
        for d, j in enumerate(choices):
            newpath=prev+(j,)
            target=gate(newpath)
            dist=exact_next(adj,path,lam)
            expected=Fraction(1,1)/(branching[d]+2+(lam if d else 0))
            assert dist[target] == expected
            # The probability of an arbitrary child of this gate is equal.
            assert sum(dist[gate(prev+(q,))] for q in range(branching[d])) == branching[d]*expected
            factor*=dist[target]
            path.append(target)
            prev=newpath
            checks+=2
        total+=factor
    assert total==correct,(total,correct)
    checks+=1
    return checks, total


def run():
    tests=0
    for b in [(1,1,1), (2,3,5), (4,2,3), (4,8,16)]:
        for lam in (Fraction(1,2),Fraction(1,4),Fraction(1,1)):
            count,prob=explicit_test(b,lam)
            print('exact graph',b,'reverse weight',lam,'event probability',prob,'checks',count)
            tests+=count
    for lengths in ((3, 4, 5, 6), (9, 3, 7, 4)):
        for lam in (Fraction(1, 2), Fraction(1, 4)):
            count, prob = explicit_test((2,3,5),lam,lengths)
            print("variable cycle lengths", lengths, "reverse weight", lam, "event probability", prob,"checks",count)
            tests += count
    # Infinite positive-event example: b_i=2**(i+2), i>=0.
    getcontext().prec=60
    lower = Decimal(2)/Decimal(3)*(-Decimal(3)/Decimal(4)).exp()
    assert lower > Decimal('0.3148')
    for lam in (Fraction(1,2), Fraction(1,10), Fraction(1,1)):
        val=Fraction(2,3)
        for i in range(1,40):
            b=2**(i+2)
            val*=Fraction(b,1)/(b+2+lam)
            assert Decimal(val.numerator)/Decimal(val.denominator)>lower
            tests+=1
    print('uniform proved lower bound',lower)
    print('PASS',tests,'exact probability / structural / bound checks')


if __name__=='__main__':
    run()
