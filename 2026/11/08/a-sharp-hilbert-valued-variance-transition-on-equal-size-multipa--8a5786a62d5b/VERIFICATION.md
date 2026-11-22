---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

From actual frozen RESULT.md, let A mean within-class variance and B variance of class centroids. The exact averaged cross-distance inequality gives (r-1)A+rB <=(r-1)/2 and internal pair identity gives A <= C=(m-1)t²/(2m). Consequently the upper envelope is min{1/2,(r-1)/(2r)+C/r}. The orthogonal within-class regular-m-simplex and class-center regular-r-simplex Gram model saturates below t_*²=m/(m-1); above it a common-center family of orthogonal centered regular simplices with squared norm 1/2 saturates universal 1/2. The exact nonnegative cross slack proves all cross distances equal 1 at saturation; B=0 and r>=3 force A_i+A_j=1 hence A_i=1/2, equal radii, and all cross inner products zero, with within distances <=t sufficient. At/below boundary, within cap also saturates so every pair distance equals its metric cap; double-centering fixes isometric Gram and rank rm-1 below, r(m-1) at boundary. At t=2 each centered equal-norm class requires dimension>=1 (even m) or >=2 (odd m), realized by balanced antipodes or centered regular m-gon, with orthogonal class spans; dimension minima r/2r. Independently written exact SymPy Gram/rank checker verified 45 sampled r,m,t² witnesses and small-case eigenvalues plus endpoint polygon examples for m=2..11. No finite check is substituted for general proof.

## originality

PASS

Qualified best-of-knowledge PASS for the COMPLETE r>=3 Hilbert sharp variance and especially nonisometric plateau equality classification and endpoint minimal-dimension parity. IMPORTANT partial coverage: the November 2 published all-multipartite negative-type theorem ALREADY implies the t_* threshold, rank collapse and (with elementary pairwise identity) the isometric-side variance. The separate r=2 published Hilbert variance theorem is a same-functional precedent. Those parts are not regarded as novel. The complete post-threshold r>=3 equality/dimension classification remains unproved by inspected prior claims. Search absence is not proof of priority.

## value

PASS

After removing prior-known negative-type threshold, isometry branch, and rank jump, this is still an exact nonexpansive vector-valued variance law for a natural r>=3 family whose nonisometric phase requires an equality classification not furnished by embeddability alone. The all-optimizer decomposition into orthogonal equal-energy class configurations and sharp parity-dependent minimum target dimension at t=2 answer natural precision/dimension questions; the 3+ class rigidity differs materially from the r=2 degenerate LP. Proof is short but structural; the fact is not just a named substitution or known table recomputation. Limitations: no arbitrary weights/unequal sizes, and no minimum dimensions for every intermediate plateau t.

The dated certificate retains the supplied scientific assessment, sources and limitations.
