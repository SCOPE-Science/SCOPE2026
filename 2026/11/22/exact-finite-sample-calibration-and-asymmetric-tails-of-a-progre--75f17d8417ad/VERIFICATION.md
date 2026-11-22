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

# Verification of the mathematical result

`check_exact.py` is a complete standalone standard-library Python 3 checker. Run `python check_exact.py` with no input files. It carries out 413 checks, including exact rational identities for uncensored and initially censored samples, the explicit \((5,3,1)\) CDF, both endpoint coefficients, and direct independent-lifetime simulations of two valid removal schemes.

The repeated prepackaging execution passed all checks. In addition, a separate high-precision calculation examined five parameter triples with two shrinking endpoint thresholds; it confirmed convergence of both normalized tail probabilities to one. These numerical experiments are finite; the all-sample proof uses the exponential-spacing decomposition, distinct-rate partial fractions and dominated convergence with finite exponential moments.

The source first appeared online September 18, 2020, established by the publisher's publication record. The same result has not received an independent mathematical audit or external validation.
