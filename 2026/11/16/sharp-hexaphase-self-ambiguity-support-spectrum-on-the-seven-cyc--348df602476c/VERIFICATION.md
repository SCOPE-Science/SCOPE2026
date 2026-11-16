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

## Mathematical checks
The supplied `verify_support.py` exhausts exactly \(6^6=46656\) normalized exponent words, uses exact \(\mathbb Z[\zeta_6]\) coordinates to recognize vanishing off-peak autocorrelations, verifies all seven nonempty-zero-mask counts, and checks four disjoint exceptional affine/conjugation orbits with total cardinality \(252\). Its exact assertions passed.

The supplied `verify_increments.py` independently enumerates cyclic exponent differences satisfying their closure congruence, reconstructs all words and recomputes the autocorrelations in another integer coordinate basis. Its complete support census agreed and its assertions passed. No tolerance, floating-point roots, Monte Carlo sampling or external data was used. The field-theoretic off-axis lemma and the reduction from autocorrelation masks to support counts are proved in `RESULT.md`; the scripts are used only for the explicitly finite census and orbit classification.

## Limits
These checks establish the finite statement for \(\mathbb Z_7\) with \(\mu_6\) coefficients. They do not establish noise robustness or a result for other group orders or phase alphabets. Historical-priority verification and independent mathematical audit remain open.
