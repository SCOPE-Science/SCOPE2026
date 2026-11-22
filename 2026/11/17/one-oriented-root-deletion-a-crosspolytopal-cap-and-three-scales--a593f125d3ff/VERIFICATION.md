---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Let P=conv(e_i−e_j, i≠j) and Q delete v=e1−e2; φ=x1−x2 singles out φ(v)=2, all other roots φ≤1. Segment intersections show P∩{φ≤1}=Q, and the section F at φ=1 is the 2(n−2)-vertex crosspolytope centered v/2. Its opposite directions w_j have Gram I+J/2, determinant n/2. The pyramid height is 1/√2; facet-volume and difference-body simplex formula yield the lost Euclidean volume 2^{n−3}√n/(n−1)! and relative 2^{n−3}/binom(2n−2,n−1), with correct n=3 boundary. Projection v/2 proves directed Hausdorff gap. A root is exposed precisely by ordered max/min coordinates, so for deleting v width changes iff the two Gaussian extreme labels equal {1,2} in either orientation, probability 2/[n(n−1)], with loss min(top gap,bottom gap)/||g−mean g||. Independent Gaussian extreme-order exponential spacings and s_g/√n→1 give conditional √(2n log n) loss⇒Exp(rate 2). Fresh Qhull calculations n=3..6 and deterministic support tests support these calculations but are not general proofs.

## originality

PASS

Comparisons made against specific mathematical statements, with natural aliases, stronger/other model hypotheses and integral versus finite-field distinctions; same-finding indexed hit not counted as independent earlier coverage.  Restricted bibliographic coverage remains as residual risk.

## value

PASS

A canonical highly symmetric polytope exhibits three sharply separated sensitivity scales after a single natural vertex fault: constant Euclidean Hausdorff loss, exponentially small relative volume, and polynomially rare width loss with universal conditional exponential law. The exact formulas quantify a structural robustness comparison, beyond merely evaluating an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
