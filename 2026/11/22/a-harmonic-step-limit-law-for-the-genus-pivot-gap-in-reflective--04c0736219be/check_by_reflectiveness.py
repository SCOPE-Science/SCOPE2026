"""Bounded histogram check using the definition of a reflective semigroup."""

from collections import Counter


def direct_histogram(genus):
    counts = Counter()
    for mask in range(1 << (genus - 1)):
        gaps = {genus}
        for i in range(1, genus):
            gaps.add(i if mask & (1 << (i - 1)) else i + genus)
        nongaps = [i for i in range(1, 2 * genus) if i not in gaps]
        if any(a + b in gaps for a in nongaps for b in nongaps if a + b < 2 * genus):
            continue
        lo = hi = genus
        while lo - 1 in gaps:
            lo -= 1
        while hi + 1 in gaps:
            hi += 1
        counts[hi - lo + 1] += 1
    return counts


def divisor_histogram(genus):
    counts = Counter({genus: 1})
    for t in range(1, genus):
        count = sum((genus - t) % a == 0 for a in range(t + 1, genus + 1))
        if count:
            counts[t] = count
    return counts


for genus in range(1, 15):
    actual = direct_histogram(genus)
    assert actual == divisor_histogram(genus), (genus, actual)
    if genus == 12:
        print(dict(sorted(actual.items())))
print('All genera 1 through 14 matched.')
