"""Exact four-support census for open neighborhoods in the Paley graph at 25."""
from itertools import combinations


def label(a, b):
    return (a % 5) + 5 * (b % 5)


def square(a, b):
    return (a*a - 2*b*b) % 5 in (1, 4)


def image(x, s, c, sign):
    a, b = x % 5, sign * (x // 5)
    d, e = s % 5, s // 5
    return label(d*a + 2*e*b + c % 5, e*a + d*b + c // 5)


def verify():
    vertices = range(25)
    square_scales = tuple(s for s in vertices if square(s % 5, s // 5))
    assert len(square_scales) == 12
    adj = tuple(tuple(square(x % 5 - y % 5, x // 5 - y // 5)
                      for x in vertices) for y in vertices)
    assert all(sum(row) == 12 and not row[y] for y, row in enumerate(adj))
    supports = 0
    remaining = set()
    for support in combinations(vertices, 4):
        supports += 1
        traces = {sum(1 << j for j, x in enumerate(support) if row[x])
                  for row in adj}
        if len(traces) == 16:
            remaining.add(support)
    assert supports == 12650 and len(remaining) == 3600

    maps = {tuple(image(x, s, c, sign) for x in vertices)
            for s in square_scales for c in vertices for sign in (1, -1)}
    assert len(maps) == 600
    profile = []
    while remaining:
        representative = min(remaining)
        images = [tuple(sorted(f[x] for x in representative)) for f in maps]
        orbit = set(images)
        assert orbit <= remaining
        stabilizer = images.count(representative)
        assert stabilizer * len(orbit) == 600
        profile.append((representative, len(orbit), stabilizer))
        remaining.difference_update(orbit)

    expected = [((0, 1, 2, 5), 600, 1), ((0, 1, 2, 8), 600, 1),
                ((0, 1, 5, 6), 150, 4), ((0, 1, 5, 11), 600, 1),
                ((0, 1, 5, 15), 600, 1), ((0, 1, 5, 23), 600, 1),
                ((0, 1, 8, 15), 300, 2), ((0, 1, 10, 11), 150, 4)]
    assert profile == expected
    for row in profile:
        print(*row)
    print(f'VERIFY_OK supports={supports} shattered={sum(s for _, s, _ in profile)} orbits={len(profile)}')


if __name__ == '__main__':
    verify()
