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

# Exact verification

The embedded `verify.py` is standalone Python 3 code using only the standard library. It generates all thirty-five line masks and all 3,048 nonempty line-free faces; counts every invertible ordered four-vector basis (20,160), evaluates all invariant cycle unions by the augmented trace identity, checks exactly twelve character profiles, and confirms that the character average is zero. A separate implementation computes signed oriented-chain traces on one example in every profile, avoiding the cycle-count sign simplification. The recorded output is `verification_output.txt`.

The published nonequivariant integral Morse theorem is a necessary premise for interpreting the alternating Lefschetz number as the single fourth-degree rational homology trace. The program does not reconstruct that historical theorem; in particular a finite trace log cannot substitute for it. The quotient claim uses rational transfer only. No integral quotient or complete integral representation calculation is made.
