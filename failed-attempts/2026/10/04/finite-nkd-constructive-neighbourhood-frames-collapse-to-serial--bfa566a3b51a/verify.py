#!/usr/bin/env python3

def subsets(n):
    return list(range(1 << n))

def is_admissible(fam):
    if not fam:
        return False
    for a in fam:
        for b in fam:
            if (a & b) == 0:
                return False
            if (a & b) not in fam:
                return False
    return True

def core_of(fam, n):
    c = (1 << n) - 1
    for a in fam:
        c &= a
    return c

for n in range(1, 5):
    subs = subsets(n)
    seen_cores = set()
    admissible = 0
    for mask in range(1 << len(subs)):
        fam = {subs[i] for i in range(len(subs)) if (mask >> i) & 1}
        if not is_admissible(fam):
            continue
        admissible += 1
        c = core_of(fam, n)
        assert c != 0
        assert c in fam
        seen_cores.add(c)
        for A in subs:
            box_family = any((u & ~A) == 0 for u in fam)
            box_core = (c & ~A) == 0
            assert box_family == box_core
            dia_family = all((u & A) != 0 for u in fam)
            dia_core = (c & A) != 0
            assert dia_family == dia_core
    assert seen_cores == set(range(1, 1 << n))
    print(n, admissible, len(seen_cores))

print("VERIFY_OK")
