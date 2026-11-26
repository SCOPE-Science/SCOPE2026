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

The squared Gaussian spectrogram at Hermite index j is e^(-x) x^j/j! for x=pi|z|^2, and integration over angle gives the radial measure dx. In particular 1-h replaces all three responses by their complements. For fixed mass p, crossing the thresholds -log(1-p) and -log p gives the lower disk and upper tail first-moment bounds: subtract the threshold times the matching mass, and the remaining integrand difference has fixed sign. Positivity away from the single threshold forces uniqueness on the two edges. At 0<p<1 the interval of mass p has e^(-a)=u, e^(-b)=u-p; its first moment is strictly decreasing in u with derivative log((u-p)/u), and its endpoint moments are precisely q_+ and q_-. At a strict interior pair the two distinct roots a,b are positive and finite. Subtracting the matching zero-th and first moments from the difference in r leaves one half the integral of (x-a)(x-b)(h-h_-), which equals the claimed absolute-value integrand everywhere by sign. It vanishes only for h=h_- almost everywhere. Complementation proves the analogous maximum identity and uniqueness; interpolation of these masks gives every intermediate r, and the edge masks and p=0,1 cases are already forced. The exponential antiderivative gives R. At p=q=1/2, independent 70-digit quadrature and root solving give a=0.435551673686811025..., b=1.917950871301904402..., and r_min=0.291158321988844511...; the last displayed digits of the approximate endpoints in the record differ by floating-point roundoff, without changing the result. See RESULT.md Steps 1–5 for exact replay and checker.py for inspected finite diagnostics only. The identities are interior only, and the claim concerns labelled responses for bounded radial masks, not ordered eigenvalues or fixed area.

## originality

FAIL

The complete attainable body is exactly a classical lift zonoid, and both weighted identities are pointwise support losses in the proof of its general support theorem. The quadratic form and exponential inverse in this application follow by taking the sign of a quadratic and integrating three elementary moments; the paper of Koshevoy–Mosler need not separately list Gaussian channels for this coverage. The failure is for concrete implication by a prior exact theorem, not for inability to inspect some related moment literature.

## value

FAIL

Conditional Hermite calibration is a natural use of the formulas. But under the standard for exact invariants, the proposed result is the existing support theorem for a specific law, with direct score substitution, fitted endpoints and elementary exponential quadrature. Both stability identities are the same general pointwise slack, so they leave no separately supported novel stability claim after removing covered content. Practical convenience in this application does not supply a surviving mathematical finding for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
