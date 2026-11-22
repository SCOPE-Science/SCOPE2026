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

# Reproduction

Execute `python3 verify.py` with Python 3.10 or later (standard library only). The script enumerates 1,295 directed-forest nonempty faces and all 53,845 strict face flags, computes complete even-permutation orbits, constructs the corresponding oriented integral quotient boundary matrices, checks every consecutive boundary composition, and performs 451 exact unit-pivot chain cancellations. It reports a chain-equivalent complex having one degree-zero and five degree-three cells and zero remaining differentials. An independent signed fixed-face Lefschetz sum confirms the Euler characteristic and the separately reconstructed full symmetric quotient provides a cross-check. `verification_output.txt` was recorded from an actual run of the embedded program.

These calculations verify the finite integral homology computation but do not, by themselves, prove the homotopy equivalence. The complete-source shellability theorem, Armstrong's orbit-space fundamental-group formula, and the Hurewicz–Whitehead argument are needed for that conclusion. No independent audit has been performed.
