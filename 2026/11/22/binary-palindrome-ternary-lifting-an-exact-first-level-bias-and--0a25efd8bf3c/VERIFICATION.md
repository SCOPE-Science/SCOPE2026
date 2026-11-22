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

The standalone `verify.py` uses only Python 3's standard library. Execute `python verify.py` in the extracted directory. The direct exact-integer enumerator checks 131071 canonical even-length binary palindromes with half-length 1 through 17 against every first-lift histogram. Separately it checks 2850 digit coefficients against both the congruence and the exact three-adic valuation lemma. Finally it constructs an explicit assignment of free binary digits for each of the 1092 targets at prime-power levels 2 through 7 using the two-coefficient greedy lift. The finite checks pass. The proof in `RESULT.md`, rather than finite exhaustion, establishes the statements for all lengths and all powers. External independent audit remains unperformed.
