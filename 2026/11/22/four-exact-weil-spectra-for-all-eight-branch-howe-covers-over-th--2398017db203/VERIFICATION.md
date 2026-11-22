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

The standalone exact checker is `scripts/verify.py`, run by `python3 scripts/verify.py` with no nonstandard packages. The check ran on the full 35 partitions and four square-class pairs, verifies all 140 \(\mathbb F_7\)- and \(\mathbb F_{49}\)-point counts by direct quadratic-character fiber summation, checks quartic cross-ratio orbit classes and complementary orbit agreement, determines the two elliptic traces, and matches the four Weil-spectrum frequencies, including the 84 maximal cases. Its output begins `EIGHT_BRANCH_HOWE_F7_VERIFIED 35 partitions 140 marked covers` and contains the full signed-trace table.

Critical mathematical premises independent of the finite experiment are the genus-five Riemann–Hurwitz count, the character-isotypic cohomology factorization, the Weil-equality argument for the genus-three factor, and the projective cross-ratio orbit counting. The checker is exhaustive only over the specified finite marked family; it does not prove originality, classify unmarked curves, or perform an independent audit.
