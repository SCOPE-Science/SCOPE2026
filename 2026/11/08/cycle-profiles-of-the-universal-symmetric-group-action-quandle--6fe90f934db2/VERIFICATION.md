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

The standalone computational checker `verify.py` uses only the Python standard library. Its group operation is an explicitly implemented right-action permutation composition; the right translations are constructed directly from the quandle operation and iterated, without using the power formula in the predicted-count computation.

Run `python3 verify.py` in the directory containing this document. The expected output is recorded in `verify_output.txt`: `VERIFY_OK fixed_power_tests=230 full_profiles=11 n_max=6` followed by `S4_four_cycle_profile=1^4 2^2 4^16 12^2`.

The program compares exact fixed counts for all permutation cycle types through degree five and two representative degree-six types, over the powers stated in the proof. It independently constructs all cycles through degree four, and compares the partition-sum formula in degrees one through five. These finite checks do not certify a universal statement; the mathematical proof is in `RESULT.md`.

Critical reasoning independently checked in the proof: repeated right translation, centralizer parametrization, uniform block orbit length, uniform total cyclic shift, coprime solvability of the shift equation, the number-theoretic inversion, and the double counting of partition part sizes. Main residual historical risk: an equivalent cycle-index formula might exist under matrix-rack or quandle-profile terminology.
