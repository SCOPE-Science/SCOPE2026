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
# Reproduction and scope

Run `python CHECK.py` from the directory containing this document, with Python 3, SymPy and SciPy installed. The script contains the exact primary-source polynomial coefficients and checks the complete radial polynomial identity and both components of the phase-parameterized original-time ODE. It then checks normalization, the physical period, and the squared-position moment formula by direct numerical integration for four parameter values, and verifies the exact Cauchy density transformation at five tangent coordinates in each numerical case.

The precise source date, 2023-12-14, appears on page one of the primary article. The finite checks are diagnostic, not proofs of the asymptotic claims; the rigorous argument is contained in `RESULT.md`. At \(w=4\) the periodic orbit degenerates, and the asymptotics are one-sided from \(0<w<4\). No independent review is asserted.
