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

# Verification and limits

The supplied `hesse_verify.py` enumerates all \(432\) affine maps of \(\mathbb F_3^2\), with a second construction of the twelve lines using translated subgroups. All action permutations are exact. Fixed lines are counted twice, by the induced permutation and by the quotient-space linear criterion. Independent group multiplication and inverse formulas yield eleven conjugacy classes; ten joint cycle spectra remain. The output CSV is the precise ten-row classification and the script reproduces it. Characteristic-seven Weierstrass discriminants, rational point counts, and division-polynomial roots are independently calculated by exhaustive arithmetic in \(\mathbb F_7\).

These finite calculations are exhaustive for the finite affine group and provide no assertion about the cardinalities of elliptic curves over arbitrary extensions without the proved group-law/Weil-pairing reduction. Characteristic three is excluded and the full zeta function of the smooth cubic is outside the claim. No external independent mathematical audit has been conducted.
