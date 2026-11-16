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
# Verification of the exact cycle-colouring Fourier formula

The supplied `checker.py` is standalone Python 3.10+ code requiring only the standard library. Execute `python3 checker.py` from the directory containing it.

It constructs the proper-colouring indicator independently for each dimension \(3\le n\le10\), performs the entire multidimensional ternary Fourier transform using exact integers in \(\mathbb Z[\omega]\) with \(1+\omega+\omega^2=0\), and then checks each coefficient against the theorem, including both zero and nonzero cases. It additionally verifies every nonzero value is divisible by three and compares the calculated additional-nullity with the factorial formula. The total compared values are 88,560.

Successful execution ends with `TERNARY_CYCLE_FULL_FOURIER_PASS total_coefficients=88560`. The evaluated ranks, in order for lengths three through ten, are 9, 15, 81, 243, 519, 2187, 6561, 15483.

The proof for arbitrary length is supplied in `RESULT.md`. Neither finite tests nor this self-review constitute independent external verification. The scope excludes larger colour alphabets and any claim of a complete nonzero magnitude distribution.
