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

# Reproducibility and checks

Run `python3 verify_srg.py` with a Python 3 standard library. The supplied `verification.txt` is the recorded output from the package's code before the record was assembled. The program constructs the six named simple graphs, checks strong regularity from pairwise common-neighbor counts, and for each graph at five exact rational positive steps directly multiplies the proposed rational kernel by the Gauss–Legendre denominator matrix and compares it to the exact numerator matrix. It tests the row sums, symmetry, sign predictions, and the exact rational Petersen counterexample. The complete universal result is proved in `RESULT.md`, not certified by numerical sampling.

Assumptions: exact unit-rate graph Laplacian, ordinary rational arithmetic for verifier tests, two-stage fourth-order Gauss–Legendre end-step. The formal proof handles all positive real steps, all admissible strongly regular graphs and the endpoints. No floating-point simulation, higher-dimensional enumeration, or independent external scientific validation is claimed.
