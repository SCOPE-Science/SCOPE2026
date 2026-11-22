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

# Verification evidence and boundaries

Run `python3 verify_spread.py` using Python 3 with only the standard library. The checker independently integrates the liquid spatial first moment directly and the gas spatial moment using an exponential change of variable, and compares their normalized sum against the proposed closed expression. It also checks open-boundary limits and sample points in the three global regimes. A completed invocation printed: `PASS: 199 quadrature, boundary, and optimizer checks`.

The exact derivative identity and factorization in `RESULT.md` prove the global sign and uniqueness assertions; the finite checks do not certify uncountably many parameters. They do not validate a microscopic stochastic model or independent publication priority. The source profiles are those of Grange, arXiv:2610.26149, and the comparison with related transport and flux geometry results is set out in `REVIEW.md` and `AUDIT.json`.
