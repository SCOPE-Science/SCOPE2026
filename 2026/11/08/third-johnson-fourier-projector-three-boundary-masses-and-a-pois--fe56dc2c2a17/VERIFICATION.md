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

The file `verify_johnson3.py` is a standalone Python 3 checker. It uses rational Gaussian elimination and exact integer hypergeometric weights, and replays the kernel/telescoping identities on all 784 pairs with n from 6 through 60 and k from 3 through floor(n/2). It also constructs complete projection matrices for sizes 20, 35, and 56 and tests idempotence with rational arithmetic. The printed cusp number and bulk asymptotic are corroborative finite-precision checks; the theorem's infinite limits and derivative jump are established analytically in RESULT.md. The independent mathematical audit has not been performed.
