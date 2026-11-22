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

# Reproducibility and limits

Run `python check_colex.py` using Python 3 and SciPy. The script checks for moduli 2 through 12 that the explicitly proposed order obeys both co-lex axioms, that the complete automaton has 2m+1 distinct minimal states, and that membership matches direct factor and length tests on 720885 words. This numerical verification is finite and does not prove the all-modulus result. The structural proof establishes the general lower and upper bounds. The program is verification code, not an independent audit. The minimum *language* width over arbitrary equivalent DFAs is not determined.
