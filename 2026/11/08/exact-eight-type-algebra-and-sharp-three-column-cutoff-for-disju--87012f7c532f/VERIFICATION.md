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

# Finite verification and proof boundary

The exact domain reduction for arbitrary column counts is proved by induction in `RESULT.md`. Finite data alone cannot replace that induction. The universal support-state domain contains \(64\) points. The five depth-at-most-two expressions give exactly eight nonempty fibers, and `closure_table.tsv` reports the induced operator's output mask for every one of the \(256\) Boolean unions of these fibers, using the signature order `00001,00100,00101,01111,10010,10100,10110,11111`.

Run `python3 support_checker.py` from the directory containing `closure_table.tsv`. Its completed output was:

`SUPPORT_ALGEBRA_OK 64 states, 8 atoms, 256 closure cases, depth 2, sizes 4/64/256`

Run `python3 direct_checker.py` from the same directory. Its completed output was:

`DIRECT_OK 1 columns 8 pointed instances 2 atoms`

`DIRECT_OK 2 columns 64 pointed instances 6 atoms`

`DIRECT_OK 3 columns 384 pointed instances 8 atoms`

`DIRECT_OK 4 columns 2048 pointed instances 8 atoms`

The latter computes directly from all labelled valuations of \(2\times m\) grids rather than relying on support compression. Both scripts use exact Boolean and integer arithmetic. Neither is an independent audit or an automated proof of historical novelty. The proof does not establish analogous counts for arbitrary product heights or the unbundled language.
