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
# Computational and proof verification

The file `verify.py` solves the derivation linear constraints over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), using exact modular Gaussian elimination with no external libraries. For each of the six tested rank/field configurations, every point of the underlying Lie algebra is enumerated and the rank of the evaluation map from ordinary derivations is determined. The observed ranks agree with the proof: zero for zero, one on each nonzero central vector, and the full Lie-algebra dimension at each noncentral vector. The raw program output appears in `VERIFY_OUTPUT.txt`; rerun with `python3 verify.py`.

Exact coverage: rank and prime combinations \((m,p)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\), amounting to 563 exhaustive pointwise evaluation checks. This is not exhaustive over all prime powers, field characteristics, or ranks.

The symbolic argument verifies necessity from characteristic preservation of the derived ideal, sufficiency via the explicit symplectic evaluation operator and choice of central functional, and counting via the full conformal-symplectic dimension. It does not assert anything about nonlinear or two-local maps. Independent audit has not been performed.
