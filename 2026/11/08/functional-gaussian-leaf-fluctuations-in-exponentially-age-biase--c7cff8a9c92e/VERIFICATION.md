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

The self-contained `verify.py` can be run with `python3 verify.py` and no third-party dependencies. It independently sums exact rational probabilities for every valid parent sequence with one to six arrivals at parameter values \(r=1/3,1/2,2/3\). For each case it compares all individual leaf probabilities, all pair probabilities, the expected total leaf count and its second moment with independent product formulas.

The program also computes truncated infinite-product approximations for \(r=0.08,0.2,0.5,0.75,0.93\) and trend checks as \(r\uparrow1\); these are **not** rigorous interval bounds. Its reproduced output reports **838 passed assertions**, no assertion failures.

The infinite theorem instead follows from the explicit independence product identity, strong-mixing approximation, conditional Bernoulli variance lower bound and a uniform finite-to-stationary coupling. The checker does not certify asymptotic normality, an infinite product exactly, numerical optimality, literature novelty or any independent mathematical review.
