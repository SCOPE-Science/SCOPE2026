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

The projected box is a planar zonotope; the absolute planar determinants of its three pairs of projected edge generators give x|U₁|+y|U₂|+z|U₃| for (x,y,z)=(bc,ac,ab). Independently expanding in centered coordinates Y_i=|U_i|−1/2 gives E[Y_i³]=0 (each |U_i| is uniform on [0,1]), E[Y_i²Y_j]=(5π−16)/(24π) for i≠j, and E[Y₁Y₂Y₃]=(π−3)/(4π) by the Dirichlet(1/2,1/2,1/2) monomial integral. With s=x+y+z, q=xy+yz+zx and p=xyz, this yields κ₃=(5π−16)(sq−3p)/(8π)+6(π−3)p/(4π), or κ₃=[3(4−π)p−(16−5π)sq]/(8π). Here p=V² and sq/p=9+Σ_{i<j}(x_i−x_j)²/(x_i x_j); the latter terms are the stated pairwise side-length energies because x_i=V/a_i. Thus the coefficient is strictly positive in the deficit and the cube value 3(7π−22)/(4π) is strictly negative. Equality in the upper bound is precisely equal sides. The area is not constant (a slight tilt from any coordinate axis increases it to first order), so the sign carries over to standardized skewness, not the proved extremum.

## originality

PASS

Credit the classical brightness formula and prior distributional work, and do not credit raw moments as a standalone contribution. The identified available exact-moment statements do not contain the cubic coefficient for all boxes, and no checked statement gives or mechanically yields the universal sharp negative central moment with its aspect-ratio deficit. Integrating a known cuboid density determines the moment in principle, but the comparison did not find a passage that reduces the signed sharp identity to a stated formula. The unresolved tomography lead is material: if it contains exact raw moments through order three, the centralization and factorization would be a direct corollary.

## value

PASS

Beyond calculating a moment, this resolves a uniform sign question for a classical geometric observable: single-coordinate cubic contributions vanish, correlated viewing coordinates drive the sign, and the exact cancellation separates a negative cube term from a nonnegative shape penalty. The penalty gives strict equality and quantitative departure from cubic shape at fixed volume without needing to integrate the cuboid PDF case by case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
