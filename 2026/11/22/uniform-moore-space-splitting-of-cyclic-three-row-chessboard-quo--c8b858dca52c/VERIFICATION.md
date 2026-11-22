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

The family theorem has a symbolic, all-integer proof in `RESULT.md`, steps 1–4. It reduces the quotient to a one-loop presentation whose attaching degrees are exactly zero or minus the group order, and includes one nonzero attaching degree. Two-cell Nielsen operations produce the standard Moore-space summand plus free two-sphere summands.

Run `python3 verification/verify.py` in the package directory. The program uses Python 3's standard library only and re-enumerates actual rook faces at widths five through ten, checks the free column orbits and quotient boundary compositions, and tests modular ranks. It also checks the written symbolic degree formula for all widths five through one hundred. These tests are reproducible corroboration but are not substituted for the proof for arbitrary widths. The source texts cited in `RESULT.md` supply classical background and comparisons, not an independent validation of this claim.
