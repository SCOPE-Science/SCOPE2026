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

# Verification and reproducibility

Install Python 3 with NumPy (see `requirements.txt`); execute `python CHECK.py` from the package root. The actual packaged run gave:

```
CHECK_OK assertions= 463 max_d_direct=8 max_d_formulas=44
```

The checker independently builds complete complex Fourier matrices on every ternary sphere for dimensions four through eight (rather than computing Gram entries only from the claimed formulas), compares full eigenvalue multisets with the two-by-two block formula, and checks exact integer count and moment identities. It also verifies the claimed best radius and exact condition-number expressions for each dimension from four through forty-four. These finite tests are not exhaustive for all dimensions. The manuscript supplies the general roots-of-unity computation, complete invariant-subspace decomposition, and exact case-by-case inequalities.

The one singular case is dimension four, radius two, with exactly one zero eigenvalue. All other Gram matrices in the stated range are positive definite. The smallest coefficient-eigenvalue range is not a claim about experimental noise, incomplete samples or nonlinear phase retrieval.

Independent audit: not performed.
