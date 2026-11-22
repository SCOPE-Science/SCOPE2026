"""Independent, standard-library check of the local wave timing lemma and samples.

Usage: python3 verify_local.py
No other files needed.
"""
from itertools import product
from random import Random


def histories_for_child(t):
    # Arbitrary input, except its final 1 forbids a 1 one or two updates earlier.
    for prefix in product(range(3), repeat=t - 3):
        for a in (0, 2):
            for b in (0, 2):
                yield prefix + (a, b, 1)


def drive(vertex_initial, children, parent):
    t = len(parent)
    x = vertex_initial
    penultimate = None
    for s in range(t):
        if s == t - 1:
            penultimate = x
        if x == 1:
            x = 2
        elif x == 2:
            x = 0
        else:
            x = int(sum(c[s] == 1 for c in children) + (parent[s] == 1) >= len(children))
    return penultimate, x


def exhaust_local(t, branching):
    count = 0
    valid_child_sequences = list(histories_for_child(t))
    for children in product(valid_child_sequences, repeat=branching):
        for parent in product(range(3), repeat=t):
            for initial in range(3):
                penultimate, final = drive(initial, children, parent)
                assert (penultimate, final) == (0, 1), (t, branching, initial, children, parent)
                count += 1
    return count


def tree_random_check(b, h, samples, rng):
    n = sum(b ** d for d in range(h + 1))
    depths = [0] * n
    for i in range(1, n):
        depths[i] = depths[(i - 1) // b] + 1
    for _ in range(samples):
        x = []
        for d in depths:
            rem = h - d
            if rem == 0:
                x.append(1)
            elif rem == 1:
                x.append(0)
            elif rem == 2:
                x.append(rng.choice([0, 2]))
            else:
                x.append(rng.randrange(3))
        for _ in range(h):
            nxt = []
            for i, state in enumerate(x):
                if state:
                    nxt.append((state + 1) % 3)
                else:
                    neighbors = ([] if i == 0 else [(i - 1) // b])
                    neighbors += list(range(b * i + 1, min(b * i + b + 1, n)))
                    nxt.append(int(sum(x[v] == 1 for v in neighbors) >= b))
            x = nxt
        assert x[0] == 1
    return n


if __name__ == '__main__':
    for t, b in [(3, 2), (4, 2), (5, 2), (3, 3), (4, 3)]:
        cnt = exhaust_local(t, b)
        print(f"local_t={t} branching={b} adversarial_inputs={cnt} PASS")
    rng = Random(26004)
    for b in range(2, 6):
        for h in range(2, 7):
            n = tree_random_check(b, h, 70, rng)
            print(f"tree_branching={b} height={h} vertices={n} samples=70 PASS")
    print('ALL LOCAL AND RANDOMIZED TREE CHECKS PASSED')
