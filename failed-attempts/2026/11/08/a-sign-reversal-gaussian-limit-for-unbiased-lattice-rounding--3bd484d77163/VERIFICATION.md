---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Common-uniform rounding couples two integer transition laws with W1 contraction r<1. The positive branch has closed states {0,1} and unique stationary Bernoulli(theta); the negative branch has stationary conditional variance identity (1-r^2)V=E psi(2theta+(1-r)(X-theta)). Tightness of (1-r)(X-theta) and continuity at noninteger 2theta give the proposed variance asymptotic. The adapted-noise coupling against i.i.d. Bernoulli(p) has mean-square vanishing normalized error, and a weighted triangular array with maximum coefficient sqrt(1-r^2)->0 proves the Gaussian limit, not merely a variance claim. Independently solved several finite rational chains and checked scaled variances; all-order conclusion rests on the coupling proof.

## originality

FAIL

An earlier published result on 2026-11-02 proves the exact SAME negative-branch recursion R((1+q)theta-qX,U), q=r, the stationary measure, divergence constant psi(2theta) and the same Gaussian limit. It gives strictly stronger uniform error bounds, half-grid exception, and lag covariances. The only addition of this later work is the positive +r Bernoulli stationary law, an immediate elementary consequence of unbiased rounding and invariant {0,1}; it cannot sustain an original overall theorem. Relabeling q as r or describing the negative process as affine iteration rather than gradient descent does not evade prior implication.

## value

FAIL

The near-critical Gaussian law and nonresonance constant are already published. The added positive-slope branch is a routine closed-two-state Bernoulli observation; the comparison is mathematically illustrative but not a new motivated gap once the stronger theorem is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
