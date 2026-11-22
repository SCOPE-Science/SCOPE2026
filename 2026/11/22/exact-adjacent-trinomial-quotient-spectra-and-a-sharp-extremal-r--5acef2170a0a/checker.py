"""Standalone exact checker for the ternary multinomial quotient spectrum."""
from math import comb


def digit_formula(p, r):
    q = comb(p + 2, 3)
    z = sum(q ** j for j in range(r))
    weights = {}
    for u in range(1, p):
        weights[u] = sum(max(0, p + 1 - (u * y) % p - y) for y in range(1, p))
    return {u: z * count for u, count in weights.items()}


def brute_force(p, r):
    cap = p ** r
    obs = {u: 0 for u in range(1, p)}
    for n in range(1, cap):
        for a in range(1, n + 1):
            choose_a = comb(n, a)
            for b in range(n-a+1):
                c = n - a - b
                original = choose_a * comb(n-a, b)
                if original % p == 0:
                    continue
                neighbor = comb(n, a-1) * comb(n-a+1, b+1)
                if neighbor % p == 0:
                    continue
                u = (neighbor % p) * pow(original % p, -1, p) % p
                obs[u] += 1
    return obs


def verify():
    count = 0
    for p, depths in [(2, (1,2,3)), (3,(1,2,3)), (5,(1,2,3)), (7,(1,2)), (11,(1,))]:
        for r in depths:
            calc = brute_force(p,r)
            formula = digit_formula(p,r)
            assert calc == formula, (p,r,calc,formula)
            count += sum(calc.values())
        if p >= 5:
            n = {u: digit_formula(p,1)[u] for u in range(1,p)}
            assert n[p-1] == p-1 and n[1] == (p*p-1)//4
            assert all(n[p-1] < n[u] < n[1] for u in range(2,p-1))
    print('CHECK_OK; exact accepted tuples:', count)

if __name__ == '__main__':
    verify()
