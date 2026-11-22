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

The symbolic proof in `RESULT.md` reduces ordered zero-product counts to a rank computation on \(J/Z_0\) and \(Z_0/W_0\). Its source-dependent assumptions are the order-64 classification, multiplication normal forms and completeness statements in arXiv:2611.16086v1.

The standalone script `verify_zero_products.py` independently evaluates all \(32\times32\) ordered radical-element pairs for each of the 88 canonical representatives, using bilinear multiplication over additive groups of type \(\mathbb F_2^5\), \(\mathbb Z_4^2\oplus\mathbb Z_2\), and \(\mathbb Z_4\oplus\mathbb Z_2^3\). It checks the same 88 direct counts against the structural formulas, validates all eight multiplicities, and reports:

```
MINIMAL_CENTRAL_ESSENTIAL_ZERO_PAIRS_OK 88
zero_pair_count : isomorphism_class_count
320 8
352 12
384 6
416 5
448 18
480 24
512 8
608 7
```

The script is an exhaustive arithmetic check for the published representative list. The infinite mathematical claims in the cited classification and the completeness/nonisomorphism of its representatives are input, not independently certified by this check. No independent audit has been performed.
