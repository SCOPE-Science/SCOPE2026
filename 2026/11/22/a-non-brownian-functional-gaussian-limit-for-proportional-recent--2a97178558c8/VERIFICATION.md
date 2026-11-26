---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The exact past window gives the displayed innovation and coefficient recurrence, and the cited Hu–Xue Lemma 3.6 applies to the same indexing and normalization. For a<=0 the update is a convex combination; for a>0 the nonnegative differences have a unit source at k. Beyond j>bk for b>1/(1-c), the source has exited the lag window and the comparison profile k^(-gamma) j^(gamma-1) is a strict supersolution for all sufficiently large j. At gamma=1/2 the limiting comparison multiplier is 2a/(1+sqrt(1-c)), strictly below one in the asserted regime, so gamma can be moved strictly below 1/2. The resulting square-sum and maximum bounds justify the early-index cutoff and martingale Lindeberg condition. Azuma and Borel–Cantelli give vanishing recent-window bias, so the predictable variance tends to the deterministic Gram limit. For i>=j/2 the old indices have squared increment sum O((j-i)^2/j), and new indices contribute O(j-i); for i<j/2 use the individual square-sum bounds. This gives the fourth-moment tightness bound for grid points and, by the deterministic slope bound and splitting fractional steps, also for the interpolation. The Wiener kernel inherits the growth bound, which gives square integrability and permits differentiation and integration by parts. The DDE is interpreted in the standard fundamental-solution sense (locally absolutely continuous on nonnegative time, equation a.e. or with right derivatives; it can have a kink at L because prehistory jumps at zero). On (0,L), w=exp(av/c); global discrete comparison gives w<=1 or w>=1, making the variance comparison with one strict when a!=0. Self-similarity plus stationary increments would force covariance sigma^2 min(s,t), contradicting the nonzero right slope. At neutral memory the kernel is one. The bundled exact finite tests were inspected, not executed or used as path-limit evidence. No endpoint or critical-regime conclusion follows.

## originality

PASS

The exact model, scalar variance and compact deterministic kernel approximation are prior inputs. The new claims are the process-level convergence, its off-diagonal covariance and the sign test for nonstationary increments. The inspected prior process limits do not cover the hard proportional window.

## value

PASS

The result distinguishes Brownian scaling from Brownian dynamics in the exact model previously understood at one time. The full cross-time law supports path-dependent observables, and the elementary right-slope identity detects both the presence and sign of memory rather than merely giving a formal functional extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
