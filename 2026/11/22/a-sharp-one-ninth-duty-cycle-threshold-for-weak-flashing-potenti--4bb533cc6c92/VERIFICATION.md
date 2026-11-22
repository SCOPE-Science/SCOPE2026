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

The entire test is self-contained aside from NumPy. Run `python CHECK.py` in a directory with this file. The Fourier-collocation solver constructs both the stationary measure and the periodic backward Poisson corrector for each force amplitude. It then computes the effective diffusivity through the exact continuous-martingale-plus-redraw-jump quadratic-variation formula. The test checks 18 finite-force rate/duty pairs, zero-drift symmetry, convergence of the normalized quadratic correction and 27 root/sign/optimization cases; it prints `PASS: 45 independent numerical and algebraic cases`.

The mathematical proof does not depend on the numerical output. Finite Fourier truncation alone cannot certify the sign for arbitrary amplitude, a continuous range of rates, or the whole infinite line. Instead those statements are derived from analytic perturbation theory and the exact quadratic coefficient. The \(O(\varepsilon^4)\) remainder is pointwise for fixed positive noncritical parameters, and no quantitative uniform amplitude bound is asserted. Independent audit remains not performed.
