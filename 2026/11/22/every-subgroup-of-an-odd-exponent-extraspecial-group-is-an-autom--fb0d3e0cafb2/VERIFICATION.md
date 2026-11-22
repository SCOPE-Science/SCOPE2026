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

# Reproducibility and scope

`CHECK.py` uses only the Python standard library. Run `python CHECK.py` to check that automorphisms realize all 19 subgroups of the order-27 Heisenberg group and all 39 subgroups of its order-125 analogue. The checker enumerates every invertible \(2\times2\) matrix over the prime field, each linear central-functional coefficient, and computes their exact fixed-point sets. It separately checks six explicit four-dimensional similitudes for \(p=3,5\).

Expected final marker: `EXTRASPECIAL_FIXED_SUBGROUP_REALIZATION_OK`.

These are finite sanity checks. The proof's generality rests on the center/subgroup dichotomy and the symbolic symplectic fixed-space constructions in `RESULT.md`; no experimental claim is used as an infinite proof. This package has not undergone independent mathematical audit.
