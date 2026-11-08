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

# Reproduction

Run `python3 verify.py` in this directory. This requires only standard-library Python 3. It enumerates finite coordinate flip sequences exactly for 28 parameter pairs and compares all five rational moment identities (140 equality checks); it also checks 84 positive covariance/variance assertions and 13 numerical checks of the proposed two scaling regimes. The Python enumerations are finite spot checks; the theorem for every \(n\ge3\), \(t\ge2\) follows from the combinatorial indicator proof, strict Jensen convexity, and analytic asymptotic expansions in `RESULT.md`.

# Limitations

No independent audit or external certification has been performed. Finite numerical examples cannot certify the infinite-domain assertion. The proof addresses uniform non-lazy flips, not distinct *vertices* visited or nonuniform coordinate selections.
