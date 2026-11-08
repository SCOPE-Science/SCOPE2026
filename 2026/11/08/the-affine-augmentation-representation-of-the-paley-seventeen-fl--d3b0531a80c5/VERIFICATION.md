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
# Verification record

Run `python3 verify_paley17.py` in the directory containing the two supporting artifacts. The script requires Python 3 only and independently recomputes all mathematical data. Its output is recorded in `verification_output.txt`. It checks the 16-edge spanning tree; one by one, all 52 remaining graph edges are killed by explicit triangular null-homotopy relations in 50 and two additions, proving simple connectivity. The triangle-boundary rank is 52 in characteristics 2, 3, 5 and 17. All 136 signed affine Lefschetz traces agree with the 17-point augmentation module, including the 17 orientation-reversing involution calculations.

The final rank-and-character theorem is finite and exact; no numerical check is presented as proof of a different graph order. Character equality proves rational rather than integral representation equivalence. Independent external audit is not performed.
