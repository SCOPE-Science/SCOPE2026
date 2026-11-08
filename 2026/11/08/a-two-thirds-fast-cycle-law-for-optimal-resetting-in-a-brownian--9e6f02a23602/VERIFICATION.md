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

`verify_claim.py` is a standalone Python 3 script requiring SymPy and SciPy. Run it from the directory containing `RESULT.md` and `verify_claim.py` with `python verify_claim.py`.

The program explicitly solves the two-stage moment fixed point, checks its contraction-derived difference factor symbolically, checks the parameter identity for \(K\), computes three independent rational-parameter Taylor-coefficient cases for the hyperbolic factor, and verifies the derivative identity for the scaling-limit minimization. It independently integrates the two thermal-stage moment ODEs using an adaptive ODE solver and compares the resulting instantaneous quench work to the exact formula for four parameter pairs. Finally it optimizes the exact rate-dependent work for decreasing half-cycle durations, illustrating convergence to the predicted \(\tau^{-2/3}\) law.

The analytic theorem is not inferred from numerical fits. The proof of existence and the all-global-maximizer asymptotic rests on the strict hyperbolic envelope, uniform expansion and nonnegative-deficit bounds in `RESULT.md`. The verifier does not claim an exhaustive scan or finite-stage uniqueness. It does not compute or include the physical energetic cost of implementing resets; a separate model is required for any net-efficiency claim.
