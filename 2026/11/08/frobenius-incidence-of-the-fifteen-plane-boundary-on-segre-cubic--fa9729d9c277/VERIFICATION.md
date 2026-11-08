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

Run `python3 verify_incidence.py` to enumerate all 32767 nonempty subsets of the fifteen matchings for every one of the eleven conjugacy partitions. Graph bipartite-component dimensions, Frobenius saturation, and exact integer-polynomial binomial inversion reproduce all 44 displayed formulas. It prints `VERIFY_SEGRE_BOUNDARY_OK 11 FROBENIUS TYPES`. The code uses only the Python standard library and exact arithmetic, not numerical interpolation.

Run `python3 verify_direct.py` to construct finite fields with 25 and 125 elements using irreducible polynomials over the field of five elements. Pointwise enumeration of the union and twisted Frobenius reproduces the totals 166, 86, 98, 91 and 4 in the five tested conjugacy types. It prints `VERIFY_SEGRE_DIRECT_OK F25_F125`.

The argument for every finite field of permitted characteristic does not extrapolate from these examples: its universal ingredients are the matching multiplicity classification, graph-linear intersection dimensions, Frobenius saturation and finite-field descent. The zero rational points in the five-cycle form have an independent direct orbit-size proof. No external mathematical audit was conducted.
