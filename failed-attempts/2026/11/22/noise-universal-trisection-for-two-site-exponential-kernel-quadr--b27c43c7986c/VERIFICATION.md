---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Integrated the kernel to recover m(t) and Q, and diagonalized the observation covariance in the sum/difference directions (a=1+η>1, hence both eigenvalues are positive even for repeated sites). At fixed scaled half-separation s∈(0,L), L=λ/2, write C=cosh(λ(c−1/2)). After factoring C−1, the shifted-minus-centered gain has the sign of −2cosh(s)+e^(−L)(C+1)[cosh²(s)+(a+e^(−2s))/(a−e^(−2s)) sinh²(s)]. The bracket is smaller than cosh(s)e^s; the feasibility bound C≤cosh(L−s) then makes the sign strictly negative. At s=0 direct maximization chooses the midpoint, and at s=L there is only one center. For centered configurations differentiation gives the sign of G(s)=e^L−e^s−ae^(2s)sinh(s), strictly decreasing and of opposite sign at the two ends. Thus the unique maximum is interior and the sites never coincide for finite positive noise. Conditional weights and variance follow from the sum eigenvector. At η=1, s=L/3 by the exponential identity e^s+2e^(2s)sinh(s)=e^(3s); writing u=e^(−λ/3), m=(1−u)(2+u)/λ, so w=(1−u)/λ and the captured variance cancels to the stated residual. Strict noise monotonicity follows directly from the decrease of G in both s and a. The label ‘weak-correlation’ used for λ↓0 is reversed (this is the near-constant-kernel limit); the limit formula itself is correct.

## originality

FAIL

Exact coverage by a distinct indexed theorem was verified, not merely a same-title or same-date hit. The general precision-budget theorem optimizes a larger design space, but its unique maximizer at n=2,P=2/η has both precisions exactly 1/η, so it belongs to the fixed-equal-variance space and remains its unique maximizer. Its equation, weights, risk and universal P=n transition give the frozen finding, including the strict noise shift by immediate monotonicity of the same root equation. No distinct scientific claim beyond this coverage is established in the frozen Finding. This is a failure to establish a distinct claim against documented coverage, not a finding that the general record was published first or that the frozen proof is incorrect. The general record's text refers to an unnamed previously established two-site theorem, consistent with the reverse order, but does not identify the reviewed record or establish the order.

## value

PASS

The scientific question is worthwhile: independent observation noise and the unknown integral are standard, and the exact finite-site law exposes an unexpected range-parameter-independent transition and strict noncollision not predicted by error rates. The direct proof of unique reflection centering at every fixed separation is informative, beyond merely numerical gains. This assesses the usefulness of the theorem and proof; documented broader coverage prevents a separate originality pass for the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
