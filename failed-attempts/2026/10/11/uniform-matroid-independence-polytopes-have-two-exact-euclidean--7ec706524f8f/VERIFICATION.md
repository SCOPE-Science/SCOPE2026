---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Full S_n symmetry and lower coordinate clearances give r>=sum c_i+rho sqrt(n)>=rho(n+sqrt(n)); opposite facets when r>=2 give rho<=1/2, and the displayed centers achieve the smaller bound, uniquely by equality. For minimum enclosing sphere S_n-invariance forces center t*1; a weight-k 0/1 vertex has squared distance nt²+k(1-2t), whose maximum over 0<=k<=r is attained at k=r for t<1/2 and at k=0 for t>1/2. Exact scalar minimization yields the two-phase radius/center/contact classification. For r=1 upper coordinate inequalities are not facets and are handled correctly. Independently checked boundary regimes and numeric samples n=9,16,20; finite checks are not the proof. All equations are mathematically valid.

## originality

FAIL

Two already published exact results jointly cover the entire claimed final statement, despite having different titles. The published general matroid independence-polytope minimum-sphere theorem gives for U_{r,n} the very same unique outer center, squared radius and contact vertices in its equations (2),(3)-(6),(11),(17). The published capped-hypercube John ellipsoid theorem analyzes exactly K_{n,tau}=[0,1]^n cap {sum x_i<=tau}, explicitly says integer tau are uniform-matroid independence polytopes, and establishes complete halfspace inclusion constraints s<=t, s<=1-t, nt+sqrt(n b)<=tau. Specializing to isotropic balls a=b=rho² (so s=rho) and symmetrizing centers gives rho<=min(t,1-t,(r-nt)/sqrt(n)); optimizing these displayed inequalities is a routine one-variable step yielding the inradius min(r/(n+sqrt(n)),1/2) and the same transition and tangent facets. Both components and their contact phases are therefore direct consequences of existing published results. Originality FAIL does not deny the submitted elementary proof.

## value

PASS

The two distinct rank thresholds describe the natural Euclidean roundness of a canonical combinatorial polytope and the full contact regimes. The structure is mathematically motivated and exactly proved, but this does not make its already-covered content original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
