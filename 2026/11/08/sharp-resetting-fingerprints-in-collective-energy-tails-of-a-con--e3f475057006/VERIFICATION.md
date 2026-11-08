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

The source file `verify.py` is included alongside this document. From the extracted package directory run:

```
python3 verify.py
```

The packaged source was run and returned `PASS: 105 independent finite/numerical comparisons`. It uses only Python's standard library, a self-contained regularized-incomplete-gamma tail, a beta-mixture quadrature, factorial/gamma moment identities, and the closed-form asymptotic constants. Checks cover \(b\in\{1/2,1,2,3\}\) for independent moment identities, the critical and fixed-supercritical tails at multiple particle counts, the Gaussian crossover for \(x\in\{-2,0,2\}\), and a chi-square exact control case.

The analytical proof of the universal limits is in `RESULT.md`. Numerical quadrature is bounded evidence and cannot certify all parameter values or the \(N\to\infty\) limit. No independent scientific audit or independent validation has been performed. The principal source already gives the stationary joint distribution and is explicitly credited; the claimed result is the sharp collective-energy tail characterization.
