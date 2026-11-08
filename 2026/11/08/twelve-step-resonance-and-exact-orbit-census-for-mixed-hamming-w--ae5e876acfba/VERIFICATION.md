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

# Reproducible checks

Run `python3 check_matrices.py` and `python3 check_bruteforce.py` from a directory containing the delivered scripts. Compare terminal output byte-for-byte with `check_matrices.stdout.txt` and `check_bruteforce.stdout.txt`. Both scripts use only the Python standard library.

The first script explicitly constructs every Hamming neighbor-sum matrix on nineteen tested factor tuples, forms the two-row map in characteristic two and evaluates fixed-point dimensions by binary elimination at times one, two, three, four, six and twelve. It checks the exponent formulas for graph orders up to 36. The second script independently iterates every binary two-row state for the tuples `(2,)`, `(3,)`, `(2,2)`, `(2,3)` and `(3,3)` (266,576 states in all), compares exact least-period frequencies with the closed census, and rejects any observed period beyond twelve. The one- and two-coordinate instances exercise the algebraic boundary; the theorem itself concerns mixed parity with at least three factors.

All six primitive periods in the claimed family are shown to exist by the proof, not by extrapolation from the finite examples. These computations do not independently validate all field sizes, graph dimensions, or historical priority. Independent audit status: not performed.
