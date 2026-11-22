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

The proof is a complete finite census of all ternary arc assignments through five old vertices, plus exact counting identities. `verify.cpp` enumerates all diagrams, all unary extension vectors, all compatible directed-pair vectors, and all vertex permutations and global arc reversals. Run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`; output is recorded in `verification_output.txt`. The output includes the exhaustive class totals, the unique five-vertex double fiber, and the exact three-point counts.

`crosscheck.py` independently computes the two explicit witnesses by direct enumeration of all admissible old/new three-vertex diagrams. Run `python3 crosscheck.py`; it must report `INDEPENDENT_FINITE_EXTENSION_CHECK_OK`.

Limitations: finite exhaustiveness stops at five old vertices. No result about all larger bases or all higher arities is asserted. The finite computations use integer arithmetic. An independent mathematical audit has not been performed.
