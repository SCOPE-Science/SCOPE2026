#!/usr/bin/env python3
"""Finite face/cyclic-character sanity checks for whiskered-cycle 2-matching complexes.
No external modules required. This is corroboration, not the all-size proof.
"""
from itertools import combinations


def inversion_sign(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1


def faces(n):
    """Bitsets on rim edges 0..n-1 and pendant edges n..2n-1."""
    for rim in range(1 << n):
        permitted = [i for i in range(n) if not (rim >> i & 1 and rim >> ((i - 1) % n) & 1)]
        for spoke_choice in range(1 << len(permitted)):
            mask = rim
            for j, idx in enumerate(permitted):
                if spoke_choice >> j & 1:
                    mask |= 1 << (n + idx)
            yield mask


def matching(n, all_faces):
    """Pairs via least available pendant edge, leaving the complete rim face."""
    pairs = set()
    for mask in all_faces:
        rim = mask & ((1 << n) - 1)
        if rim == (1 << n) - 1:
            continue
        i = min(k for k in range(n) if not (rim >> k & 1 and rim >> ((k - 1) % n) & 1))
        paired = mask ^ (1 << (n + i))
        assert paired in all_faces
        pairs.add(tuple(sorted((mask, paired))))
    assert len(pairs) * 2 + 1 == len(all_faces)
    assert ((1 << n) - 1) in all_faces
    return pairs


def oriented_trace(mask, perm):
    chosen = [i for i in range(len(perm)) if mask >> i & 1]
    mapped = [perm[i] for i in chosen]
    return inversion_sign(mapped) if sorted(mapped) == chosen else 0


def reduced_lefschetz(all_faces, perm):
    value = -1  # empty simplex contributes (-1)^{-1}
    for mask in all_faces:
        if not mask:
            continue
        value += (-1 if mask.bit_count() % 2 == 0 else 1) * oriented_trace(mask, perm)
    return value


def verify(n):
    all_faces = set(faces(n))
    critical = ((1 << n) - 1)
    pairs = matching(n, all_faces)
    assert all((a ^ b).bit_count() == 1 for a, b in pairs)
    rot = [(i + 1) % n for i in range(n)] + [n + (i + 1) % n for i in range(n)]
    ref = [(-i - 1) % n for i in range(n)] + [n + (-i) % n for i in range(n)]
    for sym, perm in (("rotation", rot), ("reflection", ref)):
        trace = reduced_lefschetz(all_faces, perm)
        rim_sign = inversion_sign(perm[:n])
        expected = (-1)**(n-1) * rim_sign
        assert trace == expected, (n, sym, trace, expected)
    invariant_rot = [mask for mask in all_faces if all(((mask >> i) & 1) == ((mask >> rot[i]) & 1) for i in range(2*n))]
    assert set(invariant_rot) == {0, (1 << n) - 1, ((1 << n) - 1) << n}
    return (n, len(all_faces), len(pairs), inversion_sign(rot[:n]), inversion_sign(ref[:n]))

if __name__ == '__main__':
    for n in range(3, 9):
        n, count, paired, rsign, ssign = verify(n)
        print(f"n={n}: faces={count}, pairs={paired}, one critical rim face, r={rsign:+d}, s={ssign:+d}, full-rotation fixed S^0")
    print("FINITE_CHECKS_PASS")
