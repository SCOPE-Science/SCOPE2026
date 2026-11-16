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

Run `python degree8_definite_set_check.py` with Python 3, SymPy, and NumPy. It checks the exact Hermite-Laguerre expansion, independent Fourier transformation under the \(2\pi\)-unitary convention, discriminant and monotone critical cubic, stationary-root comparison, all coefficient signs in the Bernstein certificate, the exact optimizer's nonpositive-set length, and 14 additional numerical parameter configurations.

The checker is reproducible from the embedded package and exited successfully with `PASS: 22 exact structural identities and 14 independent numerical configurations`. Numeric configurations and finite algebra checks supplement, but cannot replace, the parameter-uniform proof in `RESULT.md`. The conclusion covers all real coefficients only within the three Hermite orders \(0,4,8\) and the normalization \(f(0)=0\). General eigenfunctions and independent external mathematical audit have not been checked.
