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

The theorem uses a direct component-inventory proof. The programs are independent finite checks and do not replace its universal argument.

Run `python3 verify_inventory.py` using only the standard library. Its complete output is saved in `verify_inventory_output.txt`. It compares every support through the indicated finite cutoffs against direct enumeration of all row-quota/column-quota products, and separately counts star forests on active labeled vertices.

Compile and run `g++ -O3 -std=c++17 verify_uniform.cpp -o verify_uniform && ./verify_uniform`. Its recorded output is `verify_uniform_output.txt`. The six-by-six, quota-three-by-three case directly enumerates all supports through size four. The five-by-five, quota-three-by-three case additionally excludes every size-five support. Exact finite checks also cover the smaller displayed parameter tuples.

The inventory criterion follows from enumerating every local star selection consistent with positive labels, using independent coordinate selection outside the query support. Its sufficiency and necessity are mathematical proofs, not extrapolations from the finite tests.

Limitations: the complete polynomial for small unpadded grids is specified by a finite test rather than a single closed generating expression; no adaptive dimension is asserted; historical priority remains subject to external assessment.
