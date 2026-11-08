"""Exact 2-by-2 matching and tie-break risk certificate (Python standard library).

Preferences are 0 = strictly favor partner 0, 1 = strictly favor partner 1,
2 = indifferent; refinement policy is a four-bit vector in order w0,w1,f0,f1.
All participants rank both partners above being unmatched.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def refined_preference(original, bit):
    first = bit if original == 2 else original
    return (first, 1 - first)


def worker_da(orders):
    """Worker-proposing deferred acceptance: output partner worker of each firm."""
    held = [None, None]
    next_choice = [0, 0]
    free = [0, 1]
    while free:
        w = free.pop(0)
        assert next_choice[w] < 2
        f = orders[w][next_choice[w]]
        next_choice[w] += 1
        if held[f] is None:
            held[f] = w
        elif orders[2 + f].index(w) < orders[2 + f].index(held[f]):
            free.append(held[f])
            held[f] = w
        else:
            free.append(w)
    return tuple(held)


def is_stable(match, orders):
    for w in (0, 1):
        own_f = match.index(w)
        for f in (0, 1):
            if f != own_f and orders[w][0] == f and orders[2 + f][0] == w:
                return False
    return True


def is_pareto_dominated(match, weak):
    other = (match[1], match[0])
    strict = False
    for w in (0, 1):
        original = match.index(w)
        alternate = other.index(w)
        if weak[w] != 2:
            if alternate != weak[w]:
                return False
            strict = True
    for f in (0, 1):
        if weak[2 + f] != 2:
            if other[f] != weak[2 + f]:
                return False
            strict = True
    return strict


def run():
    counts = {}
    num_checks = 0
    for bits in product((0, 1), repeat=4):
        by_ties = Counter()
        for weak in product((0, 1, 2), repeat=4):
            orders = tuple(refined_preference(weak[i], bits[i]) for i in range(4))
            match = worker_da(orders)
            assert sorted(match) == [0, 1]
            # Second, independently enumerative characterization of DA on two matchings.
            stable = [m for m in ((0, 1), (1, 0)) if is_stable(m, orders)]
            assert match in stable
            assert all(orders[w].index(match.index(w)) <= orders[w].index(alt.index(w))
                       for alt in stable for w in (0, 1))
            if is_pareto_dominated(match, weak):
                by_ties[weak.count(2)] += 1
            num_checks += 1
        counts[bits] = (by_ties[2], by_ties[3])
        assert not any(by_ties[k] for k in (0, 1, 4))

    best = [b for b, c in counts.items() if c == (1, 2)]
    mid = [b for b, c in counts.items() if c == (2, 3)]
    worst = [b for b, c in counts.items() if c == (3, 4)]
    assert (len(best), len(mid), len(worst)) == (10, 4, 2)
    assert {''.join(map(str, b)) for b in best} == {
        '0000','0001','0010','0011','0110','1001','1100','1101','1110','1111'}
    assert {''.join(map(str, b)) for b in mid} == {'0100','0111','1000','1011'}
    assert {''.join(map(str, b)) for b in worst} == {'0101','1010'}

    def prob_at(t, pair):
        a, b = pair
        return Fraction(a, 4) * t * t * (1-t)**2 + Fraction(b, 2) * t**3 * (1-t)
    for t in (Fraction(0), Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        weighted = sum((prob_at(t, count) for count in counts.values()), Fraction()) / 16
        target = t * t * (1-t) * (7*t+3) / 8
        assert weighted == target, (t, weighted, target)
        opt = t*t*(1-t)*(3*t+1)/4
        assert all(prob_at(t, count) >= opt for count in counts.values())
        assert prob_at(t, counts[(0, 0, 0, 0)]) == opt
        print('t=', t, 'independent=',weighted, 'optimal=', opt)

    # Every member of a fully anonymous, unbiased common-priority policy is optimal.
    assert all(counts[b] == (1, 2) for b in
               ((0,0,0,0),(0,0,1,1),(1,1,0,0),(1,1,1,1)))
    print('verified exact profiles=', num_checks, 'policy vectors=', len(counts))
    print('class counts [best,mid,worst]=', len(best),len(mid),len(worst))
    for b in sorted(counts):
        print(''.join(map(str,b)), counts[b])
    return True


if __name__ == '__main__':
    run()
