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

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py`; its actual replay output is stored in `VERIFY_OUTPUT.txt`. It performs sparse symbolic arithmetic modulo three for all Hasse–Witt entries, verifies the discriminant substitution and boundary identities, and exhaustively counts smooth Ciani coefficient triples over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It also checks that the chosen finite-field quotient tables have no zero divisors.

The proof in `RESULT.md` independently supplies the arbitrary-field derivative and Čech-Frobenius arguments, the geometric normal crossing assertion, and a universal quadratic-character count for all \(q=3^n\). Three small-field enumerations do **not** prove an all-extension theorem, so the character-sum argument is essential. The prime-to-three elliptic isogeny is standard published input, with exact source given in the references; it is not independently reproved by the checker.

This is a self-review, not independent validation. Historical priority is provisional.
