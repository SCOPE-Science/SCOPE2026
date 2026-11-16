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

# Exact-integer verification

Run `python CHECK.py` with Python 3; no third-party packages are needed. The checker constructs the three-state automaton, checks the seven-step integer matrices and their fixed vectors, verifies all nine witness classes to length 120, computes 262,142 exhaustive Walsh coefficients for lengths one to seventeen, and cross-checks selected coefficients by direct enumeration. Expected final marker: `AVOID_101_FOURIER_PERIOD7_PASS full_frequencies=262142 lengths=1..17 witness_lengths=1..120`.

These calculations reproduce finite consequences and critical matrix equalities. General validity follows from the exact transfer-matrix identities and the parity argument in `RESULT.md`; the finite census alone would not prove the theorem. Other forbidden patterns, cyclic avoidance, exact singular nullities, and independent historical priority remain unchecked.
