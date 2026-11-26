---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction

Place `certificates.json`, `verify.py`, and `verify_independent.py` together in one directory. With Python 3 and no additional packages, execute `python3 verify.py`, expecting `VERIFY_OK`, and `python3 verify_independent.py`, expecting `ALTERNATE_OK`. Both scripts regenerate excursions of lengths one through seven and identify every distinct one-deletion output.

`verify.py` verifies, for every layer, the exact rational primal capacity inequalities and the exact rational dual covering inequalities, equality of both objectives, and an explicit integer-optimal disjoint-shadow codebook. It counts all maximum cliques in the compatibility graph using bitmask Bron–Kerbosch with pruning that excludes only branches unable to match the best size already found. It compares the maximum sizes and counts with the claim. These tests verify the objective gaps, not integrality of the packing polytope. The fractional vertex at length four can be checked directly from the three deletion shadows in `RESULT.md`.

`verify_independent.py` uses a separate Cartesian-product source enumeration and a memoized include/exclude recursion on incompatibility masks to calculate the maximum size and number of its attaining independent sets, without reading the rational certificate. This is an independent implementation rather than a third-party validation.

Checks are exhaustive for the stated finite domain only. The certificates prove no claims for larger lengths, and no independent external audit has been performed.
