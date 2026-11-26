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

For exactly two equal hard intervals and a perfect reference, the true alarm probability is reference mass plus q times secondary-only mass. If partially overlapping, push the secondary outward on its extending side until it touches: its old uncovered segment is a strict subset of the new one up to endpoints. For identical footprints, adjoining the reference adds strictly positive secondary mass. For a gap, contract both centers toward zero by a common positive factor until their distance is 2r; the entire move stays disjoint up to endpoint measure zero. Evenness and strict log-concavity imply that a fixed-width interval loses mass strictly with increasing absolute center, so this strictly improves at least one positive-weight term. These direct improvements justify optimizing over touching layouts on the unbounded line without assuming an optimizer exists in advance. In the reference-left layout, division by positive f(c) makes the sign equation a strictly decreasing function of c: log f has strictly decreasing derivative, so the left shift ratio increases and the right shift ratio decreases. The raw derivative has signs + at zero and - at r. The unique root therefore gives the global optimum in that orientation, with exactly one reflected optimum. At each interior candidate the divided derivative decreases strictly with q, giving strict root motion; continuity on the compact [0,r] and the unique endpoint roots give the limits r and 0. Independently transformed the Gaussian equation with z=exp(2rc/sigma^2), recovered the positive quadratic root, and directly evaluated the example (c,H(c),H(0))=(0.6708104538187869,0.7806302476373099,0.7158748020777312). Inspected checker.py and the recorded 26,979 assertions; their finite Gaussian/logistic checks are supplementary and were not rerun. RESULT.md's isolated phrase 'strong log-concavity' in Limitations is imprecise terminology; the theorem and proof consistently use strict log-concavity, not a uniform curvature bound.

## originality

PASS

The established two-sensor coverage objective and earlier sufficient non-overlap principle are not claimed as new. The supported distinct result is the complete globally adjoining design, uniqueness up to reflection, translation and strict quality law for the stated perfect/fallible model on the real line, with the exact normal formula. None of the closest inspected statements implies this classification.

## value

PASS

The perfect reference makes a clean benchmark for when to spread rather than cluster a supplemental detector. The claim rules out both overlap and inefficient gaps and then determines the unique placement, not just a stationary offset. Its reliability law is uniform over even strictly log-concave location priors and resolves a real design tradeoff in the idealized model. This does not validate camera performance or imply that overlap is suboptimal for two fallible detectors; as q tends to zero the placement benefit itself can be small.

The dated certificate retains the supplied scientific assessment, sources and limitations.
