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

For the standardized Gaussian triple in RESULT.md lines 20–55, put A=a²b². Gaussian regression and Wick's rule give the conditional fourth moment in the probabilists' Hermite basis as 1+2c²+(a²+b²+4abc)He₂(X₁)+A He₄(X₁). Under the normalized |X₁|⁻ˢ tilt the last two polynomials have means −s and s²+2s, respectively, by the absolute-normal gamma recurrence; 0<s<1 makes the tilt integrable. This gives the claimed polynomial, including all equality points. Marginal scales cancel in the separate-moment normalization. In equicorrelation, the admissible interval is (−1/2,1). For negative ρ the bracket is positive term by term; for positive ρ it decreases strictly on [0,1] from 2 to 3ρ²−4ρ<0, and the smaller quadratic root gives the stated threshold. At ρ=0 the difference vanishes. The supplied verify.py is a finite rational algebra check; it was inspected, not executed or counted as independent evidence.

## originality

FAIL

A dated 2026-10-12 indexed result already gives the exact same normalized moment minus its joint quadratic comparator and explicitly gives that comparator as 1+2c². The principal claimed identity and hence the full sign/equality test are recovered by adding 2c²; the equicorrelation threshold is a quadratic specialization of that known exact identity. This is verified mathematical coverage, not a failure to access external literature.

## value

FAIL

The fully factorized Gaussian comparison is motivated, and fixed positive equicorrelation examples with opposite signs are useful illustrations. But the proposed exact invariant just changes the baseline of a known exact formula, and the remaining threshold is obtained by one specialization and solving the resulting quadratic. As submitted this is a useful corollary rather than an independently valuable new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
