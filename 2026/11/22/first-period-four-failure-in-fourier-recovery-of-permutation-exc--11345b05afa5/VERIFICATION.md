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

## Reproducibility
Compile the standalone `verify.cpp` using `g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify` and run `./verify`. The executable prints the nullity/rank pair for each order from one to nineteen and the final PASS line.

The program derives a complete spectrum in two independent ways: (1) Ferrers-board rook coefficients and the signed factorial formula; (2) exact word-count recurrence and Walsh–Hadamard transform. It checks equality at **all 524287 frequency/order pairs**, direct permutation enumeration through order eight, reversal duality, the list of twenty-four zero masks at order nineteen, inertia, sharp minimum and first failed residue-class order. Both combinatorial identities are justified in `RESULT.md`, so the checker is an exhaustive certificate of a finite theorem, not a proposed proof of an infinite conjecture.

The zero-set file lists the complete mask set at order nineteen. All counts use exact integers and no statistical tolerances. The code does not claim independent external validation. The archival origin for the explicitly dated source is arXiv:1403.0691 on 2014-03-04; the more foundational older publication gives month/year only.
