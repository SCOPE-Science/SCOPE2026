---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. Rectangular tetrahedron T=conv{0, ae1,be2,ce3} with arm anisotropy R>1 has total normalized vertex solid angle Σ=1/2-(1/(2π))∑arcsin((1/a_j)/sqrt(∑1/a_k²)). This follows from spherical excess counted twice over six dihedral edges. With arms (1,R/t,R), 1≤t≤R, derivative sign is that of sqrt(R²+1)-Rt/sqrt(1+t²)-t/sqrt(R²+t²); its comparison function is strictly increasing, below/above target at endpoints, ensuring unique strict interior minimum. Root asymptotics t³/R²→1/2, b=R/t~(2R)^(1/3); arctan expansion yields Σmin=1/4-1/(2πR)+3/(2^(8/3)π)R^(-5/3)+o. R=1 explicitly excluded from interior claim. Read included independent trihedral-det formula checker; direct numerical recalculation independently compared angles and stationary roots. All-R proof is analytic, not mesh enumeration.

## originality

PASS

PASS on best-of-knowledge evidence for the fixed-perpendicular-arm-ratio optimizer of the total *sum* of vertex solid angles, its unique interior root and cube-root fractional asymptotic. Kabluchko–Schange Theorem8.5 supplies general individual angle formulas for orthocentric/right simplices but no optimization under fixed anisotropy; Licht Theorem1.1 bounds the *minimum individual* angle against fullness, different functional. Resultary search found related minimum-angle orthoscheme and sharpness results, not the same total-angle constrained variational theorem. This is a conditional historical originality judgment, not absolute priority proof; older tetrahedron shape measure work may contain equivalent optimization.

## value

PASS

PASS. Total normalized solid-angle mass is a natural tetrahedral shape invariant, and fixing extreme orthogonal arm anisotropy is a geometrically meaningful constraint rather than arbitrary slice. Optimizer is strictly nonboundary, characterized for every R>1 by a sharp monotone equation; the 1/3 scaling and noninteger R^(-5/3) correction are nontrivial and not determined by merely knowing separate angle formulas. Independent self-contained asymptotic fact can be useful in comparing right-corner simplex shapes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
