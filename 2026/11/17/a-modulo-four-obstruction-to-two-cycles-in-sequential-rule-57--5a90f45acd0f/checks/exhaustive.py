"""Directly enumerate fixed points of two successive in-place Rule 57 sweeps.
Run: python3 checks/exhaustive.py
"""

def update(word, n):
    bits = [(word >> j) & 1 for j in range(n)]
    for i in range(n):
        l, c, r = bits[(i-1) % n], bits[i], bits[(i+1) % n]
        bits[i] = (57 >> (4*l + 2*c + r)) & 1
    return sum(bit << j for j, bit in enumerate(bits))


def classified(word,n):
    if n % 4 != 2:
        return False
    first, second = word & 1, (word >> 1) & 1
    return all(((word >> i) & 1) == (
        (first,second,1-first,1-second)[i % 4]) for i in range(n))

for n in range(3, 18):
    found = 0
    for word in range(1 << n):
        new = update(word,n)
        agrees = update(new,n) == word
        assert agrees == classified(word,n), (n,word)
        if agrees:
            assert new != word
            assert new == word ^ ((1 << n) - 1)
            found += 1
    assert found == (4 if n % 4 == 2 else 0)
    print(f'n={n:2d} fixed_second_iterate={found} primitive_two_orbits={found//2}')
print('ALL EXHAUSTIVE CHECKS PASSED')
