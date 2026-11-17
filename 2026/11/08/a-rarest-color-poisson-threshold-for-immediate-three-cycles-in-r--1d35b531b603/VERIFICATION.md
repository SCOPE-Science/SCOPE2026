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

The exact conditional binomial-sum law follows from disjoint unordered edge tests: each edge between colors i and i+1 is queried only for the color-i endpoint, so deficiency indicators of all sources are independent. Multinomial coloring then gives the finite product. Uniform multinomial deviations <=n^(2/3), n p_n^2=o(1), and Le Cam sum-of-squares ->0 give TV-Poisson mean exp(-t) times the sum of predecessor color masses for rarest successors. Since min mass <=1/3, the n p >=3 log n connectivity union bound holds, identifying B_n=0 with primitive-three dynamics from time zero with error o(1). Monotone edge coupling extends zero-one threshold outside fixed t windows. Exact proof distinguishes connected from disconnected graphs; finite tests not relied upon as infinite proof.

## originality

PASS

The nontrivial contribution is the time-zero all-rotating criterion, exact finite coloring/edge conditional law, and rarest-color Poisson window. The 2018 GHM literature treats eventual limiting activity at G(n,lambda/n), not this log(n)/n full initial periodicity probability; Poisson approximation alone does not identify the correct independent Bernoulli indicators. No stronger same claim found in the Resultary nearby entries; priority remains best-of-knowledge.

## value

PASS

The initial-periodic versus eventually oscillatory distinction is mathematically natural, and a sharp rare-color critical window with exact bias-dependent Poisson parameter provides a quantitative structural phase transition beyond routine use of a generic Poisson theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
