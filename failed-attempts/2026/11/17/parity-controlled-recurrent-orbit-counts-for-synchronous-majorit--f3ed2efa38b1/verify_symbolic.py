"""Exact rational-polyhedral certificate for crown-graph majority dynamics.

All checks use integer Fourier--Motzkin elimination; no numerical solver is used.
A rational feasible system is a superset of the integer count vectors.
"""
import itertools
import math

TYPES = ((0, 0), (0, 1), (1, 0), (1, 1))


def next_pair(ca, cb, a, b):
    def h(category, x, y):
        return (0, x & (1-y), x | (1-y), 1)[category]
    return h(cb, a, b), h(ca, b, a)


def next_map(mp, ca, cb):
    return tuple(next_pair(ca, cb, *v) for v in mp)


def restrict_category(ineqs, score, cat):
    """score=2*number_of_ones-total_count; cat compares it to -1,+1."""
    if cat == 0:
        return ineqs + (score + (-3,),)
    if cat == 1:
        return ineqs + (score + (-1,), tuple(-v for v in score) + (1,))
    if cat == 2:
        return ineqs + (score + (1,), tuple(-v for v in score) + (-1,))
    return ineqs + (tuple(-v for v in score) + (-3,),)


def score(mp, coordinate):
    return tuple(2*pair[coordinate]-1 for pair in mp)


def normalize(row):
    g = 0
    for v in row:
        g = math.gcd(g, abs(v))
    return tuple(x // g for x in row) if g > 1 else tuple(row)


def rational_feasible(inequalities):
    """Check A*x<=b, x_j>=0 for four rational variables exactly."""
    rows = {normalize(row) for row in inequalities}
    rows.update(tuple(-int(i == j) for i in range(4)) + (0,) for j in range(4))
    for dimension in range(4, 0, -1):
        pos, neg, zero = [], [], set()
        pivot = dimension-1
        for row in rows:
            t = row[pivot]
            if t > 0:
                pos.append(row)
            elif t < 0:
                neg.append(row)
            else:
                zero.add(normalize(row[:pivot] + row[pivot+1:]))
        nxt = set(zero)
        for p in pos:
            for n in neg:
                u, v = p[pivot], -n[pivot]
                nxt.add(normalize(tuple(v*p[i] + u*n[i]
                                        for i in range(dimension+1) if i != pivot)))
        if any(all(z == 0 for z in row[:-1]) and row[-1] < 0 for row in nxt):
            return False
        rows = nxt
    return all(row[0] >= 0 for row in rows)


def extend(mp, constraints, ca, cb):
    r = restrict_category(restrict_category(constraints, score(mp, 0), ca), score(mp, 1), cb)
    if rational_feasible(r):
        return next_map(mp, ca, cb), r
    return None


def check_fifth_third():
    # At least three matched pairs: sum c_i >= 3.
    states = [(TYPES, ((-1,-1,-1,-1,-3),), (TYPES,))]
    counts = []
    for _ in range(5):
        successors = []
        for mp, conditions, history in states:
            for ca, cb in itertools.product(range(4), repeat=2):
                branch = extend(mp, conditions, ca, cb)
                if branch is not None:
                    mp2, conditions2 = branch
                    successors.append((mp2, conditions2, history + (mp2,)))
        states = successors
        counts.append(len(states))
    assert counts == [16, 30, 30, 30, 30], counts
    assert all(history[3] == history[5] for _, _, history in states)
    return counts


def check_only_uniform_two_cycle():
    # For F^2(x)=x with F(x)!=x, search all two-step threshold cells.
    # For atoms on which F^2 differs from identity, their multiplicity must be 0.
    # At least one changed atom must have multiplicity >=1.
    feasible = []
    checked = 0
    base = ((-1,-1,-1,-1,-3),)
    for ca, cb, da, db in itertools.product(range(4), repeat=4):
        mp1 = next_map(TYPES, ca, cb)
        mp2 = next_map(mp1, da, db)
        r = restrict_category(restrict_category(base,score(TYPES,0),ca),score(TYPES,1),cb)
        r = restrict_category(restrict_category(r,score(mp1,0),da),score(mp1,1),db)
        r = r + tuple(tuple(int(i==j) for i in range(4))+(0,)
                     for j in range(4) if mp2[j] != TYPES[j])
        for j in range(4):
            if mp1[j] == TYPES[j]:
                continue
            checked += 1
            r1 = r + (tuple(-int(i==j) for i in range(4))+(-1,),)
            if rational_feasible(r1):
                feasible.append(((ca,cb,da,db),j))
    assert checked == 608
    expected = [((0,3,3,0),1), ((3,0,0,3),2)]
    assert feasible == expected, feasible
    # These cell pairs send every state to opposite uniform shores,
    # so requiring F^2(x)=x forces the same uniform pair initially.
    return checked, feasible


if __name__ == '__main__':
    print('odd-shore F^5=F^3 exact certificate; branch counts:', check_fifth_third())
    checks, residual = check_only_uniform_two_cycle()
    print('odd-shore two-cycle certificate; tested cases:', checks)
    print('only feasible nonfixed cells:', residual)
    print('PASS')
