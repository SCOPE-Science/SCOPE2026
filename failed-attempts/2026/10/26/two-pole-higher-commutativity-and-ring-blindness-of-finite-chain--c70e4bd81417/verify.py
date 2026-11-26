"""Finite checks of higher commuting tuples for two finite chain-ring families."""
from itertools import product


def polynomial_product(x, y, p, length):
    """Multiply coefficient vectors encoded as integers in F_p[t]/(t^length)."""
    digits_x = [(x // p**i) % p for i in range(length)]
    digits_y = [(y // p**i) % p for i in range(length)]
    digits_z = [0] * length
    for i in range(length):
        for j in range(length - i):
            digits_z[i + j] = (digits_z[i + j] + digits_x[i] * digits_y[j]) % p
    return sum(a * p**i for i, a in enumerate(digits_z))


def check_case(p, length, maximum_arity, kind):
    order = p**length
    if kind == 'polynomial':
        table = [[polynomial_product(x, y, p, length)
                  for y in range(order)] for x in range(order)]
    else:
        table = [[x * y % order for y in range(order)] for x in range(order)]
    pairs = list(product(range(order), repeat=2))
    commute = [[table[a][d] == table[c][b] for c, d in pairs]
               for a, b in pairs]
    # Independently verify the pair condition using both group products.
    if kind == 'polynomial':
        def add(x, y):
            return sum((((x // p**i) % p + (y // p**i) % p) % p) * p**i
                       for i in range(length))
    else:
        def add(x, y):
            return (x + y) % order
    for i, (a, b) in enumerate(pairs):
        for j, (c, d) in enumerate(pairs):
            left = (add(a, c), add(b, d), table[a][d])
            right = (add(c, a), add(d, b), table[c][b])
            assert commute[i][j] == (left == right)
    cliques = [(i,) for i in range(len(pairs))]
    beta = (p**(length + 1) - 1) // (p - 1)
    assert len(cliques) == beta * p**length - (beta - 1) * p**(length - 1)
    for r in range(2, maximum_arity + 1):
        cliques = [tuple_ + (j,)
                   for tuple_ in cliques
                   for j in range(len(pairs))
                   if all(commute[j][i] for i in tuple_)]
        expected = beta * p**(length * r) - (beta - 1) * p**((length - 1) * r)
        assert len(cliques) == expected, (p, length, kind, r, len(cliques), expected)
    print(f'PASS {kind} p={p}, m={length}, r<= {maximum_arity}')


if __name__ == '__main__':
    for case in [(2, 2, 4, 'polynomial'), (2, 3, 3, 'polynomial'),
                 (2, 4, 2, 'polynomial'), (3, 2, 3, 'polynomial'),
                 (2, 2, 3, 'integer'), (3, 2, 3, 'integer')]:
        check_case(*case)
    print('VERIFY_OK')
