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

## Reproducible checks

Save the included `verify.cpp` in the same directory and run `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. The verifier uses direct permutation composition to construct the multiplication table of the symmetric group, independently computes the quotient exterior-square formula, and exhaustively enumerates all ordered pairs in the 6-dimensional algebra for field orders 2, 3, and 4, checking every output fiber. In characteristic two it treats subtraction as addition; the order-four field uses a degree-two irreducible polynomial. A `VERIFY_OK` exit indicates all finite checks passed.

Expected finite counts: field 2: 4,096 ordered pairs; zero fiber 1,408, each of 7 nonzero attainable values 384. Field 3: 531,441 pairs; zero fiber 76,545, each of 26 other attainable values 17,496. Field 4: 16,777,216 pairs; zero fiber 1,294,336, each of 63 other attainable values 245,760.

## Limits

Finite enumeration does not prove a statement for arbitrary prime powers. The proof in `RESULT.md` derives the result from group multiplication, an exterior-square isomorphism and a uniform count of fixed-wedge representations. Independent mathematical validation has not been performed.
