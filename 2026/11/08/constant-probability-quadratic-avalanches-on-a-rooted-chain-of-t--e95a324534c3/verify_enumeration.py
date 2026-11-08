"""Exhaustive stationary-state and avalanche checks for the rooted triangular cactus path.

Run: python verify_enumeration.py
Only the Python standard library is required.
"""
from fractions import Fraction
from itertools import product

BLOCKS = ((1, 1), (1, 0), (0, 1))


def adjacency(k):
    g = [set() for _ in range(2*k+1)]
    for i in range(1, k+1):
        for x, y in ((i-1, i), (i-1, k+i), (i, k+i)):
            g[x].add(y); g[y].add(x)
    return g


def code_height(code, k):
    h = [0] * (2*k+1)
    for i, (a, b) in enumerate(code, 1):
        h[i] = a + (2 if i < k else 0)
        h[k+i] = b
    return h


def burning_test(h, g):
    unburned = set(range(1, len(g)))
    while True:
        can_burn = {u for u in unburned if h[u] >= len(g[u] & unburned)}
        if not can_burn:
            return not unburned
        unburned.difference_update(can_burn)


def topple(h, g, source):
    height = h[:]
    height[source] += 1
    odometer = [0]*len(g)
    while True:
        active = next((u for u in range(1,len(g)) if height[u]>=len(g[u])),None)
        if active is None:
            return odometer, height
        odometer[active] += 1
        height[active] -= len(g[active])
        for v in g[active]:
            if v != 0:
                height[v] += 1


def exhaustive_recurrent_count(k, g):
    degrees = [len(g[i]) for i in range(1, 2*k+1)]
    total = 0
    for digits in product(*[range(d) for d in degrees]):
        if burning_test([0, *digits], g):
            total += 1
    return total


def run():
    for k in range(1, 10):
        g = adjacency(k)
        num = max_count = total_mass = 0
        for code in product(BLOCKS, repeat=k):
            h = code_height(code, k)
            assert burning_test(h, g), ('not recurrent', k, code)
            odo, final = topple(h, g, k)
            assert burning_test(final, g), ('final nonrecurrent', k, code)
            total = sum(odo)
            maximum = 2*k*k + k - 1
            assert total <= maximum, (k, code, total)
            should_be_max = code[-1] == (1,1) if k == 1 else code[-2:] == ((1,1),(1,1))
            assert (total == maximum) == should_be_max, (k, code, total)
            num += 1
            total_mass += total
            max_count += (total == maximum)
        assert num == 3**k
        assert max_count == (1 if k==1 else 3**(k-2))
        assert Fraction(total_mass, num) == Fraction(2*k*k+k,3)
        if k <= 5:
            assert exhaustive_recurrent_count(k,g) == num, 'recurrent classification incomplete'
        print(f'k={k:2d} states={num:5d} largest={maximum:3d} max_count={max_count:4d} mean={Fraction(total_mass,num)} PASS')
    print('EXHAUSTIVE CHECKS PASSED')

if __name__ == '__main__':
    run()
