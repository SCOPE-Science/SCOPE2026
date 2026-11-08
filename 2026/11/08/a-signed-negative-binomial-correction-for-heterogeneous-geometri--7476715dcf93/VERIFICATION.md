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
# Reproducibility and limits

Run `python3 check_geometric.py` using Python 3 standard library only. The expected result is `PASS: 3873 exact-rational assertions (finite coefficient diagnostics; not an infinite proof).` The script tests finite prefixes and exact algebraic identities for multiple parameter choices; it does not exhaust infinite tails or all parameter values.

The rigorous global conclusion relies on the signed generating-function identities, absolute convergence in \(\ell^1\), and the norm bounds \(\|A'_y\|_1=2/(1-y)^2\), \(\|A''_y\|_1=4/(1-y)^3\). The exact local leading coefficient further requires the sign-change analysis of the factorially tilted negative-binomial mass. The signed target has total mass one but can have negative coefficients.

Independent mathematical audit has not been performed. Historical priority relative to earlier general signed-measure expansions is still provisional.
