---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The finite iid rates define a continuous nondecreasing operational clock A_t, independent of the unit-rate symmetric walk. Conditional time change is valid including zero-rate intervals. Reflection gives survival at operational time a from x as the sum of the unrestricted kernel at displacements 1−x through x. This is between h_1(a) and 2x h_1(a), since every term is at most the mass at 0. Monotonicity sandwiches the mean between the positive-epoch and zero-included epoch sums times τ. At epochs the clock has transform φ(τs)^m; the h_1 Fourier kernel 1+cos θ is nonnegative so Tonelli sums it to the resolvent even in the divergent case. Only θ=0 is singular, since P(R>0)>0; s=τ(1−cos θ) gives a Jacobian comparable to s^(−1/2) near zero. Karamata yields the asserted Laplace deficit for 0<α<1, Potter bounds separate the strict power cases, and u=1/s gives the critical integral and the strict cutoff κ>1. The proposed critical tails are continuous, decreasing above their cutoff and tend to zero. No positive or finite moment is used. The finite checker was inspected, not executed, and cannot establish convergence at the critical endpoint.

## originality

FAIL

The primary predecessor provides the exact same-model survival for general rate laws, including the block-Laplace product. Specializing to x=1 and full epochs and summing its nonnegative geometric series gives the claimed iff directly. The older Appendix A does not state the arbitrary slowly varying cutoff and must not be read as ruling out finite mean at index 1/2. But the cutoff is the direct substitution of the standard Laplace form of Karamata's theorem into that resolvent, with no additional model-specific estimate. An independent theorem beyond these implications is not established. The later indexed overlaps are separately recorded and are not the basis of a priority claim.

## value

PASS

The critical boundary is meaningful: two realizable rate tails with the same power index yield opposite mean first-passage behavior, so the power index does not decide the passage question at equality. The arbitrary-law condition is also a practical test. Their mathematical coverage by earlier results is the separate reason the frozen finding does not pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
