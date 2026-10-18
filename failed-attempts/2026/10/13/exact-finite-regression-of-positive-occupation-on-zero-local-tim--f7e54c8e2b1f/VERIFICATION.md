---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

PASS: Conditioned on the entire reflected path, independently flip the sign of each complete or unfinished excursion. Every nonzero time has P(S_j>0|reflection)=1/2, giving E[A|reflection]=(2n-Z)/2 exactly; Z is measurable by the reflection. The return-probability generating function (1-z)^-1/2 yields convolution sum_i a_i a_{j-i}=1 and local-time factorial moment 2n-4mu, leading to variance 2n-3mu-mu^2, covariance -Var/2 and leading asymptotic -(1-2/pi)n. Independent enumeration of every 2^(2n) step sequence and every reflected-path fiber for n=1,...,6 confirmed the conditional identity and moments exactly.

## originality

FAIL

FAIL: The decisive conditional law is a direct specialization of Csáki, Csörgő, Földes and Révész (2016) Section 1, equation (1.1): it explicitly constructs the two-leg p1=p2=1/2 simple random walk by attaching independent fair signs to the excursions of its absolute-value path. Conditional expectation of the positive-leg count immediately gives the exact displayed regression for every finite time. The variance and covariance then follow mechanically from the classical zero-return convolution. Thus the submitted finding is an elementary corollary of a stronger previously published finite-time path construction, despite the paper not printing the same regression/covariance notation. The original self-review underestimated this implication.

## value

FAIL

FAIL: While zero visits and occupation are natural statistics, the asserted conditional regression is a one-line expectation of the published excursion-sign construction; the covariance is a routine variance substitution and standard central-binomial return convolution. No further motivated new structure, sharp boundary, classification or nontrivial technique remains after crediting the stronger prior result. The exact arithmetic is correct but does not independently pass the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
