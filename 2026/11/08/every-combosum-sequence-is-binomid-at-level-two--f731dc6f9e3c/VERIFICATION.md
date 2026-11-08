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

# Reproducibility

Run `python3 verify_level2.py` using the Python standard library. It checks every finite binary mask through index 16 that is closed under addition within that bound, and verifies the two-term level-two inequality for each admissible pair of indices. It also checks 180 reproducibly sampled finitely generated semigroups up to 180, then directly constructs 61,425 generalized binomial coefficients from signed two-prime examples. `verification_output.txt` contains the exact output of the supplied script.

The tested finite closures are restrictions of possible infinite additive submonoids. The test does **not** prove any all-index assertion by exhaustion. The rigorous argument is the sumset inequality, its exact equality characterization, and the prime-valuation threshold decomposition in `RESULT.md`. No higher-level theorem is asserted. No independent audit has been performed.
