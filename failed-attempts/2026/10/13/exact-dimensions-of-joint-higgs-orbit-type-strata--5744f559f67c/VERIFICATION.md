---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the determinant-one stabilizer, the commutant is block diagonal: in each multiplicity space SU(m_α) forces scalar action there, and determinant-one scalar phases across different blocks distinguish them (there is no cross block when s=1). The surviving coefficients are End(E_α) tensored with identity. The weighted trace is surjective, so imposing trace zero subtracts rank one and leaves degree zero. In the invariant Higgs complex, degree zero hypercohomology consists of one scalar per distinct stable factor subject to weighted trace zero; degree two is its dual by the trace pairing and Serre duality (also Cao Lemma 5.5). Riemann–Roch for the two terms gives Euler characteristic −2(g−1)(Σd_α²−1), so degree one has the claimed dimension. Cao Theorems A–B give the vertical tangent identification and the base addition 3g−3. For s≥2, the rank-square sum is bounded by (r−s+1)²+s−1, since Σd_α≤r and moving excess to the largest rank increases the sum. With t=s−1, the half-dimension gap from the bound at s=2 is (t−1)((g−1)(2r−t−2)−1), strictly positive for t>1. A repeated single factor has d≤r/2 and is strictly smaller. The (r−1,1) split exists by pairing a stable degree-zero bundle with its inverse determinant line (two distinct inverse lines in rank two). Subtraction from the stable dimension gives 4(r−1)(g−1)−2. The phrase 'inside the stable stratum' means a dimension gap, not literal inclusion of the non-stable stratum there. The independent integer optimization `python3 /workspace/checks/finite.py 2` corroborated the unique maximizing numerical type for 2≤r≤12, 2≤g≤6, without serving as proof.

## originality

FAIL

Cao already identifies the joint vertical tangent with exactly the invariant complex and gives the two endpoint dimensions, so its rank is a direct Riemann–Roch calculation. More decisively, Bellamy–Schedler gives the exact distinct-factor rank formula for the same weighted types on the fixed-curve Betti side, together with the determinant fiber description. Tensoring every factor by a common character preserves the weighted type, so their étale determinant trivialization subtracts 2g on each stratum, not merely on the whole space. The resulting formula is precisely the claimed fixed-determinant vertical formula. Degree-zero nonabelian Hodge preserves sums, irreducible/stable factors and determinant; the joint addition is Cao’s base dimension. The extremum is the elementary optimizer of this prior weighted formula, not a separate new geometry theorem.

## value

FAIL

Stratum dimension and the top nonstable codimension are useful invariants, but here their exact values carry over from the known weighted stratum dimension through the determinant and base shifts and an elementary rank-partition optimization. No new joint phenomenon or independent stratum distinction is shown; the precise numerical restatement does not meet the requirement of a worthwhile exact fact not mechanically implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
