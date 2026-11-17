---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The sketched normal equation for unit A=(e1+e2)/sqrt2 and orthogonal response gives xhat=(gamma1²-gamma2²)/(gamma1²+gamma2²+2rho gamma1 gamma2), with rho the average of m independent uniform Hadamard pair-sign products. Conditioning on rho=a and isotropic Gaussian angle gives Z_a=cos(2theta)/(1+a sin(2theta)). For |a|<1 it has the stated arcsine CDF and bounded support (1-a²)^(-1/2); for a=±1 it equals a ratio of independent equal-variance normals and is standard Cauchy. The collision mass P(|rho|=1)=2^(1-m), verified independently via exact binomial weights through m=16; all other components have support bounded by T_m=m/(2sqrt(m-1)). Thus the exact two-sided tail above T_m is mass*2arctan(1/t)/pi, and integrability threshold p<1 follows for each finite m. Uniqueness a.s. holds also at rho=±1 because its Gram denominator is a nonzero squared Gaussian except on a null set.

## originality

PASS

The motivating 2026 method already recognizes an unsafe Gaussian diagonal and a Cauchy Gaussian ratio, so this is NOT claimed as discovery of the failure mechanism. Best-of-knowledge surviving contribution is the exact all-m collision-weight mixture, compact remainder, sharp far-tail cutoff and moment dichotomy in the specified row-replacement model. A plausible highly relevant primary manuscript was not readable in full, so priority remains qualified.

## value

PASS

A mathematically motivated sharp risk diagnosis of a proposed randomized least-squares sketch: almost-surely defined estimates have infinite absolute and squared risk at every finite row budget, and the exact collision-weight and cutoff localize the rare catastrophic event. This is practically and mathematically substantive rather than an arbitrary small counterexample, while not contradicting success of the separate balanced-pooling sketch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
