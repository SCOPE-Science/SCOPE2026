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

The standalone `checker.py` uses only the Python 3 standard library and enumerates all \(n^{n-2}\) Prüfer sequences for each \(n\in\{3,4,5,6,7\}\). It independently assembles each tree and checks the weighted-tree implied binomial edge-count distribution for every prefix, the exact wedge expectation, single-edge and adjacent/disjoint-edge inclusion probabilities, and the whole-labeled-graph total-variation bound by explicitly comparing the graph probability distributions for all \(k\le\min(n,5)\).

Run `python3 checker.py` in the same directory. The recorded output is `PASS: 142 exact rational checks, all Prüfer codes for n=3,...,7`.

The verifier does **not** exhaustively enumerate trees of larger order, infer a limiting Poisson law from simulations, or independently certify the asymptotic proof. Exact formulas and asymptotic claims are established in `RESULT.md`, where the contraction, coupling, factorial-moment, and Laplace-functional steps can be inspected.

No independent audit has been performed.

