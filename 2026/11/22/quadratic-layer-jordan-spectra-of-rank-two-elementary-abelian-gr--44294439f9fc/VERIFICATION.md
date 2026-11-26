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

In the truncated polynomial presentation, all maximal-ideal elements have pth power zero, so any invertible first-order coordinate substitution extends to an automorphism. A nondegenerate symbol becomes xy after extension and a scalar normalization; each higher homogeneous term xU+yV is removed by correcting x and y in degree one less. The ranks are then (p−t)² by counting the image monomials. For a rank-one symbol, after setting it to x², successively substituting x−H/2 removes each xH of lowest unwanted degree and fixes y. Free pure-y inputs add to the residual polynomial, giving fibers of size q^(p²−p−3). For a coordinate-independent check of s, the gradient ideal is well-defined since derivatives of x^p and y^p vanish. Under an automorphism the chain rule applies with invertible Jacobian. The gradient quotient of x²+h(y) has dimension s−1 for nonzero h of order s<p, and dimension p for h=0, so s is intrinsic. Taking a truncated s-th root of the unit in h and, if necessary, adjoining a root of its leading coefficient gives x²+y^s. On each pair of exponent chains, the tensor sum is multiplication by u+v in k[u,v]/(u^a,v^b). For i<min(a,b), the determinant of its middle pairing from grade i to a+b−2−i has factorial ratios with arguments at most a+b−2, so the characteristic-zero strings survive here since a+b−1<p. This gives the displayed lengths including b_j=1 for h=0. The discriminant-zero cone has q² points including zero, and the residual-order fibers give both stated multiplicities and the full layer sum. An independent bounded p=5 run checked direct matrix ranks on transformed representatives of the nondegenerate type and all three residual orders. The all-p and all-extension conclusions rely on the proof, not the finite checks.

## originality

PASS

Credit the known characteristic-three censuses, formal splitting, and small-chain Jordan rule. The distinct contribution is the first nonlinear layer distribution for rank two and p≥5, especially the singular rank-one strata, their lift multiplicities, and their conversion into a full spectrum over every extension.

## value

PASS

This is a natural full finite-field census on the first layer not controlled by nonzero linear direction. It shows both rigidity of the smooth quadratic strata and exactly how higher lifts can change a singular quadratic multiplier, with all power-rank data and the number of occurrences over every extension. The joint classification and weights are useful beyond merely evaluating a known rule on a few normal forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
