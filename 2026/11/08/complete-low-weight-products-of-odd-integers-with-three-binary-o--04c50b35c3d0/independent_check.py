"""Independent product-first divisor census with exact integer arithmetic."""
from math import isqrt

out = []
checks = 0
for weight, limit in ((2, 1 << 14), (3, 1 << 23)):
    # A qualifying odd product must have lowest bit 1.
    if weight == 2:
        products = [1 + (1 << j) for j in range(1, 14)]
    else:
        products = [1 + (1 << i) + (1 << j)
                    for j in range(2, 23) for i in range(1, j)]
    assert len(products) == (13 if weight == 2 else 231)
    rows = []
    for z in products:
        assert z < limit and z.bit_count() == weight
        # a<=b, and each factor is odd of weight three, hence a>=7.
        for a in range(7, isqrt(z) + 1, 2):
            if a.bit_count() != 3:
                continue
            checks += 1
            if z % a == 0:
                b = z // a
                if b.bit_count() == 3:
                    rows.append((a, b, z))
    rows.sort()
    print(f'weight={weight}: tested_products={len(products)}, rows={rows}')
    out.extend((weight, *row) for row in rows)
assert sorted(out) == sorted([
    (2, 25, 41, 1025),
    (3, 7, 7, 49), (3, 7, 19, 133), (3, 7, 37, 259),
    (3, 11, 35, 385), (3, 13, 21, 273), (3, 21, 49, 1029)])
print(f'exact trial divisions: {checks}')
print('INDEPENDENT_CHECK_OK')
