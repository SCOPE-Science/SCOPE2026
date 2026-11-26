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

With the normalized measure, the four nontrivial real-conjugate character coefficients have exactly seven unordered quartic resonances. The two mixed non-pairing contributions are 8 Re(u^3 v) and 8 Re(v^3 conjugate(u)); M inserts the two distinct real multipliers a>0>b. With r>0 the norm quotient is strictly decreasing in each resonance cosine (negative numerator slope, positive denominator slope, and numerator and denominator both positive). The phase map has determinant 10, so both cosines can be -1 and this is necessary at any two-mode optimizer. The resulting N/D derivative has the stated sextic numerator; the interval substitution 4t/(1+t) yields six positive coefficients then one negative, and P(4+t) has only negative coefficients. The resulting unique root is a strict global maximum, including the limiting one-mode endpoints; r=4 already beats b^4>a^4. The angles solving the two congruences are indexed modulo ten, reached by translations (increment two) and sign (increment five). Delta is onto the real mean-zero space by its four nonzero Fourier multipliers and M Delta is the stated difference. Independent `python3 /workspace/branches/frozen_review_checks.py` (section 4, passes) enumerates the resonance counts, certifies the algebra and signs exactly, and evaluates the norm as 0.863476459984369237616776... and r as 3.62064679016703604.... The source's displayed norm decimal is illustrative and differs in its last quoted digit, not in its exact specification. The bundled checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for this real five-state neighboring-average optimum and its equality profile, not for the Fourier resonance method or convolution inequality generally. The two closest indexed sharp norms differ by modulus or by multiplier. The actual statements available in the frozen comparisons supply neither this root nor the scale ratio of its equality profile.

## value

PASS

This is a natural first odd cyclic modulus with distinct nonconstant spectral magnitudes, in an established neighboring-average inequality. The exact L4 value, not merely contractivity, exhibits a strict nonlinear versus spectral gap and distinguishes a rigid mixed-frequency worst profile from individual eigenfunctions. The precise finite-state coefficient and extremizer remain independently useful without a claim about the general product constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
