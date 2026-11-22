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

## Mathematical verification

The complete analytic proof is in `RESULT.md`, including exact assumptions \(N\ge2\) and \(\alpha>-1\), moment uniqueness, phase restrictions, polynomiality, and endpoint isometry arguments. The argument does not assume that an analytic multiplier is initially a polynomial or bounded.

Run `python3 check.py` with Python 3 and no nonstandard packages. It checks 7,106 supplementary *exact rational* endpoint norm identities, disjoint supports, and congruence-class repetitions at higher integer exponents. The finite test ranges are integers \(2\le N\le20\), \(0\le n\le120\), and integer trial exponents \(2\le d\le12\); no finite range is used to prove the infinite theorem.

## Limits

The 2018 general isometry paper's full journal text could not be inspected; the accessible author's lecture and the 2019 primary preprint were examined for the closest theorem statements. The historical equivalence/priority risk is documented in `REVIEW.md` and `AUDIT.json`. Independent mathematical review has not occurred.
