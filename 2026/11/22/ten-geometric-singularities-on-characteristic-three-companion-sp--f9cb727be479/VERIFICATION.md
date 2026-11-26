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

Independent exact recreation from the expanded b=1 equation found no infinity-chart or F3-rational Jacobian zeros and verified b=-1 by u↦−u. Using Euler (5 is invertible modulo 3) and F5B elimination on f and its three affine partials gave the stated two linear relations and univariate factors of degrees/multiplicities (2,1),(2,1),(6,3), hence exactly ten geometric points and length 22. Hessian determinants in both quadratic residue fields were u−1, and at the sextic factor the first and third Hessian rows had nonzero cross product spanning the kernel. The cubic Taylor coefficient computed using that alternate null vector was −u^5+u^4+u^3−u−1, nonzero modulo the irreducible sextic; no ordinary third-derivative assumption in characteristic three was used. The local algebras follow by scalar extension and factorization; a multiple component or the intersection of two distinct hypersurface components would force a positive-dimensional singular set. The Frobenius point count follows by divisibility of orbit lengths.

## originality

PASS

Best of current evidence: the new claim is the exact geometric Jacobian algebra and local behavior for the specified pair, not the companion construction, absence of rational singularities, or computational nonsmoothness. No inspected source gives the orbit degrees and local multiplicities or determines the Taylor behavior. The original run output was not read, so historical priority is not certified.

## value

PASS

This resolves the local geometry behind a natural minimal-degree space-filling construction's characteristic-three nonsmoothness. The support split and Jacobian lengths distinguish the four ordinary nodes from the six corank-one points and give exact obstruction data over every extension; they are not merely another smoothness flag. The information is useful when analyzing modifications of the construction or comparing characteristic-three singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
