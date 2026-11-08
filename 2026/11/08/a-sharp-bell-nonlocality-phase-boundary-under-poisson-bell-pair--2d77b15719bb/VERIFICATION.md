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

# Reproducibility and verification

Run `python checker.py` using SymPy, NumPy, and SciPy. The script reconstructs the full two-qubit Lindblad generator in a column-vectorized matrix representation and computes the stationary state as the exact resolvent \(r(rI-\mathcal L_0)^{-1}\operatorname{vec}(\rho_0)\) for several exact-rational and many floating parameters. Its CHSH computation diagonalizes a directly constructed Pauli-correlation Gram matrix rather than reusing the claimed singular-value formula, and its concurrence computation uses eigenvalues of the Wootters spin-flip product rather than the X-state shortcut.

The tested source file reported: `PASS: 491 symbolic, independent Lindbladian, concurrence, CHSH and phase assertions`; `critical x0=3.204257578046, b0=1.327246946163`.

The universal root uniqueness uses a one-sign-change polynomial argument; the critical-branch uniqueness uses monotonicity of \(v\) above \(\sqrt2\); the large-dephasing asymptotic uses a rescaled-polynomial squeeze. These are analytical arguments and not consequences of finite tests. No independent external scientific audit has been undertaken.
