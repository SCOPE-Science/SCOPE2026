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

The theorem's finite check is reproducible with `python3 checker.py` (Python standard library only). It exhaustively tests 961 pairs of ordered-partition block-size compositions through five points against two-round Ehrenfeucht–Fraïssé outcomes, then exactly checks labelled weighted enumeration and endpoint singleton identities for all 16,383 compositions through fourteen points. The polynomial count of twelve limiting probabilities is checked symbolically over integer coefficients. A positive finite-size obstruction probability is computed directly for sizes eight, twelve and sixteen and compared with the proved asymptotic.

The exact coefficient estimates, uniqueness of the least-modulus pole, the exponentially rare exceptional profiles, and the two-round profile lemma are proved in `RESULT.md`; no finite computation substitutes for these infinite claims. Historical novelty beyond the examined primary literature remains unverified. No independent audit has been performed.
