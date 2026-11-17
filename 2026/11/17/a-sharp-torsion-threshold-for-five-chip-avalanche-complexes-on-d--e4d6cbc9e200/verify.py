#!/usr/bin/env python3
"""Exact integral homology census for cyclic five-grain avalanche complexes.

Requires SymPy. Use `python verify.py` to regenerate census.csv and check
all integral Smith invariants for binary supports of size at most five on
consistently directed cycles with 3 <= number of vertices <= 15.
"""
import csv
import hashlib
import itertools
from collections import Counter, defaultdict
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def dihedral_canonical(n, support):
    return min(
        tuple(sorted((translation + direction * x) % n for x in support))
        for direction in (-1, 1)
        for translation in range(n)
    )


def all_faces(n, support):
    result = set()
    for translation in range(n):
        facet = tuple(sorted((translation + x) % n for x in support))
        for size in range(1, len(facet) + 1):
            result.update(itertools.combinations(facet, size))
    return result


def elementary_collapse(faces):
    """Remove only genuine free codimension-one face/coface pairs."""
    faces = set(faces)
    count = 0
    while True:
        codimension_one_cofaces = defaultdict(list)
        for facet in faces:
            if len(facet) <= 1:
                continue
            for i in range(len(facet)):
                codimension_one_cofaces[facet[:i] + facet[i + 1 :]].append(facet)
        options = [
            (face, carriers[0])
            for face, carriers in codimension_one_cofaces.items()
            if len(carriers) == 1 and len(carriers[0]) == len(face) + 1
        ]
        if not options:
            break
        face, carrier = min(options, key=lambda pair: (-len(pair[1]), pair[1], pair[0]))
        assert face in faces and carrier in faces
        faces.remove(face)
        faces.remove(carrier)
        count += 1
    return faces, count


def smith_rank_and_torsion(lower, upper):
    if not lower or not upper:
        return 0, ()
    rows = {simplex: i for i, simplex in enumerate(lower)}
    matrix = Matrix.zeros(len(lower), len(upper))
    for j, simplex in enumerate(upper):
        for i in range(len(simplex)):
            codimension_one_face = simplex[:i] + simplex[i + 1 :]
            matrix[rows[codimension_one_face], j] = 1 if i % 2 == 0 else -1
    smith = smith_normal_form(matrix, domain=ZZ)
    entries = [
        abs(int(smith[i, i]))
        for i in range(min(smith.rows, smith.cols))
        if smith[i, i] != 0
    ]
    assert all(entries[i + 1] % entries[i] == 0 for i in range(len(entries) - 1))
    return len(entries), tuple(entry for entry in entries if entry > 1)


def integral_homology(faces):
    """All integral homology; torsion of H_{i-1} equals torsion of coker d_i."""
    levels = defaultdict(list)
    for simplex in faces:
        levels[len(simplex) - 1].append(simplex)
    for simplices in levels.values():
        simplices.sort()
    d = max(levels)
    boundary_rank = [0] * (d + 2)
    smith_torsion = [()] * (d + 2)
    for i in range(1, d + 1):
        boundary_rank[i], smith_torsion[i] = smith_rank_and_torsion(levels[i - 1], levels[i])
    groups = []
    for i in range(d + 1):
        rank = len(levels[i]) - boundary_rank[i] - boundary_rank[i + 1]
        assert rank >= 0
        groups.append((rank, smith_torsion[i + 1]))
    return groups


def serial_group(group):
    rank, torsion = group
    return f"Z^{rank}" + ("+" + "+".join(f"Z/{v}" for v in torsion) if torsion else "")


TWO_TORSION_REPRESENTATIVES = [
    (0, 1, 2, 4, 10), (0, 1, 2, 5, 8),
    (0, 1, 3, 4, 9), (0, 1, 3, 5, 12),
    (0, 1, 3, 6, 7), (0, 1, 3, 6, 10),
    (0, 1, 3, 7, 10), (0, 1, 3, 7, 12),
    (0, 1, 3, 7, 13), (0, 1, 3, 10, 12),
    (0, 1, 4, 6, 9), (0, 1, 4, 6, 12),
    (0, 1, 4, 7, 9), (0, 1, 4, 8, 10),
]


def run():
    rows = []
    first_torsion = []
    counts = Counter()
    for n in range(3, 16):
        for chips in range(1, min(n, 5) + 1):
            representatives = {
                dihedral_canonical(n, support)
                for support in itertools.combinations(range(n), chips)
            }
            for support in sorted(representatives):
                full = all_faces(n, support)
                reduced, pairs = elementary_collapse(full)
                groups = integral_homology(reduced)
                if any(torsion for _, torsion in groups):
                    first_torsion.append((n, chips, support, groups))
                counts[(n, chips)] += 1
                row = {
                    "n": n, "chips": chips,
                    "support": " ".join(str(x) for x in support),
                    "original_face_count": len(full),
                    "collapse_pairs": pairs,
                    "remaining_max_dimension": len(groups) - 1,
                }
                for dimension in range(5):
                    row[f"H{dimension}"] = serial_group(groups[dimension]) if dimension < len(groups) else "0"
                rows.append(row)
    assert len(rows) == 747, len(rows)
    assert counts[(15, 5)] == 111
    assert len(first_torsion) == 14
    assert [x[2] for x in first_torsion] == TWO_TORSION_REPRESENTATIVES
    assert all(n == 15 and chips == 5 for n, chips, _, _ in first_torsion)
    assert all(groups[1][1] == (2, 2) for _, _, _, groups in first_torsion)
    assert Counter((groups[1][0], groups[2][0]) for _, _, _, groups in first_torsion) == Counter({(2, 1): 10, (1, 0): 4})
    assert all(len(groups) == 3 for _, _, _, groups in first_torsion)
    # Completely separate unreduced boundary-matrix reductions for two witnesses.
    for support, expected_h1, expected_h2 in [
        ((0, 1, 3, 4, 9), (2, (2, 2)), (1, ())),
        ((0, 1, 2, 4, 10), (1, (2, 2)), (0, ())),
    ]:
        raw_groups = integral_homology(all_faces(15, support))
        assert raw_groups[1] == expected_h1 and raw_groups[2] == expected_h2
        assert raw_groups[3:] == [(0, ())] * (len(raw_groups) - 3)
    path = Path(__file__).with_name("census.csv")
    columns = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print("dihedral_classes=747; length15_five_chip_classes=111")
    print("torsion_cases=14; each has H1_torsion=(Z/2)^2")
    print("ten cases: H1_free=2,H2_free=1; four cases: H1_free=1,H2_free=0")
    print("all other listed integral groups torsion-free")
    print("uncollapsed_witness_matrix_checks=2 passed")
    print("census.csv bytes=", path.stat().st_size, " sha256=", digest, sep="")

if __name__ == "__main__":
    run()
