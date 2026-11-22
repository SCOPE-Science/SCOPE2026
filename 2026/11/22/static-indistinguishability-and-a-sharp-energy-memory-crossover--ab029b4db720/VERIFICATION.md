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

# Reproducible verification

The accompanying standalone `CHECK.py` is runnable with Python 3, SymPy, NumPy, and SciPy using `python CHECK.py` from the extracted directory. It checks stationary generator identities symbolically, the exact value of \(\operatorname{Var}(X^2)\), and the continuous \(r=2k\) limit; evaluates an independent finite-dimensional matrix exponential for the conditional moments at 80 positive-parameter samples in both protocols; and evaluates a two-state Fourier resolvent for the stationary characteristic function. Completed output: `PASS: 380 independent numeric assertions; 14 symbolic generator / normalization assertions`.

The all-parameter strict positivity proof is analytic; finite numerical checks are not used to infer global uniqueness or an infinite asymptotic. Prior-source overlap was assessed from inspected accessible full HTML and available metadata, with the inaccessible complete Bressloff (2020) text explicitly identified as an originality-risk limitation. External independent scientific validation has not been performed.
