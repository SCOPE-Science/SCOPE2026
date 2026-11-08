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

The arithmetic checker `verify.py` was run with Python 3 using its standard library only. It returned `VERIFY_OK: 33 exact graph/noise cases`.

It constructs all underlying graphs for \(m\in\{1,2,3\}\), \(s\in\{2,3,4\}\) and \(c\in\{1/2,2/3,4/5\}\), solves the full pair-chain stationary equations with fractions, independently derives the reduced three-orbit equations, and calculates both observable lag correlations from random-walk kernels. Every model-to-reduced and inverse-recovery identity was exact, including the one-blade boundary. For star boundaries, six additional rational cases at \(s=1\), \(m\in\{1,2,4\}\) and \(c\in\{1/2,2/3\}\) verified the hub correlations \((0,q)\).

The infinity-wide claims that \(m\) and \(s\) are unique and that stationary correlations are monotone are supported by the analytical fixed-point proof in `RESULT.md`, *not* by the finite checker. This verification is same-model only and is not independent validation.
