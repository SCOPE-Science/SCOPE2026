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

# Exact checks and limits

The standalone program `check_gossip_gini.py` uses Python 3 standard-library `fractions.Fraction` and `itertools.combinations` only. Execute `python3 check_gossip_gini.py` in the directory containing the program. Every input of the form \(\mathbf1_S\), with \(\varnothing\ne S\subsetneq\{1,\ldots,n\}\), is enumerated for all \(2\le n\le12\); the exact Gini seminorm is calculated before and after the one-pass averaging map. For every dimension, the exhaustive cut norm agrees with the formula derived analytically. Exact trailing-block witnesses and integer optimizers are checked. A second finite calculation verifies the claimed maximizing block size for \(9\le n\le160\).

The executed program ended with `ALL_ORDERED_GOSSIP_GINI_EXACT_CHECKS_PASS`. The exact binary reduction and all-dimensional integer minimization are proved in `RESULT.md`; finite checks cannot substitute for that proof. The program does not test alternative edge orders or claim to verify an infinite domain by enumeration. No external validation was undertaken.
