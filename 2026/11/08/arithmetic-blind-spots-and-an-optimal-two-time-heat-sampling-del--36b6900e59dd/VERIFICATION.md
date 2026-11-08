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

# Reproducible checks

Run `python check_cycle_heat.py` with NumPy and SciPy installed. The file is a standalone calculation that reconstructs the entire spatial restriction and the heat matrix in a unitary finite Fourier basis. It checks direct Gram endpoint eigenvalues against the closed expressions at 105 pairs of even cycle order and positive delay, verifies singularity for the divisible-by-four class and strict positive lower bounds for the other class, and evaluates the scaled best lower bound at six larger admissible cycle orders. The run records:

```
tau 0.55442877643927 sharp_N_squared_constant 1.19133546764856
n 10 topt 0.5738706090 scaled_A_ratio 0.994147908
n 22 topt 0.5583646373 scaled_A_ratio 0.998843706
n 42 topt 0.5555046031 scaled_A_ratio 0.999685455
n 102 topt 0.5546109448 scaled_A_ratio 0.999946813
n 202 topt 0.5544751955 scaled_A_ratio 0.999986444
n 502 topt 0.5544362512 scaled_A_ratio 0.999997805
CYCLE_TWO_TIME_HEAT_PASS direct_bound_comparisons 105 asymptotic_scales 6
```

The analytic argument supplies an exact Fourier block decomposition, spectral monotonicity proof, compact-uniform convergence, and endpoint control; finite tests cannot establish any statement quantified over all even cycle sizes. Numerical optimizers are not claimed as exact rational certificates. Independently reproduced mathematical assessment has not been performed.
