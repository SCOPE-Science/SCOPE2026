---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Exact arithmetic replay: run `python3 check.py` with Python 3 and no third-party dependencies. The checker constructs each uniform weak composition for \(2\le m,n\le7\) rather than evaluating the moment formulas to generate its expectations. Observed output: `PASS: 9560 exact-rational assertions`. It tests samplewise equivalence, moment identities, vacancy probabilities, correlations, and the rational decreasing balanced sequence to \(s=29\).

The proof for unrestricted admissible \(m,n\) uses the uniform-composition representation, factorial moments, elementary conditioning, and polynomial sign checks. Enumeration is independent corroboration of finite instances and cannot certify all integers. The null covariance formula does not extend without change to nonidentical population distributions or to the superbalanced range \(n>m\). No independent mathematical audit has been performed.
