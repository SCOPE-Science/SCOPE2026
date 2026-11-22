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

The exact all-parameter formulas are proved in `RESULT.md`, especially the three-case extension partition, downset count, and simultaneous-permutation orbit normal form. The standalone `verify.py` runs with Python 3 standard library only and requires no reference file or network access.

It directly tests each of the \(3^{2n}\) possible ternary statuses of the one new point with respect to the \(2n\) named old points. Each status is checked by brute-force transitivity on the enlarged relation, independently of the theorem's downset decomposition. For \(2\le n\le6\), all \(597861\) assignments and \(1367\) valid extension types are covered; for \(2\le n\le5\), all simultaneous index permutations are used to compute \(88\) orbit types. The measured output is reproduced without modification in `verification_output.txt` and has final line `ALL_CHECKS_OK assignments=597861 valid_profiles=1367 checked_orbits=88`.

These checks do not prove the all-size statement, and they do not constitute independent mathematical peer review. Historical priority remains provisional. One known published general height-two counting identity already entails the unrefined named-type count; the new claim is the full bivariate and orbit classification.
