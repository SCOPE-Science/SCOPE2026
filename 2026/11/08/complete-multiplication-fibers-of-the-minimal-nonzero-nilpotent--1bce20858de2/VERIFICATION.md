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
# Verification of the exact minimal-nilpotent product spectrum

The proof is algebraic and applies to every finite field and matrix size at least two. Direct exhaustive matrix calculations were performed independently of the counting derivation, with standard-library Python `check_minimal_nilpotent_product.py`; its actual stdout is embedded as `verification_output.txt`.

The program enumerates every nonzero normalized rank-one square-zero matrix, constructs all ordered products, then enumerates every matrix target and compares the observed fiber size with the piecewise formula. It implements multiplication in extension fields of orders 4 and 8 by polynomial reduction; order 8 is included for arithmetic support but not in the nine reported exhaustive settings.

Executed complete checks: (2,2), (2,3), (2,4), (2,5), (3,2), (3,3), (3,4), (3,5), (4,2), where each tuple means (dimension, field order). Each output row records the number of nonzero rank-one nilpotents, all tested ordered pairs, the product-image size, the zero fiber, and the trace-zero and nonzero-trace nonzero target populations.

These are finite confirmations only, not formal proof of the general theorem. The general proof consists of the outer-product normalization, a restricted pairing rank computation, and a direct zero-product incidence count. No independent audit has been performed.
