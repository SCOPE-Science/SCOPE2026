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

The standalone `verify.py` checks the stated lattice-interval recurrence by direct brute-force Littlestone recursion on every labeled poset with at most four elements, checks the independent two-row parameterization against direct enumerations for widths one through six, and computes the rank sequence through width thirty. It separately checks the instances corresponding to the first four dyadic parameters.

Run with `python3 verify.py` from the folder containing this document and the program; no dependencies beyond Python 3 are required. The expected successful output is `ORDER_IDEAL_ONLINE_PASS 242 posets 6 direct grid crosschecks 30 grid ranks 4 dyadic equalities`.

Finite tests are not a proof for arbitrary posets or for all dyadic indices. Those conclusions rely on the proof in `RESULT.md`. The implementation is not an external formal proof assistant or independent audit. The asymptotic constants and the general fixed-width transition bound are proved mathematically rather than empirically certified.
