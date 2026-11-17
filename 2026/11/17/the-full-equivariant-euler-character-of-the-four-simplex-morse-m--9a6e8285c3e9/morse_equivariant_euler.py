#!/usr/bin/env python3
"""Exact finite enumeration of the equivariant reduced Euler characteristic of
Morse-matching complexes on simplices. Python 3.9+, standard library only.
"""
from collections import Counter
from math import factorial


def simplex_model(number_of_vertices):
    n = number_of_vertices
    faces = range(1, 1 << n)  # nonempty faces; empty face is not a Hasse node
    covers = [(a, b) for b in faces for a in faces
              if (a & b) == a and b.bit_count() == a.bit_count() + 1]
    assert len(covers) == n * (2 ** (n - 1) - 1)
    # A gradient path moves between matched lower simplices of one rank.
    # An arrow from pair (a,b) to pair (c,d) is present exactly when
    # c != a is another codimension-one face of b.
    out = []
    for a, b in covers:
        out.append(sum(1 << j for j, (c, _) in enumerate(covers)
                       if c != a and c.bit_count() == a.bit_count()
                       and (c & b) == c))
    return covers, out


def closed_gradient_path(edge_bits, out):
    """Detect a directed cycle among matched lower simplices."""
    remaining = edge_bits
    finished = 0
    while remaining:
        first = remaining & -remaining
        stack = [(first.bit_length() - 1, 0)]
        active = first
        while stack:
            v, inspected = stack[-1]
            choices = out[v] & edge_bits & ~finished & ~inspected
            if not choices:
                finished |= 1 << v
                remaining &= ~(1 << v)
                active &= ~(1 << v)
                stack.pop()
            else:
                next_bit = choices & -choices
                stack[-1] = (v, inspected | next_bit)
                if next_bit & active:
                    return True
                stack.append((next_bit.bit_length() - 1, 0))
                active |= next_bit
    return False


def representative(partition):
    permutation = []
    start = 0
    for length in partition:
        permutation.extend(start + ((i + 1) % length)
                           for i in range(length))
        start += length
    return permutation


def fixed_matching_orbits(partition, covers, out):
    n = sum(partition)
    perm = representative(partition)
    def permute(face):
        return sum(1 << perm[i] for i in range(n) if face & (1 << i))
    index = {e: i for i, e in enumerate(covers)}
    unvisited = set(range(len(covers)))
    orbits = []
    while unvisited:
        seed = min(unvisited)
        orbit = []
        current = seed
        while current not in orbit:
            orbit.append(current)
            unvisited.remove(current)
            a, b = covers[current]
            current = index[(permute(a), permute(b))]
        assert current == seed
        orbits.append(orbit)
    valid = []
    for orbit in orbits:
        occupied = 0
        for i in orbit:
            a, b = covers[i]
            pair_faces = (1 << a) | (1 << b)
            if occupied & pair_faces:
                break
            occupied |= pair_faces
        else:
            matched_edges = sum(1 << i for i in orbit)
            if not closed_gradient_path(matched_edges, out):
                valid.append((occupied, matched_edges))
    valid.sort(key=lambda data: data[0].bit_count(), reverse=True)
    return valid, len(orbits)


def fixed_orbit_polynomial(partition):
    covers, out = simplex_model(sum(partition))
    orbits, total_orbits = fixed_matching_orbits(partition, covers, out)
    counts = Counter()
    visited_states = 0
    def enumerate_subsets(position, occupied, selected_edges, number_of_orbits):
        nonlocal visited_states
        visited_states += 1
        if position == len(orbits):
            counts[number_of_orbits] += 1
            return
        enumerate_subsets(position + 1, occupied, selected_edges, number_of_orbits)
        faces, edges = orbits[position]
        if not (faces & occupied) and not closed_gradient_path(selected_edges | edges, out):
            enumerate_subsets(position + 1, occupied | faces,
                              selected_edges | edges, number_of_orbits + 1)
    enumerate_subsets(0, 0, 0, 0)
    return counts, total_orbits, len(orbits), visited_states


def reduced_lefschetz(counts):
    # A g-invariant simplex consisting of k primitive Hasse edges in o
    # g-orbits has signed reduced-chain trace (-1)^(o-1), including
    # the augmented degree -1 empty face trace -1.
    return -sum((-1) ** number * multiplicity for number, multiplicity
                in counts.items())


def character_table(partitions):
    table = []
    for part in partitions:
        fixed = part.count(1)
        sign = (-1) ** (5 - len(part))
        std = fixed - 1
        std_sq = sum(length for length in part if 2 % length == 0) - 1
        assert (std * std + std_sq) % 2 == 0
        assert (std * std - std_sq) % 2 == 0
        two_row = (std * std + std_sq) // 2 - 1 - std
        hook = (std * std - std_sq) // 2
        table.append([1, std, two_row, hook,
                      sign * two_row, sign * std, sign])
    return table


def conjugacy_size(part):
    counts = Counter(part)
    z = 1
    for length, amount in counts.items():
        z *= (length ** amount) * factorial(amount)
    return factorial(sum(part)) // z


def run():
    # Independent published comparison case: tetrahedral Morse matching complex.
    tetra_parts = [(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
    tetra_expected = (99,1,-1,0,-1)
    tetra_found=[]
    for part in tetra_parts:
        coeffs, _, _, _ = fixed_orbit_polynomial(part)
        tetra_found.append(reduced_lefschetz(coeffs))
        if part == (1,1,1,1):
            assert sum(coeffs.values()) == 12821
    assert tuple(tetra_found) == tetra_expected, (tetra_found,tetra_expected)
    print('TETRAHEDRAL_INDEPENDENT_COMPARISON_PASS',tetra_found,flush=True)

    # Identity reduced Euler characteristic follows from the published
    # exhaustive f-vector of the five-vertex simplex's Morse complex.
    published_f=(75,2485,47955,598425,5071367,29844505,
                 122685075,350017175,680808105,876110235,
                 712961065,343320335,88467825,10315975,380125)
    reduced_identity=sum((-1)**i * count for i,count in enumerate(published_f)) - 1
    assert reduced_identity==212456
    parts=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
    lefschetz=[reduced_identity]
    for part in parts[1:]:
        poly,total,usable,states=fixed_orbit_polynomial(part)
        value=reduced_lefschetz(poly)
        lefschetz.append(value)
        print(f'PARTITION {part}: primitive_orbits={total} eligible_orbits={usable} '
              f'fixed_matching_count={sum(poly.values())} '
              f'polynomial={sorted(poly.items())} '
              f'reduced_lefschetz={value} recursion_states={states}',flush=True)
    assert lefschetz==[212456,-16,0,-1,-1,0,1],lefschetz
    chars=character_table(parts)
    names=['(5)','(4,1)','(3,2)','(3,1,1)','(2,2,1)','(2,1,1,1)','(1,1,1,1,1)']
    dims=chars[0]
    multiples=[]
    for j in range(7):
        numer=sum(conjugacy_size(part)*lefschetz[i]*chars[i][j]
                  for i,part in enumerate(parts))
        assert numer%120==0
        multiples.append(numer//120)
    assert multiples==[1769,7079,8851,10623,8854,7084,1772]
    assert sum(m*d for m,d in zip(multiples,dims))==reduced_identity
    assert sum(conjugacy_size(part) * lefschetz[i] for i,part in enumerate(parts)) == 120*1769
    assert sum(conjugacy_size(part) for part in parts)==120
    print('CLASS_LEFSCHETZ',list(zip(parts,lefschetz)),flush=True)
    print('SPECHT_VIRTUAL_MULTIPLICITIES',list(zip(names,multiples)),flush=True)
    print('QUOTIENT_REDUCED_RATIONAL_EULER',multiples[0],flush=True)
    print('MORSE_FOUR_SIMPLEX_EQUIVARIANT_EULER_PASS',flush=True)

if __name__=='__main__':
    run()
