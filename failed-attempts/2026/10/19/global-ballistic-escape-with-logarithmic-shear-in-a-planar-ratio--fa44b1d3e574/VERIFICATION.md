---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Put v_n=|cx_n| and z_n=sgn(cx_0)y_n off the fixed line. Then z_{n+1}=z_n+v_n and v_{n+1}=v_n(1+a/(1+z_n^2)). Thus v_n grows strictly, z_n>=z_0+n v_0 and the log of the product of multipliers is summable. Hence v_n tends to V>v_0, and z_n/n tends to V. The exact tail V-v_n=sum_{k>=n} a v_k/(1+z_k^2) first gives O(1/n), whence z_n=Vn+O(log n). The summand is then a/(V k^2)+O(log k/k^3), giving V-v_n=a/(Vn)+O(log n/n^2). The increments of z_n-Vn+(a/V)log n are summable with the required O(log n/n) tail. Undoing the two signed changes gives both stated coefficients even for negative x_0 or c. The fixed line is pointwise fixed; no off-line orbit is bounded or periodic. The combination at N,2N,4N cancels the affine terms and leaves +a log(2)/(cX). The packaged finite checks were inspected, not run, and are not needed for any quantifier.

## originality

FAIL

The distinct Resultary record c216a2b82ab6 explicitly states the identical map, the same all-real off-line initial data and a>0, c!=0, and both signed asymptotics with the identical remainder orders. It adds a velocity-gap bound and an invariant-measure classification. All additional claims in the frozen item follow immediately from this stated theorem and the map: strict |X|>|x_0| from one strict step and monotonicity, bounded/periodic orbit exclusion from escape, and the dyadic identity by cancellation in the same y_n expansion. This is demonstrable claim coverage in the reviewed corpus, not a conclusion about historical priority or who discovered it first. The later catalogue date is reported separately and is not the basis for the decision.

## value

PASS

As a mathematical claim, resolving the entire positive-feedback fixed-line regime and obtaining finite transverse saturation together with a nonvanishing logarithmic lag is informative beyond local stability or escape alone. A later matching claim does not make the underlying scientific question unmotivated. The dyadic consequence alone is not a valuable distinct repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
