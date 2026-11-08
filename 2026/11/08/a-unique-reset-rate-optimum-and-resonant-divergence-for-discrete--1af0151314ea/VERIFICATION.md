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

The included `verify_qfi.py` is standalone and uses NumPy and SymPy. Its last replay from the assembled finding package reported `PASS: 171 algebraic, matrix-SLD, series, root and asymptotic checks`. These checks independently evaluate the symmetric logarithmic derivative from density-matrix eigenvectors, compare the exact stationary geometric sum and verify the symbolic polynomial identities. The mathematical proof of uniqueness uses Descartes' rule, not a finite grid or root enumeration. The resonance analysis is an asymptotic statement, and the finite near-resonance computations only check its consistency. No independent scientific audit has been performed.
