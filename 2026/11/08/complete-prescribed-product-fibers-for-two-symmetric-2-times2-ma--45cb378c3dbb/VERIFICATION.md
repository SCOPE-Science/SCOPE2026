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
Run `python3 verify_symmetric_product.py` and compare stdout with `verification_output.txt`. This enumerates every ordered symmetric factor pair and every target in fields of orders \(2,3,4,5,7,8,9\). The implementation uses explicit irreducible polynomials for extension fields and performs literal multiplication for each pair, independently of the proof's cyclic-centralizer classification.

Run `python3 verify_mass_identities.py` and compare stdout with `mass_output.txt`. Both target-count and mass-weighted target-count differences are rational polynomials of degree at most six, so seven distinct rational-root checks give exact polynomial identities. Neither program alone proves the universal fiber formulas; the proof in RESULT.md does.

All paths refer to files embedded in the same mathematical package. No independent mathematical audit has been conducted.
