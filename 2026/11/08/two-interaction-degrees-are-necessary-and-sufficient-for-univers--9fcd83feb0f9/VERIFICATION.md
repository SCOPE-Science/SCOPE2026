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

# Reproducibility checks

Run `python check_orders.py` with SymPy to reproduce the exact symbolic tests. The program verifies the two-degree polynomial jet identities and the full completed population Jacobian for several dimensions, degree pairs, and rational baselines. It also verifies the radial derivative identity for one-degree examples, including strictly competitive pairwise interactions.

The mathematical proof is independent of the finite tests: all dimensions and all integer degree pairs are covered by direct differentiation and homogeneity; arbitrary finite interaction supports are handled by selecting any two degrees or showing that the support has at most one degree. The proof requires free real higher-order coefficients, repeated-index monomials and local (not global) stability. No third-party independent audit has been performed.
