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

## Computational verification

Run `python3 verify_direct.py` and `python3 verify_gap.py` using only the Python 3 standard library. The saved exact stdout outputs are included as `direct_output.txt` and `gap_output.txt`. The first executable enumerates deletion masks directly, groups fixed deleted and residual words, and checks exact cardinalities, deficits and multiplicities in every nontrivial fiber. The second executable independently uses cyclic block starts and one extra deleted position, checking source-coordinate accounting across a larger range of alphabets and exponents. Actual test ranges and counts are printed in the output files.

Both programs were executed successfully. The checks are finite; the all-parameter result follows from the explicit congruence and gap-counting proof in `RESULT.md`. No independent audit or external formal certification has been performed.
