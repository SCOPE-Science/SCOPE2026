"""Independent exact verifier for lane-198 (stdlib only).

Replays: witness shapes/entries, Bareiss det=73728 for W1 and W2, Gram
recompute + det(G)=(det)^2 for both, two-sided interval arithmetic,
HT-equivalence decision procedure on controls, and the committed pairwise
HT table (W1 vs W2 inequivalent; all 7 candidates have |det|=73728).
Run:  python3 output/artifacts/verify.py
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hteq import bareiss_det, ht_equal, transpose


def load_csv(name):
    with open(os.path.join(HERE, name)) as f:
        return [list(map(int, r)) for r in csv.reader(f)]


def check_witness(M, G, tag, det):
    assert len(M) == 10 and all(len(r) == 10 for r in M), f"{tag} shape"
    assert all(v in (-1, 1) for r in M for v in r), f"{tag} entries"
    d = bareiss_det(M)
    assert d == det, f"det({tag})={d}"
    R = [[sum(M[i][k] * M[j][k] for k in range(10)) for j in range(10)]
         for i in range(10)]
    assert R == G, f"{tag} stored Gram != M*M^T"
    assert all(G[i][i] == 10 for i in range(10)), f"{tag} Gram diagonal"
    g = bareiss_det(G)
    assert g == d * d, f"det(G_{tag})={g}"
    print(f"det({tag}) = {d}, det(Gram) = {g} = {d}^2  OK")


def main():
    W1 = load_csv("witness_W1.csv")
    G1 = load_csv("gram_W1.csv")
    W2 = load_csv("witness_W2.csv")
    G2 = load_csv("gram_W2.csv")
    check_witness(W1, G1, "W1", 73728)
    check_witness(W2, G2, "W2", 73728)

    # Interval arithmetic (analytic halves proved in DRAFT.md).
    assert 73728 % 512 == 0 and 73728 // 512 == 144
    assert 10 ** 10 == 10000000000  # Hadamard: |det|^2 <= 10^10
    assert 99840 % 512 == 0 and 99840 // 512 == 195
    assert 99840 <= 100000 < 99840 + 512
    assert 73728 <= 99840
    print("interval 73728 <= D(10) <= 99840  (D(10)/512 in [144,195])  OK")

    # HT-equivalence decision procedure: controls.
    assert ht_equal(W1, W1), "reflexivity"
    N = [W1[i] for i in [0, 3, 1, 2, 9, 4, 7, 5, 6, 8]]
    N = [[-x for x in row] for row in N]
    N = [[N[i][j] for j in [0, 9, 4, 2, 6, 1, 8, 3, 7, 5]] for i in range(10)]
    for j in (1, 5, 8):
        for i in range(10):
            N[i][j] = -N[i][j]
    N = transpose(N)
    assert abs(bareiss_det(N)) == 73728
    assert ht_equal(W1, N), "HT-move positive control"
    M = [r[:] for r in W1]
    M[0][0] = -M[0][0]
    dm = abs(bareiss_det(M))
    assert dm != 73728, f"flipped |det|={dm}"
    assert not ht_equal(W1, M), "negative control"
    print("HT controls (reflexive, signed-perm+transpose True, det-drop False) OK")

    # Committed inequivalence + candidate table.
    assert not ht_equal(W1, W2), "W1 vs W2 must be HT-inequivalent"
    print("W1 vs W2 HT-inequivalent  OK")
    with open(os.path.join(HERE, "candidate_maximizers.json")) as f:
        sols = json.load(f)
    assert len(sols) == 7
    n_eq = 0
    for i, s in enumerate(sols):
        assert all(v in (-1, 1) for r in s for v in r), f"sol {i} entries"
        assert abs(bareiss_det(s)) == 73728, f"sol {i} |det|"
        if ht_equal(W1, s):
            n_eq += 1
    with open(os.path.join(HERE, "certificates.json")) as f:
        certs = json.load(f)
    assert certs["ht_pairwise"]["n_equivalent_to_W1"] == n_eq, "cert table"
    assert certs["ht_pairwise"]["classes_distinguished"] == ["W1-class", "W2-class"]
    print(f"7/7 candidates |det|=73728; {n_eq}/7 in W1-class; cert table OK")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
