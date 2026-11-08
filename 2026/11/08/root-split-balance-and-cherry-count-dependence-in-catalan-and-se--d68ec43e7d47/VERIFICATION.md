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

# Reproducibility and checks

Run `python verify.py` using Python 3 with only its standard library. The successful recorded output was `PASS: 1820 exact and numerical assertions`.

The program calculates, using exact fractions, each covariance for both root-split laws for all integer orders from 2 through 200 and compares it with the proposed closed expression. For the Catalan law it separately checks the two marked generating-function coefficient formulas, hence can detect a mistake in the symbolic extraction. An independently built recursive distribution of total cherries in each model is used for all tree orders through 12, including exhaustive Catalan counting and exact rational BST probabilities; conditional-profile inequalities are checked for sizes 5 through 100. Large-size numerical diagnostics verify rates but are not substituted for proof.

The proof in `RESULT.md` is the basis for all-order validity: the Catalan root-marking functional identities reduce to elementary binomial coefficients; BST uses uniform root sizes and a four-indicator conditional expectation correction. No external certificate or independent audit is represented.
