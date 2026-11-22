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

Run `python3 verify.py` with ordinary Python 3 and its standard library. The checker reconstructs all truth tables for two- and three-element chains directly from the defining equations, tests every adjacent-edge expansion through six elements, evaluates congruence compatibility using the original operation tables rather than the claimed cut formula, and exhaustively checks all equivalence partitions through four elements. It independently compares the binomial-expanded profile polynomial, and constructs every possible exact cut pattern through thirteen elements. Its successful output terminates with `VERIFY_OK`.

The general edge normal form, exact cut criterion, inclusion–exclusion and asymptotic probability are proved in RESULT.md. Exhaustive checks at fixed sizes cannot establish these universal or asymptotic claims by themselves. Published general principal-congruence formulas provide contextual support but are not silently treated as the new enumerator. The older general finite weak-Heyting counting paper was not accessible in complete text, so historical-priority uncertainty remains.
