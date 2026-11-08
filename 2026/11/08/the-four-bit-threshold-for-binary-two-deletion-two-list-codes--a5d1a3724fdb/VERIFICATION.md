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

# Verification

Run `python3 checker.py certificate.json` with Python 3, no dependencies. The verifier reconstructs every two-deletion shadow from scratch, reads the complete tree certificate, verifies that every internal split branches on an unassigned binary variable, checks every leaf using exact `fractions.Fraction` arithmetic and confirms no feasible code of size sixteen at length eight. It then checks each possible two-deletion output of the fifteen-word length-eight code and sixteen-word length-nine code has at most two distinct source parents.

The explicit sixteen-word length-nine witness and monotonicity under fixed-prefix extension establish that the first feasible length is nine. The finite certificate excludes every possible code; no runtime timeout, nonzero integer solver gap, float tolerance or heuristic candidate search is assumed in verification.

A separate historical priority comparison remains imperfect because some unindexed tables and independent finite computations may remain undiscovered. The mathematical certificate is self-contained, but independent audit has not yet been performed.
