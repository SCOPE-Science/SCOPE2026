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

The proof is self-contained conditional only on the standard uniform-distribution theorem for irrational rotations and the classical bounded-type interval discrepancy estimate. Key analytic checks are the exact interval-intersection identity (1), the odd/even triangular partition-of-unity computation, and the uniform arc discrepancy bound (2); these are expanded in `RESULT.md`.

Run `python3 CHECK.py` from a directory containing the standalone file. On the tested interpreter the exact-rational program reported 1,413 circle-overlap and parity checks, 252 matches between two independently generated finite languages (moduli 2 through 8, lengths 1 through 36), and 28 finite minimum Hamming-distance checks. All passed.

The rational rotation approximant and the substitution language are compared directly on every tested horizon. Finite tests neither prove irrational equidistribution nor certify the logarithmic discrepancy rate. No independently conducted mathematical audit or external formal certification is claimed.
