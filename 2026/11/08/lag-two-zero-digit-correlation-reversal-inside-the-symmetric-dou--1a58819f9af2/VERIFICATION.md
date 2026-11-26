---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The frozen table's upper-left entry is undefined as printed (u); it must equal ν by reflection of the (+1,+1) event. The complete repaired RESULT.md makes just that correction. Write a=α−1, c=2a, d=2−α. The step density H/(3α) integrates to one since 2+2a+c+d=3α. For y>0 the central branch contributes H(y/2)=2+1_(y<c) to 2PH. For y<a both outer inverses contribute a combined 3: the indicator thresholds at ±(4−3α) occur in complementary pairs, since |4−3α|≤a. For a<y<d only the right inverse survives and has H=1, and for y>d neither survives. These are exactly the values of 2H, up to null breakpoints, also when knots coincide at endpoints. The cited unique ergodic ACIM therefore identifies the density. Its central mass is 2/3 and the lag-one zero event is |x|≤1/4, of mass 1/(2α). For lag two the central-central path gives |x|≤1/8; the two reflected paths through an outer branch give 1/4<|x|≤b=(α+1/2)/4. Splitting the wing integrals at a, with 1/4≤a≤b≤1/2, yields 1−3/(4α) after adding the core. Subtracting 4/9 gives the negative lag-one covariance and the unique lag-two zero at 27/20. Same-sign adjacency has mass ν=(3−2α)/(12α) on either sign, by integrating above (α+1/2)/2 and reflecting. Opposite adjacent signs are impossible, and stationarity plus sign symmetry with ± marginals 1/6 forces the corrected table. After two positive symbols the state cannot exceed 2−α≤(α+1/2)/2, ruling out another positive symbol; reflection and the opposite-sign exclusion complete the triple bound. Ergodicity converts these stationary cylinder masses to typical-orbit frequencies. The frozen exact-rational checker was inspected but not executed; the piecewise argument supplies the continuum and endpoint cases.

## originality

PASS

Credit the entire one-symbol plateau and the invariant-density/matching framework to Dajani–Kalle. The density can be evaluated by specializing their general formula, and the adjacency run restriction is elementary branch geometry, not a separate foundational result. The supported distinct finding is the evaluated short-lag law across the plateau subinterval, in particular the sharp interior reversal despite an unchanged one-digit frequency. Neither the closest random-map record nor the inspected deterministic matching results already evaluate that lag-two law or provide an equivalent parameter classification.

## value

PASS

The unchanged one-symbol zero frequency is a motivated signed-digit statistic, but it obscures changes in stationary clustering and separation. The exact interior parameter where a lag-two dependence changes sign while lag one stays negative is a usable diagnostic, not an arbitrary finite sample or another evaluation of the plateau. The corrected adjacent law additionally quantifies which symbolic combinations contribute. This is not a longer-lag mixing theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
