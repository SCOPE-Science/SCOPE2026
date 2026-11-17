#!/usr/bin/env python3
"""Finite diagnostic for the geometric-marker Lie/Abelian complexity formulas.

For each tested (base, length), the prefix stops beyond a power whose
preceding and following marker gaps exceed the window length. Any later
window has at most one marker, and all one-marker rotations already occur,
so the enumerated factor language is complete for that length.
"""

def expected(base, length):
    k = 0
    q = length
    while q >= base:
        q //= base
        k += 1
    abelian = k + 2
    extra = (base == 2 and length in (2, 3)) or (base == 3 and length == 4)
    lie = 2 + int(extra)
    return lie, abelian


def factors(base, length):
    marker = 1
    while marker - marker // base < length:
        marker *= base
    # marker is a positive base-power, with preceding marker at marker/base.
    # It is distant enough to isolate every possible one-marker factor.
    bits = bytearray(marker + length + 1)
    power = 1
    while power < len(bits):
        bits[power] = 1
        power *= base
    seen = set()
    mask = (1 << length) - 1
    word = 0
    for i in range(length):
        word = (word << 1) | bits[i]
    seen.add(word)
    for j in range(length, len(bits)):
        word = ((word << 1) | bits[j]) & mask
        seen.add(word)
    return seen


def measured(values, length):
    seen_orbits = set()
    lie = 0
    mask = (1 << length) - 1
    for v in values:
        if v in seen_orbits:
            continue
        rots = {((v << k) | (v >> (length-k))) & mask for k in range(length)}
        if rots <= values:
            lie += 1
        seen_orbits.update(rots)
    abelian = len({v.bit_count() for v in values})
    return lie, abelian


def main():
    tests = 0
    for base in range(2, 12):
        for length in range(1, 161):
            values = factors(base, length)
            observed = measured(values, length)
            want = expected(base, length)
            if observed != want:
                raise AssertionError((base, length, observed, want))
            tests += 1
    print(f"VERIFY_OK base_length_pairs={tests} bases=2..11 lengths=1..160")


if __name__ == "__main__":
    main()
