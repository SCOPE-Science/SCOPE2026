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

The general theorem follows by the degree-three Bézout bound, the finite abelian-group zero-sum partition theorem, and the group Cayley-table near-transversal theorem, as detailed in RESULT.md. Both cited external group results have been checked at their stated theorems in lawful open full texts.

Run `python verify.py`. The script uses only the Python standard library. It exhaustively tests the explicit cyclic zero-sum construction for \(1\le k\le500\); independently enumerates rational points and every projective line for six short Weierstrass cubics; and computes the exact finite minimum set cover using subset dynamic programming. The checked curves have group sizes divisible by three and represent the two possible involution types.

Expected terminal markers:
```
CYCLIC_NEAR_COVER_CONSTRUCTION_OK 500
ELLIPTIC_CUBIC_LINE_COVER_CHECKS_OK
```

These are finite checks, not proofs for arbitrary field size or arbitrary elliptic-curve group. The general conclusion depends on the published zero-sum partition and near-transversal theorems and the group law on a smooth plane cubic.
