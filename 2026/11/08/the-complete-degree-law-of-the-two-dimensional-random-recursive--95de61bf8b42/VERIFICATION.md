---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The eligible-face incidence probability of a vertex of degree k is exactly (k+1)/(n+E_n), giving all conditional degree-count drifts without an independence assumption for the two endpoints of a chosen edge. Edge density x=E_n/n solves stable stochastic approximation to golden ratio phi. The stated bounded martingale-increment stability lemma applies to each fixed degree class by induction; the countable intersection yields simultaneous almost-sure limits. Summing the fixed-point balances gives (1+phi) sum_(k<=K) p_k =1+phi-(K+1)p_K, and the gamma ratio gives K p_K->0, hence normalized distribution and total variation. Correct boundary degree classes and no claim for k=k(n). Independently recomputed p1,p2 and partial mass through 100000 (~0.999999999998).

## originality

PASS

The Krapivsky–Lucas RRSC(2) paper computes only leaf fraction p1 and heuristically anticipates exponent phi+2, expressly identifying p2 and higher degree densities as open calculations. The current exact p2, all-k normalized gamma distribution, almost-sure convergence and positive prefactor are not implied by that exponent or leaf fraction; the fixed-dimension face-selection models are not the same pooled vertex-or-edge rule. Current Resultary results on primordial degree and edge triangle incidence do not cover empirical degree frequencies. Originality accepted best-of-knowledge.

## value

PASS

Complete exact vertex-degree law for the motivating model and a rigorous solution to a clearly stated higher-degree calculation gap; normalization and almost-sure total-variation convergence are useful structural results beyond a guessed tail exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
