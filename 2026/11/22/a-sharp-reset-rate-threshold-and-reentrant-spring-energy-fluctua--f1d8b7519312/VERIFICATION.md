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

Execute `python verify.py` with Python 3 and SymPy. The script explicitly solves all three stationary degree-two and five degree-four moment-generator identities, verifies the exact signed jump mean and rational squared coefficient-of-variation endpoints, certifies the unique quartic zero and rational bracket, and determines the exact sign pattern of the derivative numerator on the entire stated reset-rate interval. All interval sign inequalities use exact rational Bernstein coefficients; there is no discretization of the interval, approximate numerical differentiation or inference from floating-point roots. The derivative denominator is certified positive coefficientwise. An independent substitution check covers two distinct rational parameter pairs.

Optional `python simulate.py` uses NumPy and independent exact conditional Gaussian inter-event increments to approximate the signed jump statistics. Its finite samples may fluctuate and do not certify any identity, extremum or infinite statement.

The existence and moment assertions follow from contractive inter-reset affine dynamics. The claimed limits take stationarity first and vary positive bath friction afterwards. Neither a physical implementation of instantaneous resetting nor the cumulative work distribution is verified. Independent validation or audit has not been performed.
