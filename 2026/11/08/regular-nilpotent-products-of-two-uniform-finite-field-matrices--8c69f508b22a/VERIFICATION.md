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

# Reproducible mathematical checks

Run the included standard-library Python checker as `python3 verify_regular.py` and compare its entire output with `regular_output.txt`. It exhaustively enumerates products at four small field/dimension combinations, including \(\mathbb F_4\), and verifies the regular-nilpotent condition by powers. It separately enumerates all ordered pairs at \((q,n)=(2,3)\) to check the claimed single-target Jordan-block fiber. The exact count is derived symbolically in `RESULT.md` for all prime powers and dimensions; these finite checks cannot prove its unrestricted quantifiers. The checker algebraically matches the count-derived probability with the finite-product expression for \(203\) additional \((q,n)\) parameter combinations. No external audit or certification is represented.

The reported counts are 54, 960, 6300, 21168 regular-nilpotent products for the respective exhaustive \((q,n)\) cases. The exact Jordan-target fiber at \((q,n)=(2,3)\) is 504. Failed or unperformed checks must not be inferred from the presence of this log; source code and the complete derivation supply the scientific evidence.
