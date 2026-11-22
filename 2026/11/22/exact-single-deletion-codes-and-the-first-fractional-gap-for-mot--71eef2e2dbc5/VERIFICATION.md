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

# Reproduction

Place `certificates.json`, `verify.py`, and `verify_independent.py` together in one directory. With Python 3 and no additional packages, execute `python3 verify.py`, expecting `VERIFY_OK`, and `python3 verify_independent.py`, expecting `ALTERNATE_OK`. Both scripts regenerate excursions of lengths one through seven and identify every distinct one-deletion output.

`verify.py` verifies, for every layer, the exact rational primal capacity inequalities and the exact rational dual covering inequalities, equality of both objectives, and an explicit integer-optimal disjoint-shadow codebook. It also enumerates every maximal clique in the compatibility graph using a complete bitmask Bron–Kerbosch recursion and compares the maximum sizes and counts with the claim.

`verify_independent.py` uses a separate Cartesian-product source enumeration and a memoized include/exclude recursion on incompatibility masks to calculate the maximum size and number of its attaining independent sets, without reading the rational certificate. This is an independent implementation rather than a third-party validation.

Checks are exhaustive for the stated finite domain only. The certificates prove no claims for larger lengths, and no independent external audit has been performed.
