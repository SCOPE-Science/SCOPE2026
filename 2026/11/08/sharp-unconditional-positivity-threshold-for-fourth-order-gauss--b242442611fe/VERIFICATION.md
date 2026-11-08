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

# Verification of the all-step threshold

The analytic argument in `RESULT.md` establishes the infinite-family theorem for all integers \(p,q\ge2\), ratios \(t\ge0\), scales \(b>0\), and steps \(h\ge0\). The Python 3/SymPy script `artifacts/verify.py` independently reconstructs all three off-diagonal rational identities and checks full completed matrices obtained by exact inversion of the rational Padé denominator.

Replay from the extracted package directory: `python artifacts/verify.py`.

Observed exact-arithmetic output:

```text
SYMBOLIC_FACTOR_IDENTITIES_OK
EXACT_MATRIX_CASES_OK 384
SHARP_NEGATIVE_WITNESS_CASES_OK 108
```

The full-matrix test covers \(p,q\in\{2,3,4,5\}\), \(t\) equal to zero, one, half the threshold, the threshold, the threshold plus one third, and twice the threshold (deduplicating ratios where necessary), and four positive rational steps. The symbolic factorization and sign argument, not this finite grid, certify all parameters. The script does not establish any claim about floating-point positivity, internal-stage positivity, or a different graph family. Independent mathematical audit has not been performed.
