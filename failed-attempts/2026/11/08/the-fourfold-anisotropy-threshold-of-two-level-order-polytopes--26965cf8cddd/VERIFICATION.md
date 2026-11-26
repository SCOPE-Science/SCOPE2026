---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent moment route conditions on the first upper order statistic S, which is Beta(p+1,q). Given S, the lower coordinates are independent Uniform(0,S); hence their contrast eigenvalue is E[S²]/12 and their block-average variance is E[S²]/(12p)+Var(S)/4. The upper block follows by reflection and interchange. Given S, the upper block has one entry S and q−1 Uniform(S,1) entries, independent of the lower block, so c=(q+1)Var(S)/(4q). This gives the stated tensor. On the longitudinal block the top eigenvalue exceeds both diagonals and both contrast values. The signs of det(B−αI) give the stated minimum: for α_p the deciding factor is q²−p²−3p−3, equal to −p−2 at q=p+1 and p+1 at q=p+2. The α_q comparison is always strict. The all-ones variance is 1/12 because the sum has the unconditional iid-uniform sum law. For q≥p+2, α_p<1/48; for q=p+1 the positive 25 det B−4 tr(B)² is equivalent to κ<4. The balanced formulas and fixed-p limit follow directly (β_+→1/12 and α_p∼(p+1)(p+2)/(12q²)). At p=q, the two contrast subspace dimensions add for the coincident eigenvalue. Reflection of the upper coordinates gives the asserted orthogonal conjugacy.

## originality

FAIL

A distinct October record already gives the full invariant decomposition, switch and balanced condition number for the isometric complete-bipartite stable-set polytope with the same parameters and measure. The remaining threshold formulation and fixed-p limit are direct consequences of its explicit formulas. There is also distinct same-day broader coverage of the moment tensor.

## value

FAIL

This is a natural covariance problem, but after accounting for the known full spectral decomposition and mode switch, the fourfold split and fixed-p leading term are routine algebraic consequences, not a standalone substantive advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
