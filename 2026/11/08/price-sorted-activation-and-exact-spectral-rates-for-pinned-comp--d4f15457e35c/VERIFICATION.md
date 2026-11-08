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

# Reproduction and verification limits

Execute `python3 verify.py` using Python 3.10 or later; only the Python standard library is required. The verifier deterministically checks exact-rational active-set and reciprocal-rank-one identities, exact matching of adjacent phase costs and first derivatives, and independently evaluates smallest eigenvalues of random feasible gain vectors via a scalar secular equation.

On the inspected package code, the verification output was:

```
PASS: exact active-set and rank-one certificates: 266
PASS: exact continuity and first-derivative transitions: 280
PASS: independently evaluated feasible-budget comparisons: 15600
TOTAL_CHECKS: 16146
```

The analytic proof in `RESULT.md` establishes every positive-price, every-budget assertion; finite experiments do not establish universal claims, optimality beyond the proven certificate, novelty or independent certification. The numerical comparisons have ordinary floating-point tolerance, while the first two groups use exact rational arithmetic. No external independent audit or validation has been performed.
