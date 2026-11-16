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

# Reproduction and checks

Execute `python3 check_cayley.py` using Python 3 standard library. This independent rational-coefficient integration constructs the unnormalized \(\mathrm{Beta}(4,8)\) radial weight \(x^3(1-x)^7\), multiplies by the three sector weight polynomials, integrates by exact rational arithmetic, and divides by the full integral to calculate each cap eigenvalue. It compares the results with the explicit closed-form sector polynomials at 17 distinct rational heights. Each polynomial identity involved has degree at most 13, so 17-point equality proves those polynomial identities exactly for all real \(t\). The same procedure verifies the three factored spectral gaps and 26-dimensional trace. A separate fixed-distance norm test, crossing tests, strict sign-order sample tests and the thin-cap leading-coefficient identity are also included.

Successful execution prints:

```
CAYLEY_26_THREE_BRANCHES_EXACT_POLYNOMIAL_PASS 17-point degree-13 identities
CAYLEY_SPIN9_PEIRCE_NORM_IDENTITY_PASS
CAYLEY_TWO_CROSSINGS_TRACE_ORDER_AND_ASYMPTOTIC_PASS
```

The geometric premises are mathematical, not computational: the 1+16+9 Spin(9) decomposition of the first nonconstant \(F_4\) module, the primitive-idempotent block norm identities, and the \(\mathrm{Beta}(4,8)\) invariant radial law. Their proof is in RESULT.md and their context in the cited primary geometry and harmonic-analysis sources. The code is not a substitute for these premises. No external or independent mathematical audit is represented.
