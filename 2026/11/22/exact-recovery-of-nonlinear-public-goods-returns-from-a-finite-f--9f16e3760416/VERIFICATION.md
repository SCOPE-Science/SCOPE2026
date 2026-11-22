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

# Verification notes

Run `python3 verify_inverse_public_goods.py` after extracting the attached standalone script. Its exact checks separately implement the cooperator/defector hypergeometric sums, the coefficient matrix, and the triangular inverse; it verifies 198 positive rational-return parameter cases for \(3\le N\le13\), \(2\le n<N\), together with numerical profile reconstruction. It checks the exact \(N=4,n=3\) fixation certificate at \(\beta=\log2\), and 36 whole-population group cases. The checker output was:

```
PASS: 198 rational/numerical profile-and-recovery cases; exact 4-person certificate; 36 full-group degeneracy cases
```

Proof for all \(N,n\) does not depend on this finite enumeration. Mathematical conditions, explicit inverse and the exact large-population sensitivity are proved in `RESULT.md`. No independent scientific validation has been performed. The precision statement refers only to differential dependence of exact log-curvatures, not sampling-error guarantees.
