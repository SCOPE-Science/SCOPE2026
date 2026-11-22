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

# Verification and scope

Run `python3 check.py` in the same directory as `RESULT.md`; it uses only Python 3's standard library, requires no downloaded data or seed, and reports `ALL_CHECKS_PASS` on successful completion. The bundled `verification_output.txt` contains the exact output from the supplied source. Computations use exact integer arithmetic.

The checker performs 255 independent direct-word versus transfer-matrix tests for every path orientation through eight vertices, 45,057 comparisons for every coordinatewise switch change with orientations through fourteen vertices, and 4,097 independent prefix/suffix factor checks through eleven vertices. For every path size from one through fourteen, the two extremal counts are cross-checked with the stated cubic recurrences. These bounded tests do not prove the all-order assertion: the independent mathematical justification is the all-order bijection and strict factorization in `RESULT.md`, followed by Cayley–Hamilton and Perron–Frobenius theory. No independent audit or external certification was performed.
