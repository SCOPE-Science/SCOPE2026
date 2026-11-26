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

Integrating the interior measure D²f twice gives a hinge integral modulo an affine function. The affine part is reproduced for n≥1. The triangle inequality gives the upper norm bound and a hinge at a maximizing interior knot attains it (the endpoint residuals are zero, whereas each interior residual is nonzero). In equality, pairing the signed residual integral with its own unit direction forces almost every signed residual to be the same maximal vector. Their second distributional derivatives have atoms at their respective knots and otherwise are smooth, so this is possible only for a single knot. For the factorization, write a=t(1−t), J_j=P_j^{(1,1)}(2t−1). The shifted Legendre differential equation gives c_j′=−aJ_{j−1}/j; the weighted Jacobi equation integrated from 1 gives c_j=a²P_{j−2}^{(2,2)}(2t−1)/(j(j−1)) for j≥2. The difference J_{j−2}/(j−1)−J_j/(j+1) vanishes at both endpoints; its quotient by 1−z² is orthogonal with weight (1−z²)² to degrees ≤j−3 and leading coefficients give the stated connection constant. This proves that the difference between successive proposed derivatives equals −2(2j+1)c_jc_j′; the degree-one base is a³/3. Jacobi interlacing supplies exactly 2n−1 simple interior stationary points, and parity and positive leading coefficients give the stated strict midpoint signs. The degree-two maximizing a is 1/5, while the degree-three candidates a=1/7, 1/5, 1/4 give 1/7203, 1/9375, 1/3072, respectively; degree one peaks at a=1/4. These verify both constants and knot sets. The frozen SymPy checker was inspected, not executed; its reported finite identities are not the all-degree proof.

## originality

PASS

The strongest open prior work supplies exact Legendre coefficient representations and general error bounds, including input from which the hinge coefficients can be obtained. The supported distinct claim is the exact curvature-variation projection norm via the explicit all-degree Jacobi stationary law and its knot classification, not the general hinge reduction or Jacobi coefficients alone.

## value

PASS

The sharp norm over a natural variation ball is reduced to a finite exact list for every degree, rather than a bound or a search over all knots. The equality rigidity and the first three global cases show why selecting a knot matters; already at degree two, the midpoint is not worst. This is useful independently of any new global classification of the maximizing roots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
