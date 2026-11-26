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

An equilateral centrally symmetric polygon is the sum of one equal-length segment per unoriented side direction. Width adds under this sum. Between adjacent side normals the directional width is a positive sinusoid (second derivative equals minus the width), so the minimum is attained at a side normal and its exact candidates are ℓ times the sums of sines of the forward angle differences. For each k the k-step differences sum to kπ; strict Jensen in the mean of the candidate widths yields the bound by the regular sine sum, with equality only when the k=1 gaps are all equal. At regularity all candidates are active, so for any given first-order angle perturbation the one-sided derivative is the minimum of the candidate derivatives. The circulant output has zero sum; writing each cosine as two exponentials gives terms with base r satisfying r^m=−1 and sum from k=1 to m−1 equal to (1+r)/(1−r). The cotangent numerator is proportional to sin(2πq/m), with nonzero denominator, so only rotation and (for even m) alternation are neutral. For the alternating path the positive gaps are π/m±2t; even offsets are unchanged and the odd-offset cosine terms cancel in pairs. The odd-offset sine sum is csc(π/m), giving the exact decrement and hence the stated pathwise quadratic coefficient, including m=2. An independent check builds actual polygon vertices by cumulative edges and evaluates support spans, testing 90 first variations and 18 alternating cases, including near the admissible endpoint. Replay: python3 /workspace/reproductions/frozen_math_checks.py 5; output /workspace/reproductions/record-5.txt. This is not a universal second-order result along arbitrary curves sharing the neutral tangent.

## originality

PASS

The supported distinction is the nonsmooth minimum-width first variation for fixed equal segment lengths, its exact parity-dependent kernel, and the explicit nonlinear loss of the alternating family. The global sine/Jensen argument is elementary and not credited in isolation. The strongest inspected maximum-width theorem has a strictly looser general constant for this class and does not address variations. The closest indexed Fourier width result keeps the normal grid fixed, and the closest indexed alternating family keeps vertex rays fixed and studies area. Neither supplies this angle-variable equal-side tangent classification. This judgment is bounded by the inspected material.

## value

PASS

Minimum width is a natural shape invariant, and its local nonsmooth stability does not follow from uniqueness of its global maximum. A full tangent classification identifies exactly when every nonrotational first-order move decreases width and when the alternating move evades linear loss. The computed exact nonlinear loss along that family distinguishes neutral tangent from actual equality and quantifies stability for all even half-side counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
