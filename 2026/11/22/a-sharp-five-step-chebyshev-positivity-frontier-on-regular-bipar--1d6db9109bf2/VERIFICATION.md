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

# Verification performed

The bundled `verify.py` uses exact rational arithmetic without third-party packages. Executing it produces 572 checks of polynomial divided differences, small-cube path probabilities, constant-row actions, the adjacent-pair formula and the explicit negative rational witness. It also verifies that the stated strictly positive perturbation preserves a negative fifth-step output coordinate.

# Analytical checks and limits

The finite tests do **not** prove the global assertion. The accompanying proof establishes it independently by coefficientwise positivity for \(1\le m\le4\), sign classification of the degree-five divided difference for \(z\ge\sqrt5/2\), and the exact three-step walk count on hypercubes for each \(1<z<\sqrt5/2\). The claim concerns final iterates with exact spectral bounds; roundoff, inexact spectral bounds and internal-stage positivity have not been assessed.

Independent audit: not performed.
