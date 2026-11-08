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

# Reproducible checks

The standalone program `verify_walsh_five.py` enumerates all \(\binom85=56\) and \(\binom{16}5=4368\) column configurations for the two local affine row types. For each local matrix, a fraction-free integer-elimination determinant is compared with the full permutation expansion. The local table must equal \((24,32)\) for determinant magnitudes \((0,32)\) in affine dimension three and \((1360,2672,320,16)\) for magnitudes \((0,16,32,48)\) in dimension four. It additionally checks the anchored four-by-four binary-incidence determinant counts \(15,20\) and \(425,835,100,5\). The checker verifies that all 16 local maximum-volume sets are the 16 distinct translations of the stated prototype and checks the closed all-dimensional formulas for dimensions four through nine.

The checker also verifies the independently known Cauchy--Binet second-moment identity at each tested dimension. These tests use no floating-point arithmetic, third-party packages, or inaccessible data. The universal claim follows from the mathematical affine-orbit and quotient-projection argument in `RESULT.md` applied to the completely enumerated finite local tables.

Run: `python3 verify_walsh_five.py`. Expected final output: `WALSH_FIVE_DETERMINANT_HISTOGRAM_PASS`.

The program does not independently establish historical novelty or provide an independent external audit; it is a reproducibility certificate for the exact finite ingredients.
