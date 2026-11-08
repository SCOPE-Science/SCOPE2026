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
# Verification

Run `python3 verify.py` with the standard Python library. The executable constructs the uniform fixed points without external data and tests phase-recognizability, exact initial Lie values, the congruence obstruction, the cyclic source-extension bijection, and the value at length \(2b\), for bases \(3\) through \(8\) and lengths \(1\) through \(68\).

Observed output:

`VERIFY_OK bases=3..8 length_tests=408 phase_words=66 check=Lie_and_extension_equivalence`

The exhaustive finite checks are diagnostics only. The theorem for unbounded bases and lengths rests on the explicit phase and desubstitution arguments in `RESULT.md`. No independent validation or external formal certification has been performed.
