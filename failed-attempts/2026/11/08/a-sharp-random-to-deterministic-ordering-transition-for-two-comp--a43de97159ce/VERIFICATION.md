---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For fixed a>b>0, u!=v, h>0, the two proximal compositions have common contraction r=1/((1+ha)(1+hb)), independent offsets differing by Delta=h^2ab(u-v)/((1+ha)(1+hb)). The stationary mean displacement from the original quadratic average minimizer is Delta(p-a/(a+b))/(1-r), and variance Delta^2p(1-p)/(1-r^2). Their sum gives equation (1). The second derivative of the bracket is 4r/((1-r)^2(1+r))>0, yielding the clipped unique p*(h), boundary (1+ha)(1+hb)=(a+3b)/(a-b), and exact small-h leading coefficients. At u=v the stated nonzero-gap uniqueness fails, but u!=v is explicitly assumed; h>0 keeps r in (0,1). The provided exact-rational verify.py was inspected, not accepted merely from its 15,624-assertion report.

## originality

FAIL

FAIL because prior published full mathematical result for explicit-gradient two-component affine-epoch reshuffling determines stationary mean, variance, strict convexity, biased-optimal permutation and the same random-to-deterministic transition. This proximal case follows by replacing explicit component curvatures with ha/(1+ha), hb/(1+hb) at unit explicit step, translating the component minimizers and changing the risk reference center from effective to original objective. That target translation is elementary quadratic algebra; neither label nor different step parameter supplies an independent theorem.

## value

FAIL

The optimizer is sensible and exact, but its analytic risk curve, clipping and order transition are the mechanical two-affine-map specialization of the stronger already published stationary-moment formula. No additional nontrivial parameter dimension, obstruction, or independently motivated invariant remains after the reduction; the O(h^3) vs O(h^2) distinction is covered by the same expansion. Reject novelty and independent value while retaining correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
