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

# Reproducible verification

Run `python3 verify.py` with Python 3 and the standard library. The program checks each odd prime below 149, enumerating every unordered three-parameter set, and asserts the full cardinality table and the complete 12-triple classification at 73. It verifies equality between each discriminant-derived nonimage mask and an independently computed direct hyperbolic image; this is an exhaustive cross-model check at all tested primes.

The infinite exclusion is mathematical: \(U\ge (p-23-10\sqrt p)/8>0\) for primes \(p\ge149\), from the Weil bounds for three genus-one curves and one genus-two curve and an exact boundary correction. The program does not simulate or certify infinitely many primes. The published two-target formulas and general multi-target bound are credited as prior work. Independent mathematical audit has not been performed.
