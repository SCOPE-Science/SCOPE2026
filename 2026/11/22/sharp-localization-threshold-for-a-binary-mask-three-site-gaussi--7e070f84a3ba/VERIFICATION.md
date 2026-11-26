---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reflection separates the matrix into its odd eigenvalue 1-x^4 and an even block [[1+x^4,y],[2x,1]]. Since 0<x<y<1, the determinant sign is the even-block determinant sign. The minimum in the closure of the admissible middle-width range occurs at y=1; its value (x-1)(x^3+x^2+x-1) is nonnegative exactly for x<=rho in (0,1). At x=rho the excluded y=1 is the only zero, so the threshold is inclusive. For x>rho, y_*=(1+x^4)/(2x) is below 1 and exceeds x by (1-x^2)^2/(2x); y decreases strictly as beta increases, so this gives existence, uniqueness and both signs. At fixed R>1, f_p=1+x^4-2x^p, p=1+R^-2, has one interior minimum, is negative just left of 1 because f_p'(1)>0, and tends to one at zero. This proves exactly one interior crossing. For fixed x, f_p is strictly increasing in p; hence the first root is increasing in p, and continuity with the p=1 and p=2 limiting functions gives the stated endpoint limits. The rational witness has exact rank two and the stated null line. The two-site determinant verifies the minimal possible dimension, not priority of the example.

## originality

PASS

The assessed increment is the necessary-and-sufficient universal finite-width threshold, the singular-locus classification and the fixed-ratio crossing, not the variable-shape matrix, the mask rule, three-site singularity, or an ideal replacement criterion. The strongest available comparisons do not cover this increment; access limits prevent a priority guarantee.

## value

PASS

The fixed symmetric binary mask is motivated by a concrete adaptive approximation rule, and the first dimension admitting singularity is the right place to separate finite-Gaussian behavior from exact ideal column replacement. A dimensionless sharp safety boundary with both signs and a unique fixed-ratio singular crossing is materially more useful for choosing parameters or testing a solver than just another singular matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
