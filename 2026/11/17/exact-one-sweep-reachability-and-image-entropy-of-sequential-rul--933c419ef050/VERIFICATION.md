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

The target map is the labelled, in-place, left-to-right Rule 30 sweep on cyclic rings of lengths at least three. The algebraic proof derives a necessary and sufficient predecessor criterion, a 12-element Boolean-relation semigroup, and a finite vector identity implying the recurrence at all lengths. `verify_relation.py` regenerates that table from the two elementary relation matrices and checks every component of the polynomial annihilation identity over integers. `verify_direct.py` independently simulates all binary inputs through ring length 16; for lengths 3 through 12 it also checks each target against an explicit inverse-construction routine. Both scripts were executed on their packaged bytes using Python 3 standard-library only, and their output was compared with the accompanying `.txt` files.

The brute-force tests are finite and do not by themselves prove the infinite-length theorem. No experimental claim about future scans, arbitrary update orders, or stochastic dynamics is made. Historical priority remains open to inaccessible or unindexed literature. Independent external mathematical audit has not been performed.
