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

The stated rank identity follows from an exact monomial projection formula, a nonzero leading anti-diagonal after polynomial-pencil elimination, and a skew-symmetric bilinear pairing that forces even rank. The centered Wronskian degree is determined by the two distinct leading degrees, and the analytic range/vanishing-on-analytic-domain property proves square zero.

`check_rank.py` runs with Python 3 and no third-party modules. Its exact-rational deterministic suite tests 1305 pairs, including every coefficient triple in a small finite grid and seeded higher-degree pairs, and checks both the rank formula and weighted skew-symmetry. These checks were run successfully on the packaged source. They are finite diagnostics, not an exhaustive universal proof.

The closest published general finite-rank classification gives finiteness and square-zero, while quasihomogeneous rank formulas cover individual monomial-type symbols. The 2013 general rank paper was not available in full during this comparison; its possible additional polynomial results are a residual originality risk. No separate external verification or independent mathematical audit has been performed.
