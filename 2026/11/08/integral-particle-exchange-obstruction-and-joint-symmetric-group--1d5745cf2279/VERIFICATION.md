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

# Reproducibility and proof limits
Run `python3 verify.py` with a standard Python 3 interpreter. Compare the program's stdout byte-for-byte with `verify_output.txt`.

The checker independently builds the ordered two-particle cubical cells after two-edge subdivision of each arm, enumerates every arm-permutation/label-exchange action for \(m=3,4,5,6\), verifies the signed Lefschetz traces against the all-parameter predictions, and checks the mod-two parity-image rank on an integral fundamental-cycle basis of the crown graph. These are 1,740 finite group-element checks, not a proof for arbitrary \(m\).

The all-parameter result instead rests on the explicit equivariant continuous deformation retraction to the crown graph, the oriented cellular chain model, the integral mod-two cycle-space calculation for the precise parity quotient, and the symmetric-group permutation-module decomposition. None of these steps relies on a timeout, numerical rank approximation, or unchecked experimental extrapolation.

Limitations: no result on three or more particles, unequal-arm symmetry, or the additional \(S_m\)-module structure of the obstruction. Independent audit not performed.
