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

# Reproducibility and boundaries

Run `python3 verify.py` in the folder containing this file. It uses only the Python standard library, constructs the three-order gain with exact `Fraction` arithmetic, checks the exact cubic and its polynomial factorization, verifies endpoint/midpoint signs and a positive lower bound on its second derivative, then performs 640 seeded rational convexity tests on additional finite mixtures. The bundled script was executed successfully from the delivered-file content before packaging.

The general theorem for arbitrary finite or countable mixtures is proven by positivity, uniform convergence, convexity and one-dimensional flow analysis; finite rational tests do not certify the universal assertion. The exact example does not prove robustness for every perturbation of the mixture, nor does the theorem govern adaptive mixing, stochastic fixation or finite hypergraph dynamics. Scientific originality was assessed by comparison with the two-order primary preprint and the random-size public-goods literature; equivalence outside the inspected sources remains possible. Independent audit is not performed.
