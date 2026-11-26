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

For the zero-initial serial linear filters in RESULT.md, the response derivative is positive before and at shutoff. After shutoff it is proportional to (1−exp(−sL))exp(−sτ)−(1−exp(−rL))exp(−rτ); the ratio decreases from greater than one to zero. The equal-term equation gives precisely the stated lag. Differentiating verifies strict decrease since x/(exp(x)−1) strictly decreases; the logarithmic Taylor expansion gives the stated endpoints and direct differentiation at large L gives τ′∼−rτ, justifying the inverse-sensitivity law. The two strict endpoint comparisons imply at least one crossing for an open parameter family, not uniqueness in general. For the displayed pair, independently expanding the polynomial gives z(z³−z−1)(z³+z²−1); its second cubic is strictly increasing on (0,1) and the first is negative there. The unique root is z≈0.754877666246692760 and −log z≈0.2811995743229618465; decreasing z as L increases gives the stated signs. Replay: expand the two degree-eight products in RESULT.md lines 62–72 and bisect the monotone cubic (or compare it at 0 and 1 for exact existence and uniqueness). The frozen checker was read statically; no sampled result is used for a universal claim. The verification note’s description of a root bracket is loose: CHECK.py tests a floating residual, while the proof supplies the exact bracket and monotonicity.

## originality

PASS

Qualified finding for the open-family two-response rank reversal and the exact one-crossing witness. The impulse response is classical, and single-response lag and inversion are elementary consequences; priority for those ingredients is not established by this review.

## value

PASS

The robust ordering reversal bears on whether peak timing can give a fixed ordering of even two ideal linear responses. A single exact crossing gives a complete witness rather than an isolated computed example, and the inverse sensitivity states when timing loses resolving power. These are mathematical statements only, without field validation or practical exposure conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
