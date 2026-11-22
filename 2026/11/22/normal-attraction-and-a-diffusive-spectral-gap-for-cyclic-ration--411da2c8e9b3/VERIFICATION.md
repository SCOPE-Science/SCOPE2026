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

# Verification record

The checker `verify_floquet.py` was run as `python verify_floquet.py` with Python 3 and NumPy, and returned `PASS 103 return-spectrum, gap, and trajectory test groups`.

The tests construct the actual finite two-step Jacobian for ring sizes 2 through 16 and a range of cycle amplitudes, compare its eigenvalues with every factor of the analytic polynomial, check strict transverse stability, check the large-ring asymptotic against rings of size 200 and 400, and simulate perturbed orbits. The proof additionally verifies the symbolic identities \(A_o+A_e=1\), \(A_oA_e=B_oB_e=d\), and the exact Schur–Cohn strictness expression, which are not inferred from sampling.

Verification limits: finite tests do not certify statements for arbitrarily large rings. The proof of the strict inequalities and asymptotic expansion is analytic. The local attraction statement does not give a global basin description. No independent audit has been performed.
