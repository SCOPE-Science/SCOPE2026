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

# Verification performed

The standalone `checker.py` was executed with standard Python plus SymPy. It enumerates every parent sequence for recursive trees with two through eight vertices and uses exact rational polynomial coefficients, not Monte Carlo. It also checks the equivalent Bernoulli-depth probability generating function and Gaussian exponential-tilt moment identities. The recorded checker result is **105 exact identities passed**.

The analytic steps checked separately are the recursive profile expectation, Gaussian exponential tilt, Bernoulli-sum representation, exponential concentration of good spines, a marked first-moment union bound, and transfer from the published maximal-field law. The new asymptotic conclusions are proved by these steps; they are not deduced from finite enumeration. Literature priority was checked against the motivating complete manuscript, related full-text genealogy literature, and indexed results; broad historical completeness is not certified. The publication-privacy scan found no operational material in the public research package.

Independent verification and external certification were not performed.
