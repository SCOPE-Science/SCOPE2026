---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Under threshold-one parallel firing on forward C_n, each initially occupied binary site fires and translates the support exactly one vertex per step. Hence facets F_i={i,i+1,i+d,i+d+1}. For d≥3,n≥2d+2, e_i={i+1,i+d} is the unique edge of unoriented length d−1 within F_i, so a_i={i,i+1,i+d} is free in the tetrahedron and after all n such collapses e_i is free in b_i={i+1,i+d,i+d+1}; these are exactly 2n valid elementary collapses. Residual A_i={i,i+1,i+d+1} and B_i={i,i+d,i+d+1} form a connected orientable closed 6-regular triangular surface for n≥2d+3 (six distinct cyclic neighbors, opposing edge orientations), with face vector (n,3n,2n), χ=0, hence a torus. At n=2d+2 the antipodal length d+1 edge class has n/2 edges, so χ=n/2=d+1, excluding a torus. Independent finite face computation gave boundary (d,n)=(3,8) f=(8,20,16), Betti=(1,1,4); stable samples (3,9),(4,11),(5,14) had Betti=(1,2,1). This does not replace the all-parameter collapse proof.

## originality

PASS

No verified broader or equivalent prior statement implies the precise final claim after reading the identified primary theorems and searching published findings. This is a best-of-knowledge novelty assessment with the material access and indexing limitations explicitly recorded; published inputs and exact known subclaims are acknowledged.

## value

PASS

The avalanche complex is a concrete dynamical object, not merely a known cyclic torus. The explicit 2n free-face collapse identifies the invariant homotopy and cup product, and the immediately preceding antipodal threshold has a mathematically sharp Euler-characteristic obstruction. The reduction is a motivated structural response to classification of avalanche types by chip configuration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
