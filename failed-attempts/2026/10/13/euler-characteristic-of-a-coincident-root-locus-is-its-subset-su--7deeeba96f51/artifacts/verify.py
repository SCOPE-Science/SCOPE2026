def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for tail in partitions(n-first, first):
            yield (first,) + tail

def subset_sums_dp(lam):
    sums = {0}
    for a in lam:
        sums |= {s+a for s in tuple(sums)}
    return sums

def subset_sums_bruteforce(lam):
    out = set()
    e = len(lam)
    for mask in range(1 << e):
        s = 0
        for i, a in enumerate(lam):
            if mask & (1 << i):
                s += a
        out.add(s)
    return out

def complete_criterion(lam):
    a = sorted(lam)
    if not a or a[0] != 1:
        return False
    reach = 1
    for x in a[1:]:
        if x > reach + 1:
            return False
        reach += x
    return True

partition_checks = exhaustive_checks = criterion_checks = 0
total_fixed_points = 0

for d in range(1, 31):
    for lam in partitions(d):
        sums = subset_sums_dp(lam)
        assert 0 in sums and d in sums
        assert all(0 <= s <= d for s in sums)
        total_fixed_points += len(sums)
        partition_checks += 1

        assert (len(sums) == d + 1) == complete_criterion(lam)
        criterion_checks += 1

        if d <= 18:
            brute = subset_sums_bruteforce(lam)
            assert sums == brute
            for s in range(d + 1):
                assert (s in sums) == (s in brute)
                exhaustive_checks += 1

assert subset_sums_dp((3,)) == {0, 3}
assert subset_sums_dp((2,1)) == {0,1,2,3}
assert subset_sums_dp((2,2)) == {0,2,4}
assert subset_sums_dp((4,2,1)) == set(range(8))

print("VERIFY_OK", partition_checks, exhaustive_checks, criterion_checks, total_fixed_points)
