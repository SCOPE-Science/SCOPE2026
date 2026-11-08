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

The analytic proof is in `RESULT.md`. The Fourier inverse identity follows from standard character orthogonality; the support-uniqueness step uses invertibility of \(2\) modulo odd \(n\); zero-lag inversion uses strict monotonicity of the second mask. All allowed one- and two-sparse cases and the zero signal have been handled. The even-grid counterexample holds algebraically for every real mask, including negative and vanishing entries.

`CHECK.py` (Python 3 with NumPy installed via `requirements.txt`) performs finite, supplementary tests for odd grid sizes \(3,5,7,9,11,15,21,31\) and even grid sizes \(4,6,8,10,12,16,28\). It checks 905 support signatures and 2,866 test cases, including randomized complex amplitudes, full intensity arrays, direct reconstruction up to a global phase and arbitrary real masks against the exact even-grid ambiguity.

Expected successful terminal line:

`CHECK_OK phase_recovery_tests=2866 exact_support_signatures=905`

Numerical tests do not prove the theorem; infinite-dimensional quantifiers in the statement are established by the proof. The analytic result does not establish stability or nonasymptotic error bounds. The literature overlap review is not an independent audit.
