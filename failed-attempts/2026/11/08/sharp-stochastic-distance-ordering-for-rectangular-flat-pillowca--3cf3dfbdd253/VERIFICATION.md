---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the torus quotient T/(z∼−z), d_P([x],[y])=min(d_T(x−y,0),d_T(x+y,0)). The endomorphism (x,y)↦(x−y,x+y) is onto, so the two components are independent Haar and the exact CDF is 1−(1−H(r))². Uniform shortest torus representatives in [−a/2,a/2]×[−b/2,b/2] give H as a disk–rectangle area, and the four elementary branches follow integration of min(B,sqrt(r²−x²)). With fixed product, differentiating the rectangle disk-overlap in log aspect yields J′≤0, strict for B<r<R, proving all-threshold square dominance. Corner triangles give torus survival ∼2(a²+b²)/(a²b²) ε²; squaring gives 4(a²+b²)²/(a⁴b⁴) ε⁴. The endpoint, strictness, and normalization are consistent; checked the circular-segment formula independently. Arbitrary-lattice group identity does not imply rectangular optimization outside stated scope.

## originality

FAIL

The complete November 1 Schur-ordering theorem for orthogonal flat torus inversion quotients in every dimension d≥2 already supplies exactly the same squared-survival distribution, the full explicit planar rectangular CDF, full log-majorization stochastic order, unique square optimum, and terminal ε^(2d) tail with exact coefficient. Specializing d=2 recovers the November 8 submitted theorem, including its fourth-order coefficient. This is full stronger prior mathematical coverage; the alleged new planar results are corollaries.

## value

PASS

Complete geodesic pair-distance laws and exact rectangle-shape stochastic optimization for a natural singular flat orbifold are meaningful geometric-probability invariants. The closed diameter-tail coefficient is mathematically motivated. These facts are nevertheless already covered by the earlier stronger all-dimensional exact theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
