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

# Verification details

The symbolic proof in `RESULT.md` determines all elements of each centralizer: increasing elements are unions of complete residue chains, and decreasing elements are exactly the rank-at-least-two reflections for which both products with the shift power are empty. The endpoint counts are disjoint and exhaustive.

`VERIFY.py` uses direct finite partial-function composition. For chain sizes \(2\le n\le9\) and all \(1\le k<n\), it checks the full rank polynomials for both orientation types, as well as the total increasing count and stable-range reversing count. For \(n\le6\), a second exhaustive enumeration of partial injections checks the transformation normal forms, without assuming the polynomial formulas. The observed standard output is `CENTRALIZER_RANK_CENSUS_OK 36`.

Run with `python3 VERIFY.py`. No third-party Python modules or external data are required. These checks do not prove the infinite statement; the symbolic proof supplies its generality. No independent mathematical audit has been performed.
