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

The usual joint fixed-level sample-quantile CLT gives covariance p/(uv) for the two spans, since their nested Brownian bridge increments have lengths 1/2 and 1−2p; their variances are 1/(4u²) and 2p(1−2p)/v². The ratio delta method at (2a,2b) gives (1); substituting the Cauchy quantiles and densities gives tan(πp) and the stated positive V_C. This uses the joint CLT as in the proof, not merely four separate marginal limit laws. In the mixture, the logarithmic derivative of a positive quantile with respect to s is strictly larger at b than at a for s>1; thus a/b strictly decreases. At s=1 the Gaussian ratio is above the target. At infinity a is bounded since w<1/2 while b diverges since w>2p. This yields a unique scale on a continuous ratio-matching curve. The exact certificate was checked by inspection, not executed: Machin's identity and the alternating trig, integrated-Gaussian and exponential tails enclose the reference values and mixture CDF/PDF; the large-x bound follows from Mills and e>2. CDF bisection preserves the quantile brackets, and monotonicity of both quantiles in s and of φ on positive arguments justifies the interval density and variance bounds in certify.py lines 63–121. The variance enclosures have disjoint signs relative to V_C: (0.1915680,0.2001835), (0.0244888,0.0277288), and V_C in (0.1022,0.1024). An independent 60-digit numerical replay, not an exact enclosure, gives scales 17.9343215172 and 10.0401293687 and respective gaps +0.0939032616 and −0.0761551078; these corroborate the signs. Replay locators are RESULT.md lines 28–50, the frozen certify.py and CERTIFICATE.txt, and the independent_numeric.py and independent_numeric_output.txt files in the private record-1 branch. Continuity yields exact simultaneous matching; the displayed mixture parameters are only approximate. Continuity of the limiting normal at the test endpoints gives nominal limiting rejection, not finite-sample equality. The derivative of the mixture density is negative on x>0, its moment-generating function is finite everywhere, and a single centered normal cannot match the ratio.

## originality

PASS

Credit the prior Cauchy test and asymptotic calibration, standard quantile theory, and earlier examples of nonconsistency for other Cauchy tests. The supported distinct claim is a fixed two-centered-normal-scale mixture matching both the population index and the scalar first-order distribution at exactly p=0.02217468, yielding limiting rejection equal to size rather than merely low simulated power. The closest primary access gaps are recorded below; they limit historical priority assessment and are not evidence against or for prior coverage.

## value

PASS

The witness addresses a concrete limitation of a published Cauchy test. It is smooth, strictly unimodal and light-tailed with just two scales, yet the usual scalar test has asymptotic power equal to its level. Matching the variance as well as the center matters for that conclusion, and minimality within the specified Gaussian scale-mixture class makes the counterexample interpretable. No general failure of Cauchy testing or indistinguishability of full samples is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
