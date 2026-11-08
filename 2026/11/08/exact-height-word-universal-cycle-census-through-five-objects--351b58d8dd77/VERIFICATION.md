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

The two programs `verify_exact.py` and `crosscheck.py` require Python 3 and its standard library only. They do not use stored log outcomes as proof. Run both in the directory containing `core_edges_n5.tsv`.

`verify_exact.py` reconstructs all valid height words, verifies that every original edge occurs in exactly one recorded corridor, computes the matrix-tree cofactors by exact Bareiss elimination, and recomputes all count products. It also byte-compares every logical certificate row with the reconstructed paths and returns `VERIFY_OK`.

`crosscheck.py` enumerates valid words via a different surjective-alphabet construction, checks every determinant by modular elimination and exact CRT under a Hadamard bound, uses the full uncontracted graph at orders two through four, and separately enumerates all order-three Euler circuits from one fixed starting edge. It returns `CROSSCHECK_OK`.

At order five, the source graph has 308 vertices and 541 distinct arcs; the reduced graph has 75 vertices and 308 distinct contracted arcs. The cofactor is \(27571102170646823740986252600397906575360\); the degree-factorial factor is \(225390057412667141559249255183922002204556655201227127499578671104\). The result counts cyclic rotations once and does not identify rank labels. There is no independent scientific review or verification beyond the reported checks.
