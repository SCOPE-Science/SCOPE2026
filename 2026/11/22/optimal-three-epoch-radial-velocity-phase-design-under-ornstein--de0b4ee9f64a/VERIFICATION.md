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

For three scalar observations and three mean parameters the joint information determinant is (det X)^2/det Sigma. Common translation rotates the sine and cosine columns and leaves Sigma unchanged. Direct row subtraction gives det X=4 sin(a/2) sin(b/2) sin((a+b)/2); OU innovations give det Sigma=sigma^6(1-exp(-2ca))(1-exp(-2cb)). At a+b=2pi the end phases coincide and the determinant is zero, even though OU covariance is nonsingular at distinct times; as a gap goes to zero its sine squared divided by its covariance factor is O(gap). For smaller positive spans, the two gap terms in the log square root each have second derivative -1/(4 sin^2(x/2))+c^2/(2 sinh^2(cx))<=-1/(2x^2), giving unique equality of gaps at fixed span. The derivative of the equal-gap log objective is the stated root function; its derivative is strictly negative by sin(theta)<=theta and sinh(c theta)>=c theta. It is positive near zero and negative at 2pi/3. The overhead-like term 2c/(exp(2c theta)-1) decreases strictly with c, which moves the root strictly upward. Its limits are 1/theta and 0 uniformly on the compact interval from the limiting lower root to 2pi/3, yielding the two claimed limiting gaps. Evaluating the limiting determinant ratio requires squaring the ratio of the limiting equal-gap square-root objectives; this gives 0.8726723961736. The singular covariance at infinite tau is not treated as an admissible design problem.

## originality

PASS

The supported distinct claim is the globally optimized finite saturated determinant in this exact nonperiodic exponential covariance model, including its strict gap law and short- and long-correlation benchmarks. Equal spacing in other D-design models, approximate design results, and the general Fisher information formula are not attributed novelty.

## value

PASS

Three epochs are the minimal data size for the three coefficients, so the unrestricted optimum is a natural benchmark. The exact dependence on the correlation time shows that optimal spacing need not be one third of a period under known correlated noise; the strict equality result and the finite limiting determinant loss quantify this substantive distinction. This is a model benchmark, not a scheduling recommendation for realistic noise or different precision objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
