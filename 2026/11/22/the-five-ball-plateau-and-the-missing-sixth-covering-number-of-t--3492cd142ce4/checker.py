"""Exact rational triangular certificates for two torus-covering configurations.
Run with python3 checker.py; no third-party packages required.
"""
from fractions import Fraction as Q


def verify(label, centers, radius, denominator, orientation_rows):
    assert len(orientation_rows) == denominator
    assert all(len(row) == denominator for row in orientation_rows)
    assert all(symbol in '/\\' for row in orientation_rows for symbol in row)
    tested = 0
    for i, row in enumerate(orientation_rows):
        for j, symbol in enumerate(row):
            a = (Q(i, denominator), Q(j, denominator))
            b = (Q(i + 1, denominator), Q(j, denominator))
            c = (Q(i + 1, denominator), Q(j + 1, denominator))
            d = (Q(i, denominator), Q(j + 1, denominator))
            triangles = ([a, b, c], [a, c, d]) if symbol == '/' else ([a, b, d], [b, c, d])
            for triangle in triangles:
                possible = []
                for idx, (cx, cy) in enumerate(centers):
                    for sx in (-1, 0, 1):
                        for sy in (-1, 0, 1):
                            if all(abs(x - cx - sx) + abs(y - cy - sy) <= radius for x, y in triangle):
                                possible.append((idx, sx, sy))
                assert possible, (label, i, j, symbol, triangle)
                tested += 1
    print(label, 'covered:', denominator ** 2, 'square cells,', tested, 'triangles, exact rational')
    return tested


def main():
    four = [(Q(0), Q(0)), (Q(1, 2), Q(0)), (Q(1, 4), Q(1, 2)), (Q(3, 4), Q(1, 2))]
    five = [(Q(0), Q(0)), (Q(1, 3), Q(1, 3)), (Q(2, 3), Q(1, 3)), (Q(0), Q(2, 3)), (Q(1, 2), Q(5, 6))]
    four_rows = (
        '//\\/////',
        '/\\//////',
        '//////\\/',
        '/////\\//',
        '//\\/////',
        '/\\//////',
        '//////\\/',
        '/////\\//',
    )
    five_rows = (
        '/\\////',
        '\\///\\/',
        '///\\//',
        '\\/////',
        '///\\/\\',
        '//\\///',
    )
    assert verify('four centers', four, Q(3, 8), 8, four_rows) == 128
    assert verify('five centers', five, Q(1, 3), 6, five_rows) == 72
    print('All 200 rational triangle inclusion certificates passed.')


if __name__ == '__main__':
    main()
