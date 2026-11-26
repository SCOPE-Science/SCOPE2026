---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With positive masses the quadratic factors are Hurwitz stable. On the positive imaginary axis the continuous argument of their product increases strictly from 0 to nπ (each zero contributes a positive phase derivative); thus the even and odd parts have simple, alternating negative roots, with the even part at both ends. The normalized parts give independent Bernoulli sums, up to the odd half-shift. The difference of Bernoulli parameter counting functions is 0 or 1, so integrating 1−2x gives an upper and lower bound equal to the respective signed half-interval areas ±1/4. The finite-support conditional moments are continuous as the masses are mixed with uniform triples, since both conditioning probabilities remain positive in the limit. The one-variable witness has conditional variances (1/4,0); adding a deterministic half shifts and swaps the parities, giving (0,1/4). An independent integer-coefficient convolution checked the 52,686 valid denominator-four cases through n=4 and both witnesses (python3 /workspace/reproductions/frozen_checks.py 1). The frozen 53,886 count includes additional sampled cases and is recorded evidence, not the universal proof.

## originality

FAIL

The October 26 Resultary antecedent expressly establishes exactly the interlacing of the Bernoulli parameters of these same conditional laws, not merely the advertised half-unit coupling. The proposed bound is a direct corollary of that already proved stronger marginal structure: write each Bernoulli variance as the integral of 1−2x up to its parameter, sum the alternating indicators, and bound by the positive and negative parts of the kernel. The sharpness examples amount to the single ternary law and a deterministic half-shift. Thus the quantitative statement is correct and not literally stated in the closest record, but its general bound is mechanically covered. This finding is not rejected because of unsuccessful searches or on the basis of a generic displacement coupling alone.

## value

PASS

A length-independent sharp comparison of two potentially large conditional dispersions is useful in interpreting this model. The sharp endpoints distinguish parity-specific uncertainty from transport closeness. This usefulness is not evidence that the consequence is original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
