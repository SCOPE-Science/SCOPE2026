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

# Verification

Run `python3 check.py` (Python 3 standard library). The test script constructs coefficients in the original basis of \(\mathbb Z[\sqrt2]\) independently of the digit-state recurrence; verifies all 19,683 indices below \(3^9\) for 13 moduli; checks that the complete reachable digit orbit equals the proposed primitive parity-constrained set at every modulus \(2\le m\le48\); checks each residue marginal as an exact `Fraction`; and checks the finite parity-count formula for \(0\le L\le9\). The actual replay passed all stages.

The symbolic proof, rather than any finite enumeration, establishes transitivity for all prime powers, independent CRT factors, finite-state convergence, and the limiting valuation law. The claim does not give an effective uniform mixing rate over growing moduli. Independent validation has not been performed.
