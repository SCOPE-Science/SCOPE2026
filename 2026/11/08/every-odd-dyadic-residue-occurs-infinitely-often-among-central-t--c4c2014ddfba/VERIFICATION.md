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

The embedded standalone `verify_trinomial.py` is run with Python 3 and uses only the standard library. It checks recurrence integrality and the binomial coefficient definition through index \(100\), oddness of all computed terms through index \(2048\), and exact separated-block congruences over the indicated finite ranges. It checks every odd residue modulo \(2^k\) for \(1\le k\le8\) by direct enumeration through index \(2048\), then independently verifies the cyclic subgroup/coset assertion for \(3\le k\le10\). The verifier completed with `VERIFY_OK` during preparation.

These tests establish only the checked finite cases. The claim for all integers \(k\) and all odd residue classes follows from the symbolic proof in `RESULT.md`, notably the Frobenius precision lemma and the order computation. No independent mathematical audit or external certification is claimed.
