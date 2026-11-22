---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For U_theta f=f o R_theta the exact second-order chain-rule matrix in the {f_xx,f_xy,f_yy} coordinates has pure-column abs sums 1+|cs| and mixed-column sum |c^2-s^2|+4|cs|, which dominates first-jet |c|+|s| and zeroth-order 1 for every c^2+s^2=1. The classical scalar planar Ornstein endpoint L1 non-inequality produces compactly supported smooth functions with the mixed derivative dominating pure second derivatives; shrinking spatial scale then suppresses L1 lower-order terms. Reverse triangle inequalities imply the mixed-column lower bound, giving norm 2|sin2theta|+|cos2theta|. The quarter-circle envelope attains sqrt5 precisely where |sin2theta|=2/sqrt5, yielding isometry angles and diagonal cusp. Independent exact rational-angle checks reproduced Hessian coefficients, column dominance and bound at 169 angles; infinite-dimensional lower bound requires the cited Ornstein theorem, not those checks.

## originality

PASS

The new quantitative exact rotation norm and nonmonotone angular profile are not supplied by Hamad 2026 surjective isometry classification, which detects isometries but not their distortion factors. The published exact planar shear theorem applies to triangular coordinate changes; generic rotations are not a shear, and factorization yields only norm-product inequalities. Ornstein non-inequality is an acknowledged input, not claimed as new. PASS with priority risk for unpublished general linear-change formulas.

## value

PASS

A natural endpoint Sobolev norm counts each mixed derivative once and is anisotropic under rotations. The theorem gives its full angular distortion profile, sharp maximum sqrt5 away from diagonal axes, and precise cusp behavior, resolving a substantive quantitative gap between the isometry classification and operator norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
