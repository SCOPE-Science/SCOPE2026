---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exponent differences generate the full lattice and the convex hull is the \(5\times5\) square. The six homogenized sections have bidegree \((5,5)\) with no base point, and the dense-torus inverse \(y=z_3/z_2\), \(x=z_2^3/(z_0z_3^2)\) proves birationality. Each facet contains only its two endpoints, separated by lattice length five, so the boundary restriction is a fifth-power map. Thus the normalization is \(\mathbb P^1\times\mathbb P^1\), generic boundary fibers have five points, the boundary is singular and the dense torus is smooth. The degree is the normalized square area, equivalently \((5H_1+5H_2)^2=50\). A fresh arithmetic replay reproduced the lattice-generation, four facet lengths and degree.

## originality

FAIL

The object-specific arithmetic is correct, but the final geometric package is a direct specialization of standard projective toric normalization theory. Cox-Little-Schenck Theorem 3.A.5 states that the normalization of \(X_A\) is the toric variety of the normal fan of \(\operatorname{Conv}(A)\); for this square that is \(\mathbb P^1\times\mathbb P^1\). Classical toric branch theory states that the normalization separates a number of branches equal to the face-lattice index; every edge here has index five. The degree of a projective toric variety is the normalized volume. Those general results, plus the six published exponents, implication-wise determine the submitted normalization, degree and generic boundary branching; smoothness of the dense torus and closedness then give the stated singular locus. Exact wording in the SONC paper is unnecessary for coverage.

## value

FAIL

The support is a useful SONC benchmark and the geometric description is correct, but once recognized as a projective toric variety, the normalization, degree and generic boundary multiplicities follow by textbook normal-fan, normalized-volume and face-index formulas. The remaining singular-locus statement is an immediate closure argument. Under the common value bar this is a routine specialization rather than a new structural theorem or independently nontrivial exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
