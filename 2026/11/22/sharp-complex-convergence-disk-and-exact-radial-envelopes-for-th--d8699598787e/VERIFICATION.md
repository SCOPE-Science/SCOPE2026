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

The mathematical certificate is the positive-coefficient argument in `RESULT.md`; no independent audit is claimed. The exact rational recurrence for the tangent coefficients follows from \((\tan z)'=1+\tan^2 z\). It proves strict positivity at every order, hence the global holomorphic majorant on \(|z|<\pi/2\). The unique radius \(R\) solves \(\tan R=2R\), and the real extremizers achieve equality for all finite iterates.

Execute `python3 check.py` using only the Python standard library. The recorded output is:

```
PASS: 991 numerical majorant/orbit checks; 13 exact tangent coefficients; R=1.165561185207211
```

The script evaluates 13 exact rational coefficients, finitely samples the complex modulus inequality on six circles, checks the real saturation of seven iterates on each circle, and samples 49 nonreal points on the critical circle. The precise decimal is a numerical approximation, not a certified algebraic root. Finite checks cannot establish the universal quantifiers, basin connectedness or originality; these rest on the analytic proof and inspected literature comparisons.
