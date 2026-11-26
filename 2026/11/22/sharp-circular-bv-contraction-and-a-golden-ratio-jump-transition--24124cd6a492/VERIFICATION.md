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

Checked RESULT.md §§1–4 and inspected VERIFICATION.md and two_harmonic_bv_check.py without executing the supplied script. A zero-mass real derivative measure has two probability parts after division by half its variation; coupling gives the translate-distance upper bound, with equality attained by the two point masses forming the derivative of an arc indicator. Under the stated Lebesgue convolution the harmonic coefficients multiply, yielding A=a^r and B=b^r. Factoring the translate difference and integrating over z=cos u gives the branches 2 and qc+1/(qc) for the scalar integral, c=cos(φ/2). On the second branch the sign of the derivative is the sign of q²c²(1−2c²)−1. At its only possible interior maximum, s=c² is the larger root, and the squared ratio to the semicircle value is (1−s)³/(1−2s), increasing to cross one exactly at s=(3−√5)/2. The endpoints of the second branch do not tie the semicircle. This proves the sharp value, exact tie and lengths. The pure second harmonic reaches its maximum at φ=π/2 up to complementation; zero density harmonics give the trivial zero extension. Positivity almost everywhere for each probability kernel and compactness in the shift give uniform strict contraction. This is a real BV result and the length list concerns single-arc witnesses, not a classification of every maximizing function.

## originality

PASS

Best of current evidence, the covered ingredients are the translate-distance reduction and, in particular, the equal-harmonic subcase by scaling a signed projector. The supported distinct claim is the unrestricted admissible two-weight optimization, including the golden-ratio tie, the maximizing length transition and its dependence on powers.

## value

PASS

This is the first freely weighted two-harmonic setting in which distinct optimal jump separations compete. The exact coefficient distinguishes what iterated smoothing can lose in BV, while the coexistence and discontinuous change of a maximizing arc answer a geometric question not captured by Fourier multiplier bounds or by the variational characterization alone. The threshold lies in the positive-kernel domain, and the stated small positive parameter pair exhibits an actual change on iteration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
