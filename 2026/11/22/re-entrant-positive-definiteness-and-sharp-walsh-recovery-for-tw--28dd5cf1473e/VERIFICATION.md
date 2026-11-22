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

The standalone `verify.py` uses Python standard-library integer arithmetic, fractions and exhaustive permutation generation. Executing `python verify.py` produced:

```
PASS 17890 exact assertions; all signs, spectral gaps and boundary cases verified in the displayed finite scope.
Proven infinite assertions require the independent symbolic recurrence and induction in RESULT.md.
```

The direct check enumerates every permutation through \(n=7\), weights it by the number of two-colour cycle choices, and computes Walsh sums independently of the closed formula. A second exact check runs the binomial formula and recurrence through \(n=180\); a third uses the independent exponential generating function \(e^{-4z}(1-z)^{-2}\) through \(n=90\). Boundary spectra through \(n=8\), sharp gaps at orders six and eight, and exact condition numbers are checked. The argument for all integers \(n\) is the written induction, not a finite verification certificate.

The package needs no third-party libraries, downloads or hidden data. The six core documents and the verifier are complete and self-contained. Independent validation has not been performed.
