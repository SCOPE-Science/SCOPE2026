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

`verify.py` was executed against the packaged derivation and returned `VERIFY_OK 4320 direct vector steps, symbolic and exact rational identities`. It checks the exact fixed-point equation, its local multiplier, the Babylonian identity, rational two-cycle involutions, and direct vector updates of a tall orthogonal-column least-squares system for several positive scalings, relaxations and starting distances.

The global attraction proof uses the analytical identity \(s_{k+1}=a s_k+(1-a)/s_k\), together with the strict decrease of \(\lvert\log s_k\rvert\), not finite numerical testing. Exact boundary assumptions are \(m>n\ge1\), \(A^{\mathsf T}A=\lambda I\), fixed nonzero \(z\in\ker A^{\mathsf T}\), \(x_0\ne x_\star\), and \(\omega\in[1,2)\). General matrices, row sampling, refreshed noise and extended normal-equation solvers have not been verified by this result.
