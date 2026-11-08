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

The main geometric argument is contained in `RESULT.md`. `verify.py` uses exact arithmetic in SymPy and has no network dependency. Execute `python verify.py`; the recorded output, including the terminal marker `ALL_CHECKS_PASSED`, is embedded in `verify_output.txt`.

The program checks the logarithmic Gauss-map identity and reciprocal symmetry symbolically. For the examples \((m,n,\lambda)=(2,2,4),(2,3,4),(3,5,9),(4,2,16),(7,6,25)\), it checks exact critical directions, ramification-partition totals, Riemann--Hurwitz, and a faithful permutation representation of the proposed deck group with inversion relations. It does **not** itself prove irreducibility, global smoothness, or the full statement for arbitrary parameters; these are proved algebraically in the result and require verification of the stated field/valuation arguments.

All assertions concern the logarithmic Gauss map over \(\mathbb C\), not the classical projective Gauss map of an arbitrary embedding. No independent scientific audit has been performed.
