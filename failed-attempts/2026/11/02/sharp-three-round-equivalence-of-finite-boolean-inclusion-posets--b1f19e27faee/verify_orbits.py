"""Complete orbit-based rank-three EF computation for finite powerset inclusion posets."""
from functools import lru_cache
from itertools import product

ids = {}
def intern(value):
    if value not in ids:
        ids[value] = len(ids) + 1
    return ids[value]

def diagram(cells):
    k = len(cells).bit_length() - 1
    return tuple(int(not any(cells[s] and (s & (1 << i)) and not (s & (1 << j))
                             for s in range(1 << k))) for i in range(k) for j in range(k))

@lru_cache(None)
def ef_type(cells, remaining):
    if remaining == 0:
        return intern((0, diagram(cells)))
    k = len(cells).bit_length() - 1
    child_types = set()
    for split in product(*(range(c + 1) for c in cells)):
        child = tuple(c - s for c, s in zip(cells, split)) + tuple(split)
        child_types.add(ef_type(child, remaining - 1))
    return intern((remaining, diagram(cells), tuple(sorted(child_types))))

if __name__ == '__main__':
    signatures = [ef_type((n,), 3) for n in range(1, 13)]
    print('n=1..12 rank-3 canonical type identifiers:', signatures)
    assert len(set(signatures[:6])) == 6, 'six boundary theories must be distinct'
    assert all(s == signatures[5] for s in signatures[6:]), 'finite tail does not agree'
    print('ORBIT_RANK3_FINITE_PASS')
