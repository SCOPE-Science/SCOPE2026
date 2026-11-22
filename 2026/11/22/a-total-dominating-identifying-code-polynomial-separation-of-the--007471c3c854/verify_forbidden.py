"""Independent exact census by generating all forbidden downsets (not signatures)."""
from collections import Counter
from hashlib import sha256
from math import comb

EXPECTED = {
    "rook": (1056, 5520, 10170, 10800, 7944, 4368, 1820, 560, 120, 16, 1),
    "shrikhande": (1040, 5584, 10206, 10800, 7944, 4368, 1820, 560, 120, 16, 1),
}
FULL = (1 << 16) - 1


def adjacency(kind):
    a = [0] * 16
    for v in range(16):
        y, x = divmod(v, 4)
        for w in range(16):
            yy, xx = divmod(w, 4)
            if kind == "rook":
                is_edge = (y == yy or x == xx) and v != w
            else:
                diffs = ((yy-y) & 3, (xx-x) & 3)
                is_edge = diffs in ((1, 0), (3, 0), (0, 1),
                                    (0, 3), (1, 1), (3, 3))
            if is_edge:
                a[v] |= (1 << w)
    return a


def count_codes(kind):
    open_masks = adjacency(kind)
    closed_masks = [open_masks[v] | (1 << v) for v in range(16)]
    # A set fails total domination or closed-neighborhood separation precisely
    # when it is contained in one of these 136 complementary witness sets.
    bad_caps = [FULL ^ x for x in open_masks]
    bad_caps += [FULL ^ (closed_masks[v] ^ closed_masks[w])
                 for v in range(16) for w in range(v + 1, 16)]
    assert len(bad_caps) == 136
    sizes = Counter(x.bit_count() for x in bad_caps)
    assert sizes == {10: 64, 6: 72}, sizes
    tops = [x for x in bad_caps if x.bit_count() == 10]
    assert len(set(tops)) == 64
    assert max((a & b).bit_count() for i, a in enumerate(tops)
               for b in tops[i + 1:]) <= 8
    excluded = bytearray(1 << 16)
    for cap in bad_caps:
        sub = cap
        while True:
            excluded[sub] = 1
            if sub == 0:
                break
            sub = (sub - 1) & cap
    code_bitmap = bytes(1 - x for x in excluded)
    counts = Counter(mask.bit_count() for mask, ok in enumerate(code_bitmap) if ok)
    coeffs = tuple(counts[k] for k in range(6, 17))
    assert coeffs == EXPECTED[kind], (kind, coeffs)
    # The 64 distinct maximal bad 10-sets have disjoint nine-set shadows.
    assert counts[10] == comb(16, 10) - 64
    assert counts[9] == comb(16, 9) - 64 * 10
    for k in range(11, 17):
        assert counts[k] == comb(16, k)
    print(kind, "forbidden_caps_size_distribution", dict(sizes))
    print(kind, "polynomial", sorted(counts.items()))
    print(kind, "membership_bitmap_sha256", sha256(code_bitmap).hexdigest())
    return code_bitmap

if __name__ == "__main__":
    x, y = count_codes("rook"), count_codes("shrikhande")
    assert x != y
    print("FORBIDDEN_DOWNSET_PASS")
