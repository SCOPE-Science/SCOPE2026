"""Independent bit-level majority-step simulator for balanced complete multipartite graphs.

Run: python verify_balanced_multipartite_direct.py
Uses no external packages.
"""
from math import comb


def formula(r, n):
    center = comb(n, n // 2) if n % 2 == 0 else 0
    fixed = 2 + (center ** r if n % 2 == 0 else 0)
    two = (comb(r, r // 2) if r % 2 == 0
           else r * comb(r - 1, (r - 1) // 2) * (2 ** n - 2))
    if n % 2 == 0:
        for uniform_parts in range(2, r - 1, 2):
            two += (comb(r, uniform_parts) * comb(uniform_parts, uniform_parts // 2)
                    * center ** (r - uniform_parts))
    return fixed, two


def bit_level_census(r, n):
    vertices = r * n
    neighbor_masks = []
    for vertex in range(vertices):
        part = vertex // n
        mask = 0
        for other in range(vertices):
            if other // n != part:
                mask |= (1 << other)
        neighbor_masks.append(mask)
    degree = (r - 1) * n

    def step(state):
        result = 0
        for vertex, mask in enumerate(neighbor_masks):
            ones = (state & mask).bit_count()
            if 2 * ones > degree or (2 * ones == degree and (state >> vertex) & 1):
                result |= 1 << vertex
        return result

    fixed = two = 0
    for state in range(1 << vertices):
        first = step(state)
        if first == state:
            fixed += 1
        elif step(first) == state:
            two += 1
    return fixed, two


def main():
    parameters = [(4, 1), (4, 2), (4, 3), (4, 4),
                  (5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (7, 1), (7, 2)]
    examined = 0
    for r, n in parameters:
        direct = bit_level_census(r, n)
        predicted = formula(r, n)
        assert direct == predicted, (r, n, direct, predicted)
        examined += 2 ** (r * n)
        print(f'r={r}, n={n}: fixed={direct[0]}, primitive_two={direct[1]}')
    print(f'PASS: {len(parameters)} direct parameter cases; {examined} labelled states examined')


if __name__ == '__main__':
    main()
