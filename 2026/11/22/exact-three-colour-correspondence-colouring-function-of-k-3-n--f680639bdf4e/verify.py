"""Independent small exact enumeration of the three-fold cover minima."""
from itertools import combinations_with_replacement, permutations, product

perms = list(permutations(range(3)))
triples = list(product(range(3), repeat=3))
factors = []
for p in perms:
    for q in perms:
        factors.append(tuple(3 - len({x, p[y], q[z]})
                             for (x,y,z) in triples))
assert len(factors) == 36
expected = [(24,1,1),(18,2,36),(14,18,666),(6,6,8436),
            (5,180,82251),(0,60,658008)]
for n in range(1,7):
    best = 1000000
    count_min = 0
    tests = 0
    for others in combinations_with_replacement(range(36),n-1):
        tests += 1
        total = 0
        for j in range(27):
            term = factors[0][j]
            for i in others:
                term *= factors[i][j]
                if term == 0:
                    break
            total += term
            if total > best:
                break
        if total < best:
            best, count_min = total, 1
        elif total == best:
            count_min += 1
    assert (best,count_min,tests) == expected[n-1]
    print(f'n={n}: {best}, minimum_tuples={count_min}, tested={tests}, PASS')
print('VERIFY_OK')
