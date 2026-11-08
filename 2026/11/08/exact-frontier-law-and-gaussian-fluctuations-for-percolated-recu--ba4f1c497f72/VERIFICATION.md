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

# Verification and reproducibility

Run `python3 check_frontier.py` with Python 3 and its standard library. The checker implements independent finite Markov recursions, exact rational comparisons with complete small-tree enumeration, exact coefficient extraction from the proposed bivariate generating function, and exact stopped negative-binomial prefix counts. In the completed replay, 883 exact comparisons passed. The optional finite Monte Carlo diagnostic uses NumPy and is evidence only about finite sampling, not an asymptotic proof.

The proof establishes the finite-size identities for all integers \(n\ge1\), a stopped law for all integers \(k\ge2\), and the asymptotic laws for every fixed real \(0<p<1\). The infinite arguments use a Yule birth-process coupling, a martingale strong law and a stable bounded-increment martingale central limit theorem. Historical priority and the mathematics have not received an independent audit.
