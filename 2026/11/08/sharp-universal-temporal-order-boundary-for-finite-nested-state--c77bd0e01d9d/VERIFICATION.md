---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every depth i>=3 and every q in [nu_i,1), with sum_{k=1}^{i-1}nu_i^k=1, choose eta=q/2, a 2-Lipschitz piecewise-affine small history and distinct separated initial nesting points y_1,...,y_{i-1}. Local slope assignments v_1=...=v_{i-2}=-2, v_{i-1}=+2 retain all values and force d_i prime=1-sum_{k=1}^{i-1}q^k on an actual common interval. This is zero at nu_i, negative above. The relay reference g has |g|<=1+||phi||_infty so eta|g|<1, and every invisibility hypothesis with c=1 is satisfied; source Theorems 1.1 and 5.1 give global trajectory coincidence and the sufficient q<nu_i direction. Tested independent recurrence algebra at representative depths; finite tests only corroborate the quantified piecewise-linear proof. No smooth-history assertion.

## originality

PASS

The motivating paper supplies nu_i as sufficient for temporal order, not exact all-depth sharpness or a genuine plateau at equality. A separate published same-day boundary at q=1 describes loss of trajectory invisibility, a different property from finite-depth loss of monotonic delayed arguments while invisibility survives for q<1. Walther 2009 concerns implicit/algebraic delay, but complete priority comparison limited by inaccessible text.

## value

PASS

Solves a precise sharpness question raised by a natural published universal sufficiency condition, for every finite nesting depth including equality, and separates time-order failure from trajectory invisibility; these are structural dynamical statements rather than parameter substitutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
