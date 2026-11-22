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

# Verification record

The full all-dimension argument is in `RESULT.md`. The standalone, standard-library-only program `verify.py` was executed against the exactly embedded code, with the output:

```
PASS: 132 rational graph-and-witness cases; 71991 exhaustive finite assignments; one exact sign-average check
```

The program uses `fractions.Fraction` and checks normalized Bellman inequalities for every directed edge and every coordinate in each tested instance, upper-envelope inequalities on finite rational grids, matching extremizer support, explicit pigeonhole assignments, and an exact off-diagonal sign average. It covers \(2\le n\le9\), \(1\le m\le n\), and \(\rho\in\{1/4,2/3,9/10\}\) in the parameter tests, plus assignment enumeration through dimension six. Computational coverage is finite and does not establish universal validity; the signed-support averaging and graph inequality proof do.

Claim boundaries: real finite dimension; positive contraction strictly below one; independent arbitrary modes; isotropic nonnegative stage cost; max-of-quadratics upper envelopes. This package does not verify publication priority or establish independent mathematical certification.
