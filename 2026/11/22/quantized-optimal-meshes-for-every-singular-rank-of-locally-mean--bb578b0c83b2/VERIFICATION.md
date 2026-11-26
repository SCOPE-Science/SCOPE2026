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

Each cell integral of (I−P)f vanishes, so no contribution propagates between cells. On each cell the constant is killed and normalized nonconstant cosines are mapped into the complete sine basis with coefficients h/(mπ). This gives every positive singular value and its multiplicity, and compactness. For t>0 the number strictly above t on cell j is q_j=ceil(h_j/(πt))−1, including thresholds exactly on a ladder. Taking t=s_k yields 1=Σh_j≤πt(N+Σq_j)≤πt(N+k−1). Equality requires both Σq_j=k−1 and equality on each cell separately; conversely every positive composition of N+k−1 yields exactly k−1 values above the threshold and one value at it from every cell. This proves attainment and rules out any other ordered mesh. The uniform value 1/[πN ceil(k/N)] gives the asserted congruence including N=1, and the k=2 examples increase the operator norm for N≥2. Summation of the complete ladders gives divergence for 0<p≤1 and the stated zeta formula for p>1; strict convexity gives the unique global minimizer. The exact-rational checker was inspected without execution; its finite ranks and grids do not prove the all-rank optimization.

## originality

PASS

Best-of-knowledge pass for the exact optimum and complete ordered equality set for every indexed rank. The cellwise Dirichlet ladder, direct-sum viewpoint and Schatten convexity are classical inputs or immediate consequences, not stand-alone novelty. The decisive combined-spectrum optimization and tie rigidity are not supplied by the inspected sources.

## value

PASS

Mesh design for a target singular rank is a natural objective distinct from minimizing total error or the worst-case norm. The exact equality set answers which meshes improve a desired index and when a uniform mesh is already optimal. The all-index quantization, attained rigidity and explicit second-rank tradeoff are the useful content, rather than calculating the classical one-cell eigenvalues again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
