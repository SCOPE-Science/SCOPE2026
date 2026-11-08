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

# Verification and limits

The analytical proof is given in `RESULT.md`; `verify_edge.py` is a separate reproducibility diagnostic. Run the script with Python, NumPy and SymPy installed. It symbolically verifies the derivative identities for the half-\(t\) waiting-time density, survival, equilibrium residual tail, its mean and its first asymptotic coefficient. It then constructs a stationary equilibrium-age sample and approximates the past of the alternating renewal signal by 96 completed runs; the forgotten remainder of the linear filter is exponentially attenuated in the total simulated past duration.

The checker evaluates four small-edge probabilities using a fixed random seed, compares them with the rigorous renewal-age lower bound and a valid upper bound, and tests the equilibrium-age marginal. These finite diagnostic computations do not certify the universal regular-variation theorem; the proof in `RESULT.md` supplies its quantifiers and limits. Results concern stationary cumulative probabilities and do not imply pointwise density asymptotics, noise-robust inference, or an infinite-mean stationary regime.
