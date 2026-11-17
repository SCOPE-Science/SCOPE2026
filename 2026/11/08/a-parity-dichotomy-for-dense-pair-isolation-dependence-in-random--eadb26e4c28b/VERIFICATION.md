---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Parity character projection gives P_m(p)=2^{-m}sum_k binom(m,k)(1-2p)^{k(m-k)}, with P0=1. The unconditioned probabilities of one and two isolated vertices are q^{n-1}P_{n-1} and q^{2n-3}P_{n-2}, so exact conditioned covariance is q^{2n-3}(P_{n-2}P_n-qP_{n-1}²)/P_n². At p=1/2 the even-degree subspace has size 2^{(n-1)(n-2)/2}, giving the exact positive value. For even n, complement of even-degree graphs has all degrees odd; smallest edge count n/2 gives only perfect matchings, so P_n~(n-1)!!q^{n/2}, while P_{n-1}->1. The one-point square dominates the joint q^{2n-4}/(n-1), making the negative coefficient. For odd n the complete graph is even-degree, so P_n,P_{n-2}->1 and positive pair term dominates. n=4 direct even graph enumeration gives p³q²(2-3p)/(6p²-4p+1)² and unique zero 2/3. Independent rational brute enumerations of all graphs n=3,4,5 at p=1/2,2/3,4/5 agreed; source longer finite checker was inspected rather than trusted as proof.

## originality

PASS

Grimmett–Janson earlier define and analyze random even graphs, parity partition functions and related forbidden-degree ensembles, and enumerate small n=4 cases; they do not explicitly establish the fixed-n all-orders conditional pair-isolation covariance sign dichotomy in the material inspected. Related Resultary 2026/11/08 findings concern incident/disjoint EDGE covariance in the same ensemble, and unconditioned isolation vs odd-degree covariance, not the pair of isolation indicators under all-even conditioning. No dominating source identified, with residual risk of a hidden covariance corollary in classical random-cluster work.

## value

PASS

A sharp sign reversal created by conditioning independent edges on global degree parity is a structurally motivated counterexample to naive positive-association intuition. The full parity split, fixed-order dense asymptotic coefficient and exact n=4 threshold clarify when global parity constraints reverse local dependence, beyond the classical even-graph model itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
