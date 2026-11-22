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

# Reproduction and verification

The full proof is in `RESULT.md`. It starts from the two generalized principal eigenproblems, uses the mean-zero Neumann Poisson solution at first order, and checks the extra non-divergence term at second order. The proof establishes the continuum conclusion; computational evidence alone does not.

Run `python check.py` in a Python environment with NumPy and SciPy. The script checks the exact rational quadratic coefficients in both trigonometric witness families and independently calculates reproduction numbers by symmetric Neumann cosine-Galerkin variational matrices, with 15 basis functions and 96 Gaussian quadrature nodes. Tested amplitudes are \(\varepsilon=0.05\), \(0.02\), and \(0.01\).

At \(\varepsilon=0.01\), the computed values are \((\mathcal R_F,\mathcal R_P)=(0.999987488757,1.000012469867)\) for the first witness and \((1.000012481256,0.999987485472)\) for the second. Each agrees in sign with the exact asymptotics. Because only finitely many modes and parameter values were computed, these calculations cannot serve as an exhaustive stability certificate or an infinite-dimensional proof.

Source definitions inspected: Liu, Wang and Zhang (2026), equations (3.7) and (3.12), Section 3, DOI 10.1017/S0956792526100448. Earlier competing background read: Wang, Wang and Kim (2022), Sections 1–5, DOI 10.1137/22M1485814.
