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

This is an exact one-partition binary-label calculation. With exactly m of each label, and J designated-label units among a draws without replacement, the two retaining conditions are 2J≤a and 2J≥a for the smaller and larger daughters, respectively. Only a strict majority of the designated label removes a daughter, and a tie retains both. For a=1 there are two equally likely states; for a=2 the weights for J=0,1,2 are (m−1)/(2(2m−1)), m/(2m−1), (m−1)/(2(2m−1)); for a=3 the two endpoint weights are each (m−2)/(4(2m−1)) and the middle weights are each 3m/(4(2m−1)). Weighting the retained counts and within-daughter mixed-label products gives the displayed expectation formulas. For odd a, symmetry between J and a−J gives E N_a=m; for a=2 the tie adds m times its probability, yielding m(3m−1)/(2m−1). Independent subtraction confirms the infected-count differences Ī_2−Ī_1=(m²+1)/[2(2m−1)] and Ī_1−Ī_3=(m−2)/[2(2m−1)]; the mixed-pair numerators over the same denominator are m((m−2)²+1) and 4m(m−2). For q_a=E I_a/E N_a, the successive differences are (m+1)/[2m(3m−1)] and (m−2)/[2m(2m−1)]. All are strictly positive for m≥3 and the m=3 numbers follow by substitution; 3+3 can be labeled either way without changing totals, and fewer than six units cannot support all three sizes. The supplied checker was read, not executed. Nothing here identifies q_a with an expectation of the realized ratio, or mixed pairs with transmission.

## originality

PASS

The primary motivating study supplies the same types of mechanisms and an explicit six-unit comparison of 1+5 with 3+3, which is credited as partial overlap. Its full-text passages inspected give neither the conditional half-and-half, immediate three-size comparison including 2+4 nor a general solved expression implying the simultaneous strict rankings. The distinct parasite partitioning theorem treats a different state space and observable; the only exact catalogue return was the frozen item itself. Priority is qualified by the scope of these comparisons.

## value

PASS

This isolates a precise source of nonmonotonicity in a motivated one-event model: at exact balance the smallest even daughter can share a tie with its complement, whereas both adjacent odd sizes cannot. The strict ordering simultaneously for two counts and the survivor-normalized ratio is stronger than observing that more units survive an even split, and supplies an exact minimal benchmark for one-step calculations. The value is in this structural comparison within its assumptions, not in a biological intervention or a prediction about spread, fitness or long-run dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
