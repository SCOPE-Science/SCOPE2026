from itertools import product


def ham_ball(z, q, s):
    """All q-ary words at Hamming distance at most s from z."""
    m = len(z)
    out = set()
    for w in product(range(q), repeat=m):
        if sum(a != b for a, b in zip(z, w)) <= s:
            out.add(w)
    return out


def ds_ball(x, q, s):
    """Exactly one deletion followed by at most s substitutions."""
    out = set()
    for d in range(len(x)):
        z = x[:d] + x[d + 1:]
        out |= ham_ball(z, q, s)
    return out


def compatible(x, y, q, s):
    return ds_ball(x, q, s).isdisjoint(ds_ball(y, q, s))


cases = []
for s in range(3):
    for q in range(2, 4):
        for n in range(1, 2 * s + 2):
            words = list(product(range(q), repeat=n))
            balls = [ds_ball(w, q, s) for w in words]
            for i in range(len(words)):
                for j in range(i):
                    if balls[i].isdisjoint(balls[j]):
                        raise AssertionError(("compatible pair below threshold", s, q, n, words[i], words[j]))
            cases.append((s, q, n, "max=1"))

        n = 2 * s + 2
        words = list(product(range(q), repeat=n))
        balls = [ds_ball(w, q, s) for w in words]
        for i in range(len(words)):
            for j in range(i):
                if balls[i].isdisjoint(balls[j]):
                    assert words[i][0] != words[j][0], ("same first symbol compatible", s, q, words[i], words[j])

        constants = [tuple([a] * n) for a in range(q)]
        for i in range(q):
            for j in range(i):
                assert compatible(constants[i], constants[j], q, s), ("constant words conflict", s, q, n, i, j)
        cases.append((s, q, n, "max=q"))

print("checked", len(cases), "parameter cases")
for case in cases:
    print(case)
print("VERIFY_OK short_block_threshold s<=2 q<=3 direct_channel")
