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

# Verification and reproducibility

The theorem is established by the explicit normalized integral simplicial boundary and a degree-one CW attachment induction in `RESULT.md`. The `checker.py` script is a separate finite diagnostic: it enumerates ordered paths and their simplicial faces, reduces persistence over \(\mathbb F_2\), and checks predicted positive-length intervals through homological degree ten across 68 exact-cost test instances. Run with `python3 checker.py` using the Python standard library only.

Its recorded output is given in `CHECKER_OUTPUT.txt`; the script was also executed from the embedded-source path before packaging. The checking bound does not prove the infinite-dimensional statement or integral torsion-freeness. Those follow instead from the primitive integral boundary maps and Hurewicz/CW attaching argument.

Source priority comparisons are bounded by available full text and indexed research records; equivalent unindexed literature might exist. An independent mathematical audit has not been performed.
