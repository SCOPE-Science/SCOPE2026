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

# Reproduction and scope

Run `python3 verify.py` using Python 3 (standard library only). Expected terminal line begins `VERIFY_OK 634 independent parameter instances`.

The checker independently enumerates cyclic rotations and exact right-residual languages by prefix length for all positive \(a,b\le22\). It builds a separate prefix trie and minimizes it from the leaves, obtaining the total number of states independently of the residual-set counter. For all such pairs it checks the entire predicted depth profile and exact state count. It then tests 150 pseudorandom, deterministically seeded pairs with run lengths up to 100 and checks the independent algebraic collision count at every intermediate depth.

Finite tests neither settle originality nor certify an infinite family. General correctness comes from the boundary-phase residual argument in `RESULT.md`. The source review was not an independent scientific audit and possible unindexed equivalents remain a bibliographic risk.
