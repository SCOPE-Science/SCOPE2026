---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS, limited to the claim as a true special case. Projected coordinate normals have length Lq=sqrt(1-1/(3q)), Monge normals length 2. The nonnegative Z=(C-rLq·1)/(2r) has mixed slacks ≥1, and the dual tent weights u_j=min(2j,q-j),v_j=min(j,2(q-j)) give sum Z≥2 floor(q²/3). Positive interior weights force equality in every Monge slack; complementary coordinate zeros reduce equality to two scalar hinge/quantile minimizations. The resulting center set has dimension 2 exactly when 3|q, 0 otherwise; given tangent-facet strata follow by counting zeros. More decisively independently specialized two published all-rectangular formulas to p=3: (p²q²-p²-q²+gcd(p,q)²)/6=4 floor(q²/3), and center dimension gcd(3,q)-1. Verified this identity exactly for q=4..100 and it follows for all q by three residue classes. Thus the mathematical formulas are correct, though already proved more generally.

## originality

FAIL

FAIL decisive stronger prior coverage. Published 2026-10-18 all-rectangular normalized Monge Frobenius inball theorem states exact r_{p,q}, all centers an affine (gcd(p,q)-1)-cube and facet contacts pq+1-g+e. For p=3, g=1 or3, its denominator becomes 3qLq+4floor(q²/3), its center locus point or 2-cube, and its contact counts 3q or 3q-2+e; this exactly covers the proposed final claim for all q>=4, despite a different parameterization. A second 2026-10-25 all-rectangular theorem independently confirms radius and gcd-dimension coverage. There is no unproved new remainder to repair.

## value

FAIL

FAIL AS AN ORIGINAL CONTRIBUTION. Exact metric incenter and contact counts are natural objects, but the claimed new three-row period-three uniqueness, radius, center parallelogram and all contact strata are direct p=3 consequences of a known all-p,q theorem and complete cube/contact parametrization published 2026-10-18. The bespoke dual tents offer an alternate proof of an already-covered special case, not a separately motivated result beyond that theorem. Computational reproducibility and a correct specialization alone do not establish a fresh valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
