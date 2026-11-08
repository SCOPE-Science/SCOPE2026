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

# Verification of persistence explanation profiles

The verification artifact `checker.py` enumerates the entire binary completion universe for lengths one through eight. For each word, it checks every candidate position subset against the formal AXp and CXp semantics and then filters to inclusion-minimal subsets. This direct enumeration does not assume either proposed normal form. It compares the resulting families with the inversion-pair, cut-set and satisfying-word formulas.

The same checker directly counts words by adjacent \(10\)-descents and verifies the coefficient \(\binom{n+1}{2d+1}\), and verifies the total \(2^n-n-1\) number of violating words. Its last output is `ALL_CHECKS_OK`.

These checks are exhaustive only within the stated small range. The general claim is supported by the explicit proof using cut completion, inclusion-minimality and transition-position counting, not by extrapolation. Novelty searches and the cited public primary source do not amount to independent validation or certification of historical priority.
