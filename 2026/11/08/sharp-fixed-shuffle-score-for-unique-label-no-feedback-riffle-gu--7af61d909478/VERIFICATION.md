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

# Reproducible checks and limits

Run `python3 checks/verify.py` from the extracted package root. The script requires only the Python standard library. It constructs the exact marginal probability matrix as a mixture of two binomial laws with rational probabilities, checks that all row and column sums equal one, verifies the concrete unique-label guessing strategy is a permutation, and computes exact finite-deck optimal assignments by subset dynamic programming. It checks that the constructed score is bounded between zero and the true finite optimum, and that the optimum does not exceed the column-capacity bound. It also evaluates the proposed fixed-shuffle leading coefficients and compares the one-shuffle closed form \(\sqrt{2/\pi}\).

The expected standalone output includes `Exact checks passed: 61` and leading constants \(0.797884560803\), \(0.337225694841\), and \(0.160563316492\) for mixture sizes \(2\), \(4\), and \(8\). The finite checks do not prove an infinite asymptotic or the novelty of a claim. The analytical proof in RESULT.md supplies the separation, local-limit, capacity, and Riemann-sum steps; it depends on classical bounded-Bernoulli local-limit estimates.

Scope of the checks: finite decks with up to twice the number of mixture components for \(m\in\{2,4,8\}\), exact normalization and finite assignment inequalities; no external certification or independent mathematical audit is claimed.
