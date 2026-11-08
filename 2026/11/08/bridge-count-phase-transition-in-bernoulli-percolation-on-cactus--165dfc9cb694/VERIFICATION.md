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

# Reproduction and limits

Run `python verify_cactus.py` using Python 3 standard library only. It enumerates all \(2^m\) retained edge subsets for each of eight small cactus graphs, independently evaluates bridges by graph traversal, and checks exact rational joint probabilities, conditional means at each feasible retained-edge budget, and covariance identities at retention probabilities \(1/5\), \(1/2\), and \(4/5\). It additionally checks conditional concavity and the threshold inequality. There are 24 Bernoulli-model comparisons and eight finite-cactus concavity checks. The tests passed in the package environment. They are finite reproducibility checks, not proofs for general graph order.

The all-size proof in `RESULT.md` relies on the edge-disjoint cycle decomposition, independent edge indicators, and explicitly differentiated falling factorials. The argument does not cover overlapping cycles or inhomogeneous edge retention. Independent external audit was not performed.
