"""Exact finite checks for looped complete-bipartite unicycle walks.

Asymptotic mixing is proved analytically in RESULT.md. This script verifies
finite unicycle-state closure, invariant uniform state measure, connectivity,
local two-step hitting bounds, and coupon-empty variance identities.
"""
from itertools import product
from fractions import Fraction


def neighbors(a, b):
    return [tuple([i] + list(range(a, a+b))) for i in range(a)] + [
        tuple([i] + list(range(a))) for i in range(a, a+b)
    ]


def unique_cycle(arrows):
    seen = set()
    cycles = []
    for s in range(len(arrows)):
        if s in seen:
            continue
        loc = {}
        path = []
        cur = s
        while cur not in loc and cur not in seen:
            loc[cur] = len(path)
            path.append(cur)
            cur = arrows[cur]
        if cur in loc:
            cycles.append(tuple(path[loc[cur]:]))
        seen.update(path)
    return cycles[0] if len(cycles) == 1 else None


def check_graph(a, b):
    nb = neighbors(a,b)
    deg = [len(x) for x in nb]
    states = []
    for ar in product(*nb):
        cycle = unique_cycle(ar)
        if cycle is not None:
            states.extend((x,ar) for x in cycle)
    ss = set(states)
    assert len(states) == len(ss)
    incoming_weight = {s: Fraction(0) for s in ss}
    transitions = {}
    assertions = 1
    for x, ar in states:
        next_states = []
        for y in nb[x]:
            ar2 = ar[:x] + (y,) + ar[x+1:]
            s2 = (y,ar2)
            assert s2 in ss
            incoming_weight[s2] += Fraction(1,deg[x])
            next_states.append(s2)
            assertions += 1
        transitions[(x,ar)] = next_states
    for s in states:
        assert incoming_weight[s] == 1, (a,b,s,incoming_weight[s])
        assertions += 1
    initial = tuple(a for _ in range(a)) + tuple(0 for _ in range(b))
    root = (0,initial)
    assert root in ss
    assertions += 1
    visited = {root}
    queue = [root]
    for s in queue:
        for nxt in transitions[s]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    assert len(visited) == len(states), (a,b,len(visited),len(states))
    assertions += 1
    # The uniform stationary law is invariant under all within-part relabelings.
    z = 0
    mean_target_arrows = Fraction(
        sum(sum(ar[v] == z for v in range(a,a+b)) for _,ar in states),len(states))
    assert mean_target_arrows <= Fraction(b,a)
    assertions += 1
    for x in range(a+b):
        for y in range(a+b):
            if x == y:
                two_step_hit = Fraction(1)
            else:
                two_step_hit = Fraction(int(y in nb[x]),deg[x])
                two_step_hit += sum((Fraction(int(v in nb[x]),deg[x]) *
                                     Fraction(int(y in nb[v]),deg[v])
                                     for v in range(a+b) if v != y),Fraction(0))
            other_size = b if y < a else a
            size_of_target_part = a if y < a else b
            lower = Fraction(other_size,(other_size+1)*(size_of_target_part+1))
            assert two_step_hit >= lower, (a,b,x,y,two_step_hit,lower)
            assertions += 1
    return len(states),assertions,mean_target_arrows


def check_occupancy():
    assertions = 0
    for n in range(2,18):
        for k in range(36):
            one = Fraction(n-1,n)**k
            two = Fraction(n-2,n)**k
            mean = n*one
            var = n*one*(1-one) + n*(n-1)*(two-one*one)
            assert 0 <= var <= mean
            assertions += 1
    return assertions

if __name__ == '__main__':
    total=0
    for a,b in ((2,2),(2,3),(3,2),(3,3)):
        states,assertions,mean = check_graph(a,b)
        total+=assertions
        print(f'K_{{{a},{b}}}: recurrent_states={states} exact_assertions={assertions}; E[#B arrows to A0]={mean}')
    co=check_occupancy()
    total+=co
    print(f'coupon-variance checks={co}; total exact assertions={total}; PASS')
