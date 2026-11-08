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

Run `python verify.py` with Python 3 and SymPy installed. This script was executed from its actual package path and returned:

`VERIFY_OK cases=7 exact_symbolic=7 bounded_iterates=1428 max_amplitude_relative_error=0.000042`

Its seven parameter pairs include \(m=0\), \((m,h)=(1,0)\), and five interior cases satisfying \(c\ge0\). It checks exact polynomial differentiation, the flip equation, the cubic coefficient, and the cubic two-iterate expansion symbolically. Numerical checks confirm physical range on a 201-point mesh per case, the \(k^{-1/2}\) critical rate for 22,000 two-step iterations, and two-cycle amplitudes after 45,000 iterations at a small positive parameter offset.

The exact theorem for every admissible real parameter pair follows from the analytic arguments in RESULT.md, not from finite samples. The historical-priority comparison is not exhaustive, and no independent audit was performed.
