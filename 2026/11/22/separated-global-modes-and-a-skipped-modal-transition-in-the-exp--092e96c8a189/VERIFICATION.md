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

The log-containing W is the stated published base CDF; its real extension has W(−1)=0, W'>0 for x>−1 and tends to 1. Thus telescoping gives the positive normalized PMF. Writing R_j=p_j/p_0 as the difference A^b−B^b with A>B≥1, its derivative is positive because x^b log(x) strictly increases on [1,∞). In particular R_2 is continuous, increases from zero to infinity for positive b, and crosses 1 only once. Independently certified the finite signs without executing the uploaded script: used the positive series L=Σ_{r≥1}(4/25)^r/r with 21 terms and remainder bounded by (4/25)^22/[22(1−4/25)]. Since W_j(L) decreases with L for j≥0, lower and upper CDF endpoints are rational. Scaled by 10^10, binary-searched the floor of each endpoint power using exact integer cross-products, then subtracted bounds. In units of 10^−10, p_2−p_0 at 779/1000 is in [−1409815,−1409812], and at 39/50 the intervals for j=1,2,3,4,5 respectively are [−12472908,−12472905], [390760,390763], [−12462093,−12462090], [−42490841,−42490838], [−82844661,−82844658]. This establishes the bracket and all four rival gaps throughout the bracket by ratio monotonicity. For the infinite tail, W'' has the sign of 1−(x+2)L; L>1/6 makes it negative on [4,∞). Composing with the increasing strictly concave bth power for 0<b<1 gives strictly decreasing increments starting at p_5, uniformly for b in the bracket. Therefore the crossing is genuinely global and locally skips count 1. Independent high-precision numerical bisection gave b≈0.7797825617279780577, consistent with the reported approximation, not used as a proof.

## originality

PASS

Best-of-knowledge pass for the exact adjacent-count-skipping transition in the original log-containing CDF-power Lindley family. The defining PMF is prior. The strongest distinct catalogue result gives the same pair of modal counts but for a different distribution, on a different parameter slice, and does not imply the claim. The original preprint and the later same-name model were compared at the level of exact PMFs and modal statements, not their titles.

## value

PASS

A strict separated global tie and a stable local 0→2 jump are stronger than a plotted shoulder or two local maxima. They give a concrete counterexample to unimodality or adjacent modal evolution for the original published count model, with a reproducible certificate that treats every point of infinite support. The chosen rational q is an exact witness to a natural model-shape question, not an arbitrary numerical slice claimed to describe all parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
