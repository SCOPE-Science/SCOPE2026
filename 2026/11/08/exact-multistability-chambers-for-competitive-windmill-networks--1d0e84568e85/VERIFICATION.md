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

# Reproducibility and verification

This package contains `verify.py`, a standalone Python 3 script using only the standard library. Run `python3 verify.py` in a directory containing the extracted script. It independently builds the full \((2k+1)\)-species matrix, enumerates all nonempty supports, solves supported equilibrium linear equations with rational arithmetic, applies an exact positive-definiteness criterion, and checks every missing-species invasion exponent against the classification.

The script passed 84 exact full-support comparisons at sizes \(k=2,3,4\) over four pair-competition strengths and seven hub-competition strengths (excluding transition-curve instances). The proof in RESULT.md—not these finitely many checks—establishes the theorem for arbitrary \(k\ge2\).

The review is limited to the mathematical result in the open parameter chambers. No independent mathematical audit or external certification has been carried out. Unindexed literature equivalences remain possible.
