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

# Exact reproducibility

Run `python3 verify_king4_d4.py` using ordinary Python 3 and its standard library. The complete construction of king faces, square symmetries, barycentric flags, orbit cells, signed integer boundaries, integral unimodular pivots and finite-field rank checks is embedded in the script. Expected successful last line is `H_0=Z H_1=0 H_2=Z/2 H_3=0; no other degrees` preceded by `KING4_D4_QUOTIENT_INTEGRAL_HOMOLOGY_OK`.

Checks: 313 nonempty faces with counts 16, 78, 140 and 79; 50, 283, 471 and 237 quotient cells; the integral consecutive boundary compositions vanish; 49, 234, 236 unit Smith pivots and a final degree-three invariant factor 2; mod-two and mod-three boundary ranks match. These are exhaustive finite checks, not an infinite proof or independent mathematical audit. The result does not determine the quotient's fundamental group or homotopy type.
