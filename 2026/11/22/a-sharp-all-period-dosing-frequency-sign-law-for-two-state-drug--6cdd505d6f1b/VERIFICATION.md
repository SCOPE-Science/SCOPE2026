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

The exact Floquet trace identity is derived in `RESULT.md`, including the h>-1 condition, strict Jensen and extrapolation cases, and endpoint limits. `checker.py` performs symbolic matrix equalities, rational strict-inequality certificates for the witness, numerical Floquet exponent comparisons for 500 deterministic positive-off-diagonal matrix pairs, and a T=4 simulation. It was run successfully using Python, SymPy, NumPy and SciPy. These checks corroborate but do not replace the analytic universal proof. A full-text historical comparison for Patra–Klumpp (2015) remains unperformed; no independent audit has occurred.
