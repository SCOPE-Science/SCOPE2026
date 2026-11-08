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

Run `python3 verify.py` from the same directory. The script requires only standard Python and enumerates all directed paths on monotone two-row ladders with \(2\le m\le8\). For five primitive root orders \(N=2,3,4,5,6\), and every corresponding \(1\le q<N\), it independently computes the forbidden-face matrices in all allowable degrees, the true boundary matrices, their composition, and the claimed Mayer dimensions. Exact modular arithmetic uses primes 7, 7, 5, 11 and 7, respectively, with roots 6, 2, 2, 3, 3.

Expected reproducible output:

`ALL_VERIFY_OK cases=35 ladder_columns=2..8 orders=2,3,4,5,6 allowed_path_instances=2835`

The checks do not infer infinite parameter ranges from finite test sets: the separate proof in RESULT.md establishes invariant-chain and boundary-rank formulas for every integer length and root order. No general symbolic factorization or external independent certification is claimed.
