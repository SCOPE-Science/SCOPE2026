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

# Reproducibility

Run `python3 artifacts/verify.py` in a directory containing that script, without third-party packages. The program checks the nine-vertex fiber kernel, enumerates all \(1024\) possible supports of the ten identified negative curves, tests negative definiteness independently by exact fraction-free determinant elimination and rational \(LDL^T\) elimination, verifies all ten support-size coefficients, and prints the three exclusions. The recorded output is `artifacts/verification.log`. This is an exact finite check, not a substitute for the geometric proof that the listed curves exhaust all negative irreducible curves.

Independent mathematical validation has not been performed. The novelty review is based on inspected primary literature and targeted searches and does not establish historical uniqueness.
