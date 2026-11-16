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

The standalone `verify.py` is executable with Python 3 and the standard library. It independently constructs the complete matching-incidence Walsh transform for dimensions \(2\) through \(5\); checks the direct matching-sign sum against the row-sum identity; and uses exact eight-column multinomial aggregation for dimensions \(2\) through \(12\). It tests all coefficients' mod-four residues, the predicted existence of zero coefficients, exact Parseval second moments and rational endpoint norms. The checker also tests the zero constructions through dimension \(64\) and compares a numerical Gaussian chaos sample with the analytically derived constant. Finite checks do not prove infinite congruence or limit assertions.

Recorded exact output includes `n 4 freqs 4096 coeff_types 10 zeros 1160 norm 567/128`, `n 5 freqs 32768 coeff_types 16 zeros 7560 norm 5805/1024`, and `n 6 freqs 262144 coeff_types 23 zeros 0 norm 231435/32768`. Final marker: `K3N_TWO_MATCHING_WALSH_ALL_CHECKS_PASS`.

Fourier normalization, matching cardinality, exact boundary classes and uniform integrability are proved in `RESULT.md`. The source manuscript's two central arithmetic steps (mod-four edge-flip invariance and four-column zero construction) need no computational completeness assumption. The Gaussian constant comes from an exact exponential/chi-square integral, not from Monte Carlo.
