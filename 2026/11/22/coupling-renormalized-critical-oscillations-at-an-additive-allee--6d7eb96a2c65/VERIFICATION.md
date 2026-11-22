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

# Verification notes

The full proof is in `RESULT.md`, and `verify.py` is self-contained apart from SymPy.

1. Run `python verify.py` in the directory containing these two files. The expected success line is `FOLD_FLIP_COUPLED_CLOCK_VERIFY_OK` after four numerical diagnostics.
2. The checker symbolically verifies the exact host fold identity and the relevant two-step Taylor coefficients. It also tests the asymptotic constants for \((A,\beta)=(1/3,1)\) and \((3/5,4/5)\), in both sign wedges.
3. The infinite-time claim is established by the proof's trapping argument and squared-amplitude inequality; numerical tolerances are diagnostics only. In particular, the checker is not a certificate of asymptotic convergence or a substitute for checking the uniform remainder bounds.
4. The original source formula and its fold/flip discussion were inspected at https://doi.org/10.3390/axioms12111031. General fold–flip analyses for different maps are not directly transferable to this one.

The theorem covers local open wedges above the host fold, not all initial points. The independent audit status remains unperformed.

