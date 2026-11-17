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

# Verification scope
The theorem is proved using finite-group GNS, spectral Fourier decomposition for finite abelian groups, and explicit states of the generalized dihedral group. The proof does not rely on finite experiments to infer a universal statement.

# Reproducible diagnostics
Run `python check_extension.py` with Python 3 and NumPy. A successful execution prints `PASS 2638 finite diagnostics; universal theorem uses the analytic proof`. The script checks normalized reflection values, Hermitian positive semidefinite full-group Gram matrices, identity/endpoint cases, and exact Fourier norm of the one-negative obstruction in several cyclic groups. It is supplementary, not a general proof of the arbitrary-group case.

# Limits
No independent audit has been performed. The proof covers finite abelian base groups and scalar data only. Literature searches identified relevant general extension theory but cannot exclude an older equivalent Fourier–Stieltjes restriction result.
