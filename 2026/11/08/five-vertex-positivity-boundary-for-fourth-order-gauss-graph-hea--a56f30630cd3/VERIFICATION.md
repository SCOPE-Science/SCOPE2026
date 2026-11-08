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

Run `python verify.py` with Python 3 and the standard library. The script computes the two-stage Gauss endpoint map through exact rational matrix inversion and checks all small-cycle rational entry formulas at enough distinct rational timesteps to establish the formulas as rational-function identities (cleared numerator degree at most \(4n\)). It also checks the exact negative \(C_6\) entry at \(h=8\), certifies the strict rational square-root bounds and geometric-tail inequality used for all \(n\ge7\), and tests the cycle Green-kernel formula at thirty sizes as a supplementary consistency check.

Expected console output:

`VERIFY_OK 212 exact small-cycle identities; exact C6 witness; rational Fourier bounds; Green-function tests`

The Green-kernel proof for all sizes is an algebraic second-difference identity presented in the result, not an extrapolation from thirty tests. The h=8 tail estimate is proved for all \(n\ge7\) by its geometric majorant, with the constants certified by rational comparisons. No independent specialist audit or formal proof-assistant verification has been performed.
