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

# Exact finite verification

Run `python3 verify.py` from this directory using Python 3 with the standard library. The file `cover_dual_certificates.json.gz` carries all normalized-profile nonnegative rational duals, with sparse positive integer numerators and one positive integer common denominator per profile. The verifier derives its own majority matrices and strict covering relations; it checks each certificate's full vector inequality using exact integer arithmetic and checks both explicit mixed-popular counterexamples directly. No optimization solver or scientific file outside this package is needed to replay the result.

A successful run reports all seven universal-data sets: each of the three covering relations at two agents (two normalized profiles) and three agents (36 normalized profiles), and McKelvey covering at four agents (13,824 normalized profiles). It also reports the Bordes and Gillies examples and finishes with `ALL EXACT CHECKS PASS`.

The exhaustive coverage is only for the explicitly stated finite market sizes and covering variants. In particular, the package supplies no universal claim for five-agent McKelvey covering or four-agent Bordes/Gillies inclusion. The verification is a self-contained mathematical certificate check, not an independent scientific audit or publication-priority determination.
