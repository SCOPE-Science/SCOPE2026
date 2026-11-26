---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reading Eq. (25) with f(y)=-lambda*y and multiplying by D=(3-kappa)(1+kappa) gives exactly the stated B and C. For q=1/(1+z), expansion gives p(q)>0 and 2q>B, so q is strictly above the largest real root whenever real roots exist. For kappa<=1/2 the discriminant is nonnegative through z_c=(1+kappa)/(2(1-kappa)) and B>=0 there. When C<=0 the nonnegative recurrence coefficients suffice; otherwise the two nonnegative roots and the start above the larger one give nonnegative iterates (including the repeated-root solution). Beyond z_c the complex-root sinusoid must have a negative iterate: it either samples a negative arc densely or sums to zero on a nontrivial finite rotation orbit with positive initial value. For kappa>1/2, z_a=(1-kappa^2)/kappa is the B=0 point with C<0 there and below. Beyond z_a, C>=0 gives y_2<0, whereas C<0 gives a larger-modulus negative root with strictly negative coefficient because q exceeds the positive root, forcing eventual negativity on even indices. This verifies inclusivity and the degenerate B=C=0 endpoint, and the strict branch monotonicities give the unique optimum. An independent rational replay gives first negative n=97 at kappa=0, z=R+1/500, and n=824 and 2266 at kappa=2/3 and 9/10 at the same offset, respectively; no finite cap is used for the theorem.

## originality

FAIL

The distinct indexed November 2 positive-start phase diagram completely covers the fixed-start claim. Its A,B are the frozen B,C and its positive ratio w can be set to q=1/(1+z). Where the admissible set is w>=lambda_- this q qualifies by p(q)>0 and 2q>A; where only w=lambda_+ works it does not qualify, by the very same identities. The all-ratio and no-ratio branches are immediate. The resulting boundary is z_c for kappa<=1/2 and z_a above it, with the same degenerate endpoint and unique maximum. It is the full ratio classification, not the all-start radius alone, that gives this coverage. This is a coverage verdict against the current catalogue, not a claim about historical priority. The stronger record is dated later and explicitly refers to an earlier backward-Euler special result.

## value

FAIL

The sharp switch and damping optimum are meaningful for the chosen starter, but as a standalone additional contribution this is now a fixed-ratio evaluation of the existing complete phase diagram. The frozen claim contains no independently unknown threshold, stronger scope, or separate result beyond the covered slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
