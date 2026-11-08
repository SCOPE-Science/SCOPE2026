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

# Verification record

Run `python3 verify.py` with a standard Python 3 interpreter. The script tests all four branch choices for each integer \(m\) from 2 through 2000, comparing \(\gcd(A,B,C)\), the candidate closed formula and the gcd of the first three polynomial values. Separately, for each base from 2 through 18 it constructs independent coin-change dynamic programs for the full partition sequence and the truncated four-generator sequence, checks the first three values of all four branches, and compares with the cubic formula. The recorded console output is in `verification_output.txt`.

The standalone script is a finite arithmetic cross-check, not an infinite proof. The all-parameter theorem rests on the exact generating-series identity, an integer-unimodular coefficient change and case-complete prime-adic valuations in `RESULT.md`. The generating-series operator identity is also available in Rødseth--Sellers (2001), Lemma 6. Mathematical novelty is limited to what the literature comparison in `REVIEW.md` supports. Independent audit is not performed.
