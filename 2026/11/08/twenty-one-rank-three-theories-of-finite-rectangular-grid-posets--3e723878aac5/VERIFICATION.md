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

The accompanying `checker.py` is a self-contained Python 3 script requiring no third-party modules. Execute `python3 checker.py`; its output is:

`GRID_RANK3_CERTIFICATE_OK cases=28 classes=21 pair_checks=784 direct_games=55 terminal_minimum=30`

The script constructs exact comparison matrices for all 28 grids with normalized side lengths between 1 and 7, computes the nested three-move atomic signatures for every grid, compares all 784 ordered grid pairs against the claimed 21-class partition, and independently executes a direct Spoiler/Duplicator recursive game for all 55 unordered pairs (with repetition) of the ten grids with both side lengths at most four.

The mathematical reduction from arbitrary side lengths to at most seven uses a three-round EF interval strategy on each factor and a coordinatewise product strategy. No finite experimentation alone is used to justify statements for unbounded side lengths. The signature algorithm is an exact complete finite decision procedure for three-move equivalence by the back-and-forth characterization.

The claim does not extend the minimality statement beyond the rectangular-grid-poset family. This package has not received independent expert audit or formal verification.
