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

# Reproducible checks

Use `python3 verify_fano.py` and compare its stdout with `verify_output.txt`. Only the Python standard library is needed. The exact integer incidence matrix is generated from the seven nonzero binary triples with incidence parity zero. The verifier constructs the \(14\times14\) intersection form and enumerates every one of its \(16384\) principal subsets. One check computes induced matching degrees; a second, arithmetically independent check uses exact rational Schur elimination for negative definiteness. Each mask is tested, and every support-size coefficient and the total are asserted. On success stdout ends `ALL_CHECKS_PASSED`.

The proof of completeness of the negative-curve list, the anticanonical basepoint argument, and the Zariski-chamber correspondence are mathematical arguments in RESULT.md, not consequences of the 16384-mask program. The latter is an exhaustive finite computation because there are exactly fourteen geometrically proved negative curves. This check does not independently confirm historical priority or supply an external scientific audit.
