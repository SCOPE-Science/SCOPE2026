---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the finite checks

Execute `python3 verify_wave.py` and `python3 verify_bruteforce.py` from the extracted package containing those two standalone files. Both scripts use Python 3 standard library exclusively. The captured stdout is in `verify_wave_output.txt` and `verify_bruteforce_output.txt`.

`verify_wave.py` independently computes adjacency arrays and exact ranks over \(\mathbb F_2\) for the 5-cycle, two complete bipartite graphs, the Petersen graph, 4- and 5-rook graphs, two triangular graphs, the Paley graph on 13 vertices, the 63-vertex symplectic graph, and its four-vertex Godsil--McKay switch. It tests every asserted fixed-space dimension by direct nullity of the corresponding two-row update matrix power and tests that the predicted global order is exact. For the 63-vertex cospectral pair it verifies binary 2-ranks 6 and 8, with the common strongly regular parameters \((63,32,16,16)\).

`verify_bruteforce.py` independently iterates all \(1024\), \(256\), and \(4096\) binary two-row configurations of the 5-cycle, \(K_{2,2}\), and \(K_{3,3}\), respectively, to recover primitive periods, fixed counts and primitive cycle numbers, without matrix powers. Outputs match the claimed order-ten, order-four, and order-six branches.

**Limits.** The calculations are finite checks; infinitely many strongly regular graphs and arbitrarily large field sizes are covered solely by the algebraic argument in `RESULT.md`. None of these checks certifies novelty or serves as an independent mathematical audit.
