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

Normalize the centers to 0,D; this preserves the positive weight magnitudes. For a scalar rank-two compression, the min–max principle already gives Re(e^{-iθ}z) ≤ λ₂(Hθ). With u=D cos θ, the four eigenvalues are ±r and u±s. For |u|≤r+s the second is min(r,u+s), so if D≤r+s the inequalities give precisely the disk intersection as an upper bound. Every point of that intersection is achieved by a pair of unit vectors, one in each block, with the prescribed scalar expectation (the numerical range of a 2×2 Jordan block is the disk). At D>r+s the directions cos θ=±(r+s)/D, each with both sine signs, force Im z=0 and Re z=Dr/(r+s). An isometry with block components √(s/(r+s)) I and √(r/(r+s)) diag(1,−1) attains it by exact off-diagonal cancellation. This establishes the formula even without sufficiency of the general half-plane characterization. Coincident centers, containment/tangency and external tangency follow directly; the normal limit is the whole segment since weighted block copies of the identity realize every point and ordinary expectations bound the range by the segment. Eventually the separated formula applies along every stated vanishing-weight path; all ratios, including both endpoints, can occur in the limit.

## originality

PASS

Credit the known higher-rank half-plane characterization and normal segment. The supported distinct claim is the explicit weighted two-active-block phase law, including the persistent singleton outside both disks' intersection and the selection of arbitrary points of the limiting segment by weight ratios. The available statement-level comparisons do not cover this classification. The overlap phase alone is not the basis for the pass.

## value

PASS

The smallest pair of independently nonnormal Jordan blocks gives an explicit minimal-dimensional test family for scalar compression. The persistent unique compression beyond disk overlap, its radius-weighted location, and the ability to select every point of a much larger limiting range isolate a meaningful instability; this is more than a finite numerical check or a restatement of convexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
