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

# Reproducibility and boundaries

The complete universal argument is given in `RESULT.md`. In particular, its first step supplies the exact critical Zak multiplier, the second step classifies all zeros in the one-sided fundamental rectangle, and the third step derives the constrained quadratic minimization responsible for the universal coefficient. This uses the classical density-one Zak criterion and ordinary partial-fraction identities; it requires no symbolic or external proof software.

Running `python3 checker.py` using only the standard library produced the output:

```
PASS 188 finite formula/circle/root/onset/truncation checks
Scope: standard-library finite numeric diagnostics; no infinite theorem is inferred.
```

Checks cover four strictly positive pole heights, explicit cotangent-circle identities, one-sided critical zeros, interior zeros on the unstable side, first-order convergence of the lower-bound ratio, and Fourier-series partial-fraction consistency. The checker does not exhaust all pole heights or parameter values; finite numerical checks are not certificates of infinite-dimensional frame or completeness properties. The analytic proof establishes these properties under the explicitly stated hypotheses. Inaccessible or unindexed historical sources could affect priority. Independent validation has not been performed.
