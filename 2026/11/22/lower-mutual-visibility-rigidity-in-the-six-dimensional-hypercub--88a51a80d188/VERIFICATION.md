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

# Verification scope

The complete proof for the finite \(Q_6\) claim consists of the elementary closed-neighborhood and XOR-translation arguments plus a finite exhaustive enumeration over every \(k\)-subset containing zero for \(2\le k\le7\). The `verify_permutations.cpp` program checks mutual visibility by explicitly testing all shortest coordinate-flip permutations and maximality by testing every one-vertex extension. It ends in `PERMUTATION_VERIFY_OK` after counting exactly seven normalized seven-vertex maximal solutions, each a closed neighborhood.

`verify_lattice.cpp` uses a different shortest-path algorithm: dynamic programming through the Boolean interval between two endpoints. It exhaustively repeats all normalized cardinalities \(2\) to \(6\), with zero maximal sets, and tests all 64 neighborhood constructions. It ends with `LATTICE_VERIFY_OK`. The expected output text for the first program is also supplied, but these recorded results are only corroboration; the executable predicate definitions and exhaustive loops are the actual certificates. No finite test certifies higher dimensions, no independent external audit has been conducted, and the title's novelty is subject to historical priority.
